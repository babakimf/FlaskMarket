from sqlalchemy import create_engine, text 
import os
from dotenv import load_dotenv

load_dotenv()

db_connection_string = os.getenv("DB_CONNECTION_STRING")

if not db_connection_string:
    raise ValueError("DB_CONNECTION_STRING environment variable is not set")

engine = create_engine(db_connection_string)

def add_item_to_db(data):
    with engine.connect() as conn:
        query = text("""INSERT INTO items (name, barcode, price, description) VALUES (:name, :barcode, :price, :description)     
        """)
        conn.execute(query, {
            "name":data['name'],
            "barcode":data['barcode'],
            "price":data['price'],
            "description":data['description']
        })
        conn.commit()
        
# data = {'id': 1, 'name': 'IPhone 10', 'barcode': '893212299897', 'price': 500, "description": "short description" }
# data = {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900, "description": "This is a laptop"}
# data = {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150, "description": "I am describing a Keyboard"}
# add_item_to_db(data)


def get_items_from_db():
    with engine.connect() as conn:
        query = text("SELECT * FROM items")
        results = conn.execute(query).fetchall()
        results_list = []
        for result in results:
            results_list.append(result._asdict())
        return results_list
