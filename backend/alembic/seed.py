# backend/seed.py

from backend.db.session import SessionLocal
from backend.models.user import User

def seed():
    db = SessionLocal()

    try:
        # Check if seed already applied (optional)
        if db.query(User).first():
            print("Seed data already exists.")
            return

        # Add seed data
        users = [
            User(email="alice@example.com", name="Alice"),
            User(email="bob@example.com", name="Bob"),
        ]
        db.add_all(users)
        db.commit()
        print("Seed data added.")
    except Exception as e:
        db.rollback()
        print("Error seeding database:", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed()
