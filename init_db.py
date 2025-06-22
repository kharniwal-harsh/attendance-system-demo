from database import teachers_collection
from datetime import datetime

def init_db():
    # Check if admin user already exists
    admin = teachers_collection.find_one({"username": "admin"})
    if not admin:
        # Create admin user if it doesn't exist
        teacher_data = {
            "username": "admin",
            "password": "admin123",  # In production, use a secure password
            "email": "admin@example.com",
            "created_at": datetime.now()
        }
        teachers_collection.insert_one(teacher_data)
        print("Admin user created successfully!")
    else:
        print("Admin user already exists!")

if __name__ == "__main__":
    init_db()
