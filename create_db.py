from market import app, db
from sqlalchemy import text
from models import Item
    
with app.app_context():
    try:
        db.create_all()
        print("Table created successfully!")
    except Exception as e:
        print("Table creation failed:", e)