from app import db
import datetime

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'vehicle_id': self.vehicle_id, 'name': self.name}

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    speed = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    battery = db.Column(db.Float, nullable=False)
    track = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'race_id': self.race_id,
            'distance': self.distance,
            'speed': self.speed,
            'date': self.date.isoformat(),
            'battery': self.battery,
            'track': self.track
        }

class StatsRace(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    speed_max = db.Column(db.Float, nullable=False)
    speed_average = db.Column(db.Float, nullable=False)
    battery_max = db.Column(db.Integer, nullable=False)
    battery_min = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'race_id': self.race_id,
            'distance': self.distance,
            'speed_max': self.speed_max,
            'speed_average': self.speed_average,
            'battery_max': self.battery_max,
            'battery_min': self.battery_min,
            'time': self.time,
            'date': self.date.isoformat()
        }
