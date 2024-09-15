x<template>
    <div>
      <RaceHistory/>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue'
  import RaceHistory from '@/componnent/RaceHistory.vue';
  
  export default defineComponent({
    components: {
      RaceHistory
    }
  })
  </script>
  