from flask import Blueprint, request, jsonify
from app.models import Vehicle, Race, SensorData, StatsRace
from app import db, mqtt_client
from app.mqtt_handler import MQTTHandler
from sqlalchemy import text
import time
routes = Blueprint('routes', __name__)

mqtt_handler = MQTTHandler(mqtt_client)

@routes.route('/vehicle', methods=['POST'])
def add_vehicle():
    data = request.json
    try:
        vehicle = Vehicle(name=data['name'])
        db.session.add(vehicle)
        db.session.commit()
        return jsonify({'message': 'Vehicle successfully added', 'data': vehicle.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@routes.route('/vehicle/<id>', methods=['GET'])
def get_vehicle_by_id(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify({'data': vehicle.to_dict()})
@routes.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    try:
        vehicles = Vehicle.query.all()
        return jsonify({'data': [vehicle.to_dict() for vehicle in vehicles]}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@routes.route('/vehicle/<id>', methods=['DELETE'])
def delete_vehicle_by_id(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle successfully deleted'})

@routes.route('/vehicle/<id>', methods=['PUT'])
def update_vehicle_by_id(id):
    data = request.json
    vehicle = Vehicle.query.get_or_404(id)
    vehicle.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Vehicle successfully updated', 'data': vehicle.to_dict()})

@routes.route('/race', methods=['POST'])
def add_race():
    data = request.json
    try:
        race = Race(vehicle_id=data['vehicle_id'], name=data['name'])
        db.session.add(race)
        db.session.commit()
        return jsonify({'message': 'Race successfully added', 'data': race.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@routes.route('/race/<id>', methods=['GET'])
def get_race_by_id(id):
    race = Race.query.get_or_404(id)
    return jsonify({'data': race.to_dict()})

@routes.route('/race/<id>', methods=['DELETE'])
def delete_race_by_id(id):
    race = Race.query.get_or_404(id)
    db.session.delete(race)
    db.session.commit()
    return jsonify({'message': 'Race successfully deleted'})

@routes.route('/race/<id>', methods=['PUT'])
def update_race_by_id(id):
    data = request.json
    race = Race.query.get_or_404(id)
    race.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Race successfully updated', 'data': race.to_dict()})

@routes.route('/sensor_data', methods=['POST'])
def add_sensor_data():
    data = request.json
    try:
        sensor_data = SensorData(
            race_id=data['race_id'],
            distance=data['distance'],
            speed=data['speed'],
            date=data['date'],
            battery=data['battery'],
            track=data['track']
        )
        db.session.add(sensor_data)
        db.session.commit()
        return jsonify({'message': 'Sensor data successfully added', 'data': sensor_data.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@routes.route('/sensor_data/<race_id>/speed', methods=['GET'])
def get_speed_last_ten_min(race_id):
    data = mqtt_handler.get_speed_last_ten_min(race_id)
    if data:
        return jsonify({'data': data}), 200
    else:
        return jsonify({'message': 'Error fetching speed'}), 500

@routes.route('/sensor_data/<race_id>/consumption', methods=['GET'])
def get_consumption_last_ten_min(race_id):
    data = mqtt_handler.get_consumption_last_ten_min(race_id)
    if data:
        return jsonify({'data': data}), 200
    else:
        return jsonify({'message': 'Error fetching consumption'}), 500

@routes.route('/stats_race', methods=['POST'])
def add_stats_race():
    data = request.json
    try:
        stats_race = StatsRace(
            race_id=data['race_id'],
            distance=data['distance'],
            speed_max=data['speed_max'],
            speed_average=data['speed_average'],
            battery_max=data['battery_max'],
            battery_min=data['battery_min'],
            time=data['time'],
            date=data['date']
        )
        db.session.add(stats_race)
        db.session.commit()
        return jsonify({'message': 'Stats race successfully added', 'data': stats_race.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@routes.route('/stats_race', methods=['GET'])
def get_stats_race_by_race_id():
    race_id = request.args.get('race_id')
    if not race_id:
        return jsonify({'message': 'race_id parameter is required'}), 400

    try:
        stats_race = StatsRace.query.filter_by(race_id=race_id).all()
        if not stats_race:
            return jsonify({'message': 'No statistics found for the given race_id'}), 404
        return jsonify({'data': [stat.to_dict() for stat in stats_race]}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@routes.route('/stats_race/<id>', methods=['DELETE'])
def delete_stats_race_by_id(id):
    stats_race = StatsRace.query.get_or_404(id)
    db.session.delete(stats_race)
    db.session.commit()
    return jsonify({'message': 'Stats race successfully deleted'})

@routes.route('/stats_race/<id>', methods=['PUT'])
def update_stats_race_by_id(id):
    data = request.json
    stats_race = StatsRace.query.get_or_404(id)
    stats_race.distance = data['distance']
    stats_race.speed_max = data['speed_max']
    stats_race.speed_average = data['speed_average']
    stats_race.battery_max = data['battery_max']
    stats_race.battery_min = data['battery_min']
    stats_race.time = data['time']
    stats_race.date = data['date']
    db.session.commit()
    return jsonify({'message': 'Stats race successfully updated', 'data': stats_race.to_dict()})
@routes.route('/get_broker_data', methods=['GET'])
def get_broker_data():
    # Topics à écouter
    topics_to_listen = ["esp32bis/speed", "esp32bis/timer"]

    # Variable pour stocker les données reçues
    broker_data = {}

    # Fonction de callback temporaire pour recevoir les messages
    def on_message(client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()
        broker_data[topic] = payload
        print(f"Received message: {payload} from topic: {topic}")

    # S'abonner aux topics et ajouter le callback temporaire
    for topic in topics_to_listen:
        mqtt_client.subscribe(topic)
        mqtt_client.message_callback_add(topic, on_message)

    # Attendre les données pendant un certain temps
    time.sleep(5)  # Ajustez ce délai selon vos besoins

    # Supprimer les callbacks pour ces topics après réception
    for topic in topics_to_listen:
        mqtt_client.message_callback_remove(topic)

    # Vérifier si des données ont été reçues
    if broker_data:
        return jsonify({'data': broker_data})
    else:
        return jsonify({'message': 'No data received from broker'}), 504
@routes.route('/get_stats_races', methods=['GET'])
def get_all_stats_race():
    # Requête SQL pour obtenir les statistiques
    query = text("""
        SELECT
            race_id AS sensor_data_race_id,
            COUNT(*) AS total_entries,
            AVG(distance) AS average_distance,
            AVG(speed) AS average_speed,
            MAX(distance) AS max_distance,
            MIN(distance) AS min_distance,
            AVG(battery) AS average_battery,
            MAX(battery) AS max_battery,
            MIN(date) AS start_time,
            MAX(date) AS end_time,
            MAX(date) - MIN(date) AS time_difference
        FROM sensor_data
        GROUP BY race_id
        ORDER BY race_id;
    """)

    with db.engine.connect() as connection:
        result = connection.execute(query).fetchall()

    # Convertir les résultats en liste de dictionnaires
    stats_race_list = [
        {
            'sensor_data_race_id': row[0],  # Utilisez l'index pour accéder aux valeurs
            'total_entries': row[1],
            'average_distance': row[2],
            'average_speed': row[3],
            'max_distance': row[4],
            'min_distance': row[5],
            'average_battery': row[6],
            'max_battery': row[7],
            'start_time': row[8],
            'end_time': row[9],
            'time_difference': row[10].total_seconds()
        }
        for row in result
    ]

    return jsonify(stats_race_list)
@routes.route('/stats_every_5_seconds', methods=['GET'])
def get_stats_every_5_seconds():
    # Requête SQL pour obtenir les statistiques toutes les 5 secondes par race_id
    query = text("""
        SELECT 
            id, 
            race_id, 
            distance, 
            speed, 
            date, 
            battery, 
            track
        FROM 
            sensor_data sd1
        WHERE 
            date IN (
                SELECT 
                    date 
                FROM 
                    sensor_data sd2
                WHERE 
                    sd1.race_id = sd2.race_id 
                    AND sd2.date >= sd1.date - INTERVAL '5 seconds' 
                    AND sd2.date < sd1.date + INTERVAL '5 seconds'
            )
        ORDER BY 
            race_id, 
            date;
    """)

    with db.engine.connect() as connection:
        result = connection.execute(query).fetchall()

    # Convertir les résultats en liste de dictionnaires
    stats_list = [
        {
            'id': row[0],
            'race_id': row[1],
            'distance': row[2],
            'speed': row[3],
            'date': row[4],
            'battery': row[5],
            'track': row[6]
        }
        for row in result
    ]

    return jsonify(stats_list)