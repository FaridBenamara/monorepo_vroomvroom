import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/ui', '@nuxtjs/tailwindcss'],

  // Configuration du proxy
  routeRules: {
    '/stats_every_5_seconds/**': { proxy: 'http://localhost:5000/stats_every_5_seconds' },
    '/get_stats_races/**': { proxy: 'http://localhost:5000/get_stats_races' }
  }
})
