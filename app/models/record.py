from datetime import datetime
from app.extensions import db


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    sum = db.Column(db.Float, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', back_populates='records')
    category = db.relationship('Category', back_populates='records')

    @staticmethod
    def create(user_id, category_id, sum):
        record = Record(user_id=user_id, category_id=category_id, sum=sum)
        db.session.add(record)
        db.session.commit()
        return record

    @staticmethod
    def get_by_id(id):
        record = Record.query.get(id)
        if record is None:
            return None
        return record.to_dict()

    @staticmethod
    def delete(id):
        record = Record.query.get(id)
        if record is None:
            return None
        record_dict = record.to_dict()
        db.session.delete(record)
        db.session.commit()
        return record_dict

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'category_id': self.category_id,
            'sum': self.sum,
            'date_time': self.date_time,
            'id': self.id
        }
