from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MongoDB URI is not set in environment variables")

client = MongoClient(MONGO_URI)
db = client["twitter_data"]
trends_collection = db["trends"]

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/get_trends', methods=['GET'])
def get_trends():
    try:
        trends = list(trends_collection.find().sort("timestamp", -1))

        for trend in trends:
            trend['_id'] = str(trend['_id'])

        return jsonify({"success": True, "data": trends})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/store_trend', methods=['POST'])
def store_trend():
    try:
        trend_data = request.json
        if not trend_data:
            return jsonify({"success": False, "message": "No data provided"}), 400
        
        result = trends_collection.insert_one(trend_data)
        return jsonify({"success": True, "message": "Trend data stored successfully", "id": str(result.inserted_id)}), 201
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Process Overview:
# 1. Load environment variables using load_dotenv() to get the MongoDB URI.
# 2. Connect to MongoDB using pymongo with the URI obtained from environment variables.
# 3. Set up a Flask app to handle HTTP requests.
# 4. Enable Cross-Origin Resource Sharing (CORS) for all routes using flask_cors to allow client-server communication across different origins.
# 5. Define a route '/get_trends' to retrieve all trends from the MongoDB collection.
#    - Fetch trends from MongoDB, sorted by timestamp in descending order (most recent first).
#    - Convert MongoDB's _id to a string to prevent JSON serialization issues.
#    - Return the trends as a JSON response.
# 6. Define a route '/store_trend' to store new trend data in the MongoDB collection.
#    - Accept trend data via POST request, parse the JSON body.
#    - If the data is valid, insert it into the MongoDB collection and return a success message with the inserted ID.
#    - If there is no data or an error occurs, return an error response.
# 7. Start the Flask app with debugging enabled to run the server locally.
