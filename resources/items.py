from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class Item(Resource):
    def __init__(self):
        pass

    def get(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            return item.json()
        return {"message": "item not found"}, 404


    def post(self, name):

        if ItemModel.get_by_name(name):
            return {"message": f"{name} already exist"}, 400

        parser = reqparse.RequestParser()
        parser.add_argument("price",
                            type=float,
                            required=True,
                            help="this is required!")

        parser.add_argument("store_id",
                            type=int,
                            required=True,
                            help="this is required!")
        request_data = parser.parse_args()

        item = ItemModel(name, **request_data)

        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"inser failed with error {str(e)}"}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.get_by_name(name)
        if item is None:
            return {"message": f"An item with name {name} not exists"}, 400

        item.delete_from_db()

        return {"message": "item deleted"}

    def put(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument("price",
                            type=float,
                            required=True,
                            help="this is required!")
        request_data = parser.parse_args()

        item = ItemModel.get_by_name(name)
        if item:
            item.price = request_data["price"]
        else:
            item = ItemModel(name, **request_data)

        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"Error with {str(e)}"}

        return item.json()


class ItemList(Resource):

    def get(self):

        return {"items": [item.json() for item in ItemModel.query.all()]}
