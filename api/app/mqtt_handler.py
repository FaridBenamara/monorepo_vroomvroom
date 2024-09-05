from app.models import SensorData, Race
from app import db, app
import datetime

sensor_data_map = {}  # Initialiser sans course active

class MQTTHandler:
    def __init__(self, client):
        self.client = client

    def message_callback(self, message, topic):
        with app.app_context():
            print(f"Processing message: {message} from topic: {topic}")
            global sensor_data_map

            if topic == "esp32bis/race":
                if message.lower() == "false":
                    # Désactiver la course si le message est "false"
                    sensor_data_map = {}  # Réinitialiser le map pour désactiver la course
                    print("Race deactivated, ignoring subsequent messages")
                    return
                else:
                    # Activer la course si un identifiant est reçu
                    race_id = int(float(message))  # Enlever le ".00" et convertir en entier
                    sensor_data_map["race"] = {"race_id": race_id}
                    print(f"Race activated with ID: {race_id}")
                    return

            # Si la course est inactive (sensor_data_map["race"] n'existe pas), ne rien faire
            if "race" not in sensor_data_map:
                print("No active race, ignoring message")
                return

            race_id = sensor_data_map["race"].get("race_id", None)
            if not race_id:
                print("RaceID not set yet, waiting for RaceID")
                return

            try:
                if topic in ["esp32bis/speed", "esp32bis/distance", "esp32bis/battery", "esp32bis/track"]:
                    value = float(message)
                    if topic == "esp32bis/speed":
                        sensor_data_map["race"]["speed"] = value
                    elif topic == "esp32bis/distance":
                        sensor_data_map["race"]["distance"] = round(value, 2)
                    elif topic == "esp32bis/battery":
                        sensor_data_map["race"]["battery"] = round(value, 2)
                    elif topic == "esp32bis/track":
                        sensor_data_map["race"]["track"] = int(value)

                # Si toutes les données sont disponibles, enregistrer les données du capteur
                if all(key in sensor_data_map["race"] for key in ["race_id", "speed", "distance", "battery"]):
                    sensor_data = SensorData(
                        race_id=sensor_data_map["race"]["race_id"],
                        distance=sensor_data_map["race"]["distance"],
                        speed=sensor_data_map["race"]["speed"],
                        date=datetime.datetime.now(),
                        battery=sensor_data_map["race"]["battery"],
                        track=sensor_data_map["race"].get("track", 0)
                    )
                    db.session.add(sensor_data)
                    db.session.commit()
                    print(f"Sensor data added successfully: {sensor_data}")
                    # Réinitialiser le map pour la prochaine collecte
                    sensor_data_map = {}

            except Exception as e:
                print(f"Error processing message: {e}")

    def get_sensor_data_by_id(self, race_id):
        return SensorData.query.filter_by(race_id=race_id).all()

    def get_speed_last_ten_min(self, race_id):
        pass

    def get_consumption_last_ten_min(self, race_id):
        pass
