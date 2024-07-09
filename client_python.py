import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker with result code {rc}")
        client.subscribe("esp32") 
        print(f"Subscribed to topic 'esp32'")
    else:
        print(f"Failed to connect with result code {rc}")
def on_message(client, userdata, msg):
    print(f"Received message on topic '{msg.topic}': {msg.payload.decode()}")

mqtt_host = "localhost" 
mqtt_port = 1883  
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_host, mqtt_port, 60)

client.loop_forever()
