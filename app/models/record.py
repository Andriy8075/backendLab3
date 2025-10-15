from datetime import datetime

from ..pools import records

class Record:
    next_id = 1

    def __init__(self, user_id, category_id, sum):
        self.user_id = user_id
        self.category_id = category_id
        self.sum = sum
        self.id = Record.next_id
        self.date_time = datetime.now()
        Record.next_id += 1

    @staticmethod
    def create(user_id, category_id, sum):
        record = Record(user_id, category_id, sum)
        records.append(record)
        return record

    @staticmethod
    def get_by_id(id):
        for record in records:
            if record.id == id:
                return record.to_dict()
        return None

    @staticmethod
    def delete(id):
        for record in records:
            if record.id == id:
                records.remove(record)
                return record.to_dict()
        return None

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'category_id': self.category_id,
            'sum': self.sum,
            'date_time': self.date_time,
            'id': self.id
        }
