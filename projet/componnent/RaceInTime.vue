<template>
  <div class="race-container">
    <h2 class="title">Données de la Course</h2>
    <div class="data-display">
      <div class="data-item">
        <span class="label">Course ID:</span>
        <span class="value">{{ raceId }}</span>
      </div>
      <div class="data-item">
        <span class="label">Vitesse:</span>
        <span class="value">{{ speed }} km/h</span>
      </div>
      <div class="data-item">
        <span class="label">Distance:</span>
        <span class="value">{{ distance }} m</span>
      </div>
      <div class="data-item">
        <span class="label">Batterie:</span>
        <span class="value">{{ battery }} %</span>
      </div>
      <div class="data-item">
        <span class="label">Durée:</span>
        <span class="value">{{ duration }} s</span>
      </div>
      <div class="data-item">
        <span class="label">Date:</span>
        <span class="value">{{ date }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'RaceInTime',
  setup() {
    const raceId = ref<string>('');
    const speed = ref<string>('');
    const distance = ref<string>('');
    const battery = ref<string>('');
    const duration = ref<string>('');
    const date = ref<string>('');

    onMounted(() => {
      console.log('Tentative de connexion au WebSocket backend...');

      // Connexion au serveur WebSocket backend
      const ws = new WebSocket('ws://localhost:8082');

      ws.onopen = () => {
        console.log('Connexion WebSocket établie avec succès.');
      };

      ws.onmessage = (event) => {
        console.log('Message WebSocket brut reçu:', event.data);  // Log du message brut

        if (!event.data) {
          console.error('Le message WebSocket est vide ou non reçu.');
          return;
        }

        try {
          const data = JSON.parse(event.data);
          console.log('Message WebSocket JSON parsé:', data);

          switch (data.topic) {
            case 'esp32bis/race':
              raceId.value = data.message;
              break;
            case 'esp32bis/speed':
              speed.value = data.message;
              break;
            case 'esp32bis/distance':
              distance.value = data.message;
              break;
            case 'esp32bis/battery':
              battery.value = data.message;
              break;
            default:
              console.log('Topic non reconnu:', data.topic);
          }
        } catch (err) {
          console.error('Erreur lors du traitement du message WebSocket:', err);
        }
      };

      ws.onerror = (err) => {
        console.error('Erreur WebSocket:', err);
      };

      ws.onclose = () => {
        console.log('Connexion WebSocket fermée.');
      };
    });

    return {
      raceId,
      speed,
      distance,
      battery,
      duration,
      date,
    };
  },
});
</script>

<style scoped>
.race-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.title {
  text-align: center;
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.data-display {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.data-item {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #fff;
}

.label {
  font-weight: bold;
  color: #555;
}

.value {
  color: #333;
  text-align: right;
}
</style>
