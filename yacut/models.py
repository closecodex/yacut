import datetime

from yacut import db

MAX_URL_LENGTH = 2048
MAX_SHORT_ID_LENGTH = 16


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL_LENGTH), nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_ID_LENGTH), unique=True, nullable=False
    )
    timestamp = db.Column(
        db.DateTime, index=True, default=datetime.datetime.utcnow
    )

    def to_dict(self):
        return {
            'id': self.id,
            'original': self.original,
            'short': self.short,
            'timestamp': self.timestamp
        }
