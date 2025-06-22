import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    print("Warning: MONGO_URI not found in environment variables")
    print("Checking .env file...")
    from dotenv import load_dotenv
    load_dotenv()
    MONGO_URI = os.getenv("MONGO_URI")
    if not MONGO_URI:
        raise ValueError("No MONGO_URI found in environment variables or .env file!")

try:
    # Connect with a timeout and additional options for Atlas
    client = MongoClient(MONGO_URI, 
                        serverSelectionTimeoutMS=5000,
                        connectTimeoutMS=5000,
                        socketTimeoutMS=5000,
                        maxPoolSize=50)
    # Verify connection
    client.server_info()
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {str(e)}")
    raise

db = client["attendance_system"]
teachers_collection = db["teachers"]
students_collection = db["students"]
classes_collection = db["classes"]
attendance_collection = db["attendance"]

