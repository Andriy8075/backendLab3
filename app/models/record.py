from datetime import datetime
from app.extensions import db


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    sum = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    category = db.relationship('Category', back_populates='records')

    @staticmethod
    def create(category_id, sum, currency=None):
        # If no currency specified, get user's default currency through category
        if currency is None:
            from app.models.category import Category
            category = Category.query.get(category_id)
            currency = category.user.default_currency if category and category.user else 'USD'
        
        record = Record(category_id=category_id, sum=sum, currency=currency)
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
            'category_id': self.category_id,
            'sum': self.sum,
            'currency': self.currency,
            'date_time': self.date_time,
            'id': self.id
        }
