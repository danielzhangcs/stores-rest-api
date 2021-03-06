from flask import Flask
import os
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
api = Api(app)

app.secret_key = "kun"
jwt = JWT(app, authenticate, identity)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://qieaeqmmxuzsyt:d229c389d2bf5b39f29ae012dc98fe52df228843ebc804cb7babf436ceaee584@ec2-34-194-171-47.compute-1.amazonaws.com:5432/depiqr97d8oeqj"

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000)
