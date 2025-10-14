from ..pools import categories

class Category:
    next_id = 1

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.id = Category.next_id
        Category.next_id += 1

    @staticmethod
    def create(name, user_id):
        category = Category(name, user_id)
        categories.append(category)
        return category

    @staticmethod
    def get_all():
        return categories

    @staticmethod
    def delete(id):
        for i, user in enumerate(categories):
            if user.id == id:
                categories.pop(i)
                return True
        return False

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
        }
