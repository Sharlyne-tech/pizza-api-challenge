from server.app import db
from sqlalchemy_serializer import SerializerMixin

class Restaurant(db.Model):
class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules=("-restaurant_pizzas.restaurant",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
