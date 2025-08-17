from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv
from database import get_items_from_db

load_dotenv()
db_connection_string = os.getenv("DB_CONNECTION_STRING")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")



@app.route("/market")
def market_page():
    items = get_items_from_db()
    print(items)
    return render_template("market.html", items = items)