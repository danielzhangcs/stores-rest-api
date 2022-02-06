from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.store import StoreModel


class Store(Resource):
    def __init__(self):
        pass

    def get(self, name):
        store = StoreModel.get_by_name(name)
        if store:
            return store.json()
        return {"message": "store not found"}, 404


    def post(self, name):

        if StoreModel.get_by_name(name):
            return {"message": f"{name} already exist"}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except Exception as e:
            return {"message": f"inser failed with error {str(e)}"}, 500

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.get_by_name(name)
        if store is None:
            return {"message": f"An item with name {name} not exists"}, 400

        store.delete_from_db()

        return {"message": "store deleted"}


class StoreList(Resource):

    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}