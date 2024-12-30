from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import uuid
import time
import requests

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "twitter_data"
COLLECTION_NAME = "trends"

if not MONGO_URI:
    raise ValueError("MongoDB URI is not set in environment variables")

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
trends_collection = db[COLLECTION_NAME]

def get_system_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json().get("ip")
    except Exception as e:
        print(f"Error fetching system IP address: {e}")
        return "Unknown"

def scrape_trends():
    unique_id = str(uuid.uuid4())
    public_ip = get_system_ip()
    print(f"System IP Address: {public_ip} | Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\aadar\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument('--profile-directory=Default')
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    trends = {}

    try:
        driver.get("https://x.com/explore/tabs/trending")
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        elems = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".r-18u37iz")))

        data = ""
        for elem in elems:
            data += elem.text

        start = data.find("Explore\n1\n·")
        end = data.rfind("posts")

        for _ in data[start:end].split("posts"):
            temp = _.split("\n")
            if temp[1].isdigit():
                trends[temp[1]] = temp[4]

        trends_document = {
            "unique_id": unique_id,
            "trends": trends,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": public_ip,
        }

        trends_collection.insert_one(trends_document)
        print("Trends successfully saved to MongoDB:", trends_document)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to close the browser...")
        print("Closing...")
        driver.quit()

if __name__ == "__main__":
    scrape_trends()

# Process Overview:
# 1. Load environment variables using load_dotenv() to get MongoDB URI.
# 2. Connect to MongoDB using pymongo with the URI obtained from environment variables.
# 3. Fetch the system's public IP address using requests.get() from the ipify API.
# 4. Setup Selenium WebDriver with ChromeOptions to load a specific user profile for browsing.
# 5. Open the Twitter/X trending page and wait for the page to load.
# 6. Extract trend elements from the page using Selenium's WebDriverWait and CSS selectors.
# 7. Parse the extracted data to identify the trends (rank and trend name).
# 8. Create a MongoDB document to store the scraped data including a unique ID, trends, timestamp, and system IP address.
# 9. Insert the document into the MongoDB database.
# 10. Handle any exceptions that may occur during the scraping process.
# 11. Close the browser after the scraping is completed.
