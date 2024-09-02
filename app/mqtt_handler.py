from app import db
from app.models import SensorData
from uuid import UUID
import datetime

class MQTTHandler:
    def __init__(self, client):
        self.client = client
        self.sensor_data_map = {}

    def message_callback(self, message, topic):
        print(f"Processing message: {message} from topic: {topic}")

        race_id = self.sensor_data_map.get("race", {}).get("race_id", None)

        if not race_id and topic != "esp32/race":
            print("RaceID not set yet, waiting for RaceID")
            return

        try:
            if topic == "esp32/race":
                self.sensor_data_map["race"] = {"race_id": UUID(message)}
            elif topic in ["esp32/speed", "esp32/distance", "esp32/battery", "esp32/track"]:
                value = float(message)
                if topic == "esp32/speed":
                    self.sensor_data_map["race"]["speed"] = value
                elif topic == "esp32/distance":
                    self.sensor_data_map["race"]["distance"] = round(value)
                elif topic == "esp32/battery":
                    self.sensor_data_map["race"]["battery"] = round(value)
                elif topic == "esp32/track":
                    self.sensor_data_map["race"]["track"] = round(value)

            if all(key in self.sensor_data_map.get("race", {}) for key in ["race_id", "speed", "distance", "battery"]):
                sensor_data = SensorData(
                    race_id=self.sensor_data_map["race"]["race_id"],
                    distance=self.sensor_data_map["race"]["distance"],
                    speed=self.sensor_data_map["race"]["speed"],
                    date=datetime.datetime.utcnow(),
                    battery=self.sensor_data_map["race"]["battery"],
                    track=self.sensor_data_map["race"].get("track", 0)
                )
                db.session.add(sensor_data)
                db.session.commit()
                print(f"Sensor data added successfully: {sensor_data}")
                self.sensor_data_map = {}

        except Exception as e:
            print(f"Error processing message: {e}")

    def get_sensor_data_by_id(self, race_id):
        return SensorData.query.filter_by(race_id=race_id).all()

    def get_speed_last_ten_min(self, race_id):
        # Implement the SQLAlchemy query for speed in the last ten minutes
        pass

    def get_consumption_last_ten_min(self, race_id):
        # Implement the SQLAlchemy query for consumption in the last ten minutes
        pass
