# Twitter Trends Scraper and Viewer

This project is a web application that scrapes current Twitter trends using Selenium, stores them in a MongoDB database, and provides a Flask API to fetch and display the trends on a frontend interface.

## Project Overview

- **Backend**: Flask, MongoDB, Python
- **Frontend**: HTML, CSS, JavaScript
- **Tools Used**:
  - Selenium for scraping Twitter trends
  - MongoDB for storing the scraped trends
  - Flask to create the API
  - CORS for handling cross-origin requests
  - dotenv for managing environment variables
  - **ProxyMesh** for handling proxy-based requests to bypass any IP restrictions on Twitter.

## Project Structure


## Setup and Installation

### Prerequisites

1. **Python 3.x**  
   Ensure that you have Python 3.x installed on your system. If not, download it from [here](https://www.python.org/downloads/).

2. **MongoDB Cluster**  
   Set up a MongoDB Atlas cluster if you don’t have one. Follow the instructions [here](https://www.mongodb.com/cloud/atlas) to create an account and cluster.

3. **ChromeDriver**  
   Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches the version of your Chrome browser.  

4. **ProxyMesh Account**  
   You can use ProxyMesh to access Twitter trends through a proxy. Follow the instructions on their site to create an account and get your credentials. ProxyMesh helps to bypass IP restrictions, making it easier to scrape Twitter trends without getting blocked.

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aadarsh2904/Twitter_trends.git
   cd Twitter_trends

2. Create and Activate a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies
   ```bash
  pip install -r requirements.txt

4. Create a .env file
Add your MongoDB URI, ChromeDriver path, and ProxyMesh credentials to the .env file.

```bash

MONGO_URI="mongodb+srv://your-mongo-username:your-mongo-password@cluster0.mongodb.net/"
CHROMEDRIVER_PATH="C:\\path\\to\\your\\chromedriver.exe"
PROXYMESH_PROXY_URL="your-proxy-username:your-proxy-password@us-ca.proxymesh.com:31280"

5. Run the Flask App

python flask_app.py

6.Start the Web Scraper

python app.py

1. Scraping Twitter Trends
Selenium is used to open a browser and navigate to the Twitter/X trending page (https://x.com/explore/tabs/trending).
The scraper collects trending topics and stores them in the MongoDB database with a timestamp and the system's IP address.
ProxyMesh is used to route the traffic through a proxy server. This helps bypass any IP blocks or rate-limiting that might be placed on your IP by Twitter during scraping.
2. Storing Data in MongoDB
The data is stored in MongoDB under the twitter_data database and trends collection.
Each document contains:
A unique ID
A dictionary of trends (ranked)
A timestamp for when the trends were scraped
The IP address used to fetch the trends
3. Fetching Data via Flask API
The Flask app provides two endpoints:
/get_trends: Returns the most recent trends from the database.
/store_trend: Allows for manually storing trends (via POST request).
4. Frontend (HTML, CSS, JS)
The frontend displays the trends fetched from the Flask API.
When the user clicks "Load Trends," the browser sends a GET request to /get_trends to fetch the latest trends from MongoDB.
The trends are displayed in a list, showing the rank and the trend topic.
5. Displaying Trends
When trends are fetched:
The page shows the IP address (simulated as a random IP).
A list of the top 15 trends is displayed.
Users can click "Show Again" to reset the view and load trends again.
Endpoints
/get_trends (GET)
Description: Fetch the most recent trends stored in MongoDB.
Response:
Success: JSON with the list of trends.
Error: JSON with error message.
/store_trend (POST)
Description: Manually store trends into the database.
Request Body: JSON object containing the trend data (including timestamp and trends).
Response:
Success: JSON with success message and the inserted document ID.
Error: JSON with error message.
Environment Variables
MONGO_URI: Your MongoDB URI for connecting to the database.
CHROMEDRIVER_PATH: Path to your local chromedriver.exe file.
PROXYMESH_PROXY_URL: Your ProxyMesh proxy URL and credentials (if using proxy).
Troubleshooting
MongoDB Connection Issues: Ensure your MongoDB URI in the .env file is correct and you have access to the cluster.
ChromeDriver Issues: Ensure the version of chromedriver.exe matches the version of Google Chrome installed on your system.
ProxyMesh Issues: Verify that your ProxyMesh credentials are correct and the proxy URL is valid





