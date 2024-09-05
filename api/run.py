from app import create_app
from flask_cors import CORS  # Importer CORS
import os

app = create_app()

# Configurer CORS
CORS(app, resources={r"/*": {"origins": "*"}})  # Permet toutes les origines. Ajustez selon vos besoins.

if __name__ == '__main__':
    # Subscribe to MQTT topics
    from app import mqtt_client
    from app.mqtt_broker import subscribe_to_topic

    subscribe_to_topic(mqtt_client, "esp32bis/#")  # Subscribe to all topics under "esp32Bis"
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
