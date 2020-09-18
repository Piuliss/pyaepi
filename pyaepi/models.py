"""
models.py
- Data classes for the surveyapi application
"""
import enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SpeedUnit(enum.Enum):
    mbps = 1


class ConnSpeedTest(db.Model):
    __tablename__ = 'conn_speed_tests'

    id = db.Column(db.Integer, primary_key=True)
    upload = db.Column(db.Float(precision='10,2'), nullable=False)
    download = db.Column(db.Float(precision='10,2'), nullable=False)
    ping = db.Column(db.Float(precision='10,2'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    speed_unit = db.Column(db.Enum(SpeedUnit),
                           default=SpeedUnit.mbps,
                           nullable=False)

    def to_dict(self):
        return dict(id=self.id,
                    upload=self.upload,
                    download=self.download,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    speed_unit=self.speed_unit.value)
