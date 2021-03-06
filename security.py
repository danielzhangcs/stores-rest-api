from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_user_name(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_user_id(user_id)
