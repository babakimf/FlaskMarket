
from market import db

class Item(db.Model):
    __tablename__ = 'items' 
    id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    barcode = db.Column(db.String(length = 16), nullable = False, unique = True)
    price = db.Column(db.Integer())
    description = db.Column(db.String(1024), nullable = False, unique = False)