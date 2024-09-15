import WebSocket from 'ws';
import mqtt from 'mqtt';

// Configuration du broker MQTT
const MQTT_BROKER = 'mqtt://13.60.74.162:1883';
const MQTT_TOPICS = ['esp32/race', 'esp32/speed', 'esp32/distance', 'esp32/battery'];

// Création du client MQTT
const mqttClient = mqtt.connect(MQTT_BROKER, {
  username: 'guest',
  password: 'guest',
});

// Création du serveur WebSocket
const wss = new WebSocket.Server({ port: 8082 });

mqttClient.on('connect', () => {
  console.log('Connecté au broker MQTT');
  MQTT_TOPICS.forEach(topic => {
    mqttClient.subscribe(topic, (err) => {
      if (err) {
        console.error(`Erreur de souscription au topic ${topic}:`, err);
      } else {
        console.log(`Souscription réussie au topic ${topic}`);
      }
    });
  });
});

mqttClient.on('message', (topic, message) => {
  const data = {
    topic,
    message: message.toString(),
  };
  console.log('Message MQTT reçu:', data);

  // Transmettre le message reçu aux clients WebSocket
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(data));
      console.log('Message envoyé au client WebSocket:', data);
    }
  });
});

wss.on('connection', (ws) => {
  console.log('Client connecté via WebSocket');

  ws.on('close', () => {
    console.log('Client déconnecté du WebSocket');
  });
});

console.log('Serveur WebSocket en écoute sur le port 8082');
