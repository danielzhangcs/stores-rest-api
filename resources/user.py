from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("username",
                            type=str,
                            required=True,
                            help="this is required!")

        parser.add_argument("password",
                            type=str,
                            required=True,
                            help="this is required!")

        request_data = parser.parse_args()

        if UserModel.find_by_user_name(request_data["username"]):
            return {"message": "A user already exists"}, 400

        user = UserModel(**request_data)
        user.save_to_db()

        return {"message": "user created successfully"}, 201
