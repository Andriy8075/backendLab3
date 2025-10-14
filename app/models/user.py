from ..pools import users

class User:
    next_id = 1

    def __init__(self, name):
        self.name = name
        self.id = User.next_id
        User.next_id += 1

    @staticmethod
    def create(name):
        user = User(name)
        users.append(user)
        return user

    @staticmethod
    def get_all():
        return users

    @staticmethod
    def get_by_id(id):
        for user in users:
            if user.id == id:
                return user.to_dict()
        return None

    @staticmethod
    def delete(id):
        for i, user in enumerate(users):
            if user.id == id:
                users.pop(i)
                return True
        return False

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
