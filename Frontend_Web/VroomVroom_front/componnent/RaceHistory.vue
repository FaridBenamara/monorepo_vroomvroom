<template>
    <div class="charts-container">
      <div v-for="(data, raceId) in raceData" :key="raceId" class="chart-container">
        <h2 class="chart-title">Race ID: {{ raceId }}</h2>
        <canvas :id="'chart-' + raceId"></canvas>
        <div v-if="stats[raceId]" class="stats-container">
          <p><strong>Vitesse Moyenne:</strong> {{ stats[raceId].average_speed.toFixed(2) }} Cm/h</p>
          <p><strong>Distance:</strong> {{ stats[raceId].max_distance.toFixed(2) }} Cm</p>
          <p><strong>Moyenne Battery:</strong> {{ stats[raceId].average_battery.toFixed(2) }} volts</p>
          <p><strong>Durée:</strong> {{ stats[raceId].time_difference.toFixed(2) }} seconds</p>
        </div>
      </div>
    </div>
  </template>
  <script>
  import { onMounted, ref, nextTick } from 'vue'
  import { Chart, registerables } from 'chart.js'
  
  Chart.register(...registerables)
  
  export default {
    setup() {
      const raceData = ref({})
      const stats = ref({})
  
      const fetchData = async () => {
        try {
          const [dataResponse, statsResponse] = await Promise.all([
            fetch('/stats_every_5_seconds'), // route api
            fetch('/get_stats_races') // route api
          ])
  
          const data = await dataResponse.json()
          const statsData = await statsResponse.json()
  
          // Transform the data to group by race_id
          const groupedData = data.reduce((acc, item) => {
            if (!acc[item.race_id]) {
              acc[item.race_id] = { labels: [], data: [] }
            }
            acc[item.race_id].labels.push(new Date(item.date).toLocaleTimeString())
            acc[item.race_id].data.push(item.speed)
            return acc
          }, {})
  
          // Store the statistics by race_id
          const statsByRaceId = statsData.reduce((acc, item) => {
            acc[item.sensor_data_race_id] = item
            return acc
          }, {})
  
          raceData.value = groupedData
          stats.value = statsByRaceId
  
          // Ensure DOM is updated before rendering charts
          await nextTick()
          renderCharts()
        } catch (error) {
          console.error('Error fetching data:', error)
        }
      }
  
      const renderCharts = () => {
        Object.keys(raceData.value).forEach(raceId => {
          const ctx = document.getElementById('chart-' + raceId).getContext('2d')
          new Chart(ctx, {
            type: 'line',
            data: {
              labels: raceData.value[raceId].labels,
              datasets: [{
                label: `Speed for Race ${raceId}`,
                data: raceData.value[raceId].data,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
              }]
            },
            options: {
              responsive: true,
              scales: {
                x: {
                  title: {
                    display: true,
                    text: 'Time'
                  },
                  ticks: {
                    autoSkip: true,
                    maxTicksLimit: 20
                  }
                },
                y: {
                  title: {
                    display: true,
                    text: 'Speed'
                  },
                  suggestedMin: 0
                }
              }
            }
          })
        })
      }
  
      onMounted(fetchData)
  
      return { raceData, stats }
    }
  }
  </script>
  <style scoped>
  .charts-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    padding: 20px;
  }
  
  .chart-container {
    width: 400px;
    height: 250px;
    margin: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .chart-title {
    text-align: center;
    margin: 0;
    padding: 10px;
    font-size: 16px;
    color: #333;
    background-color: #f9f9f9;
    border-bottom: 1px solid #ddd;
    width: 100%;
  }
  
  canvas {
    width: 100% !important;
    height: auto !important;
  }
  
  .stats-container {
    margin-top: 10px;
    padding: 10px;
    text-align: left;
    font-size: 14px;
    color: #333;
    background-color: #f9f9f9;
    border-top: 1px solid #ddd;
    width: 100%;
  }
  </style>