from pymongo import MongoClient
from dotenv import load_dotenv
import os

def migrate_data():
    load_dotenv()
    
    # Source database (local)
    source_client = MongoClient("mongodb://localhost:27017/")
    source_db = source_client["attendance_system"]
    
    # Target database (Atlas)
    target_client = MongoClient(os.getenv("MONGO_URI"))
    target_db = target_client["attendance_system"]
    
    # Collections to migrate
    collections = ["teachers", "students", "classes", "attendance"]
    
    for collection_name in collections:
        print(f"Migrating {collection_name}...")
        source_collection = source_db[collection_name]
        target_collection = target_db[collection_name]
        
        # Get all documents from source
        documents = list(source_collection.find())
        
        if documents:
            # Insert into target
            target_collection.insert_many(documents)
            print(f"✓ Migrated {len(documents)} documents in {collection_name}")
        else:
            print(f"No documents found in {collection_name}")
    
    print("\nMigration completed!")
    
    source_client.close()
    target_client.close()

if __name__ == "__main__":
    migrate_data()
