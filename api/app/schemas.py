from marshmallow import Schema, fields

class VehicleSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class RaceSchema(Schema):
    id = fields.Int()
    vehicle_id = fields.Int()
    name = fields.Str()
    date = fields.DateTime()

class SensorDataSchema(Schema):
    id = fields.Int()
    race_id = fields.Int()
    distance = fields.Float()
    speed = fields.Float()
    date = fields.DateTime()
    battery = fields.Float()
    track = fields.Int()

class StatsRaceSchema(Schema):
    id = fields.Int()
    race_id = fields.Int()
    distance = fields.Float()
    speed_max = fields.Float()
    speed_average = fields.Float()
    battery_max = fields.Int()
    battery_min = fields.Int()
    time = fields.Int()
    date = fields.DateTime()
