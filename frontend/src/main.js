import { createApp } from 'vue'
import App from './App.vue'
import api from './services/api'

// Création de l'application Vue
const app = createApp(App)

// Enregistrement du service API au niveau global
app.config.globalProperties.$api = api

// Montage de l'application
app.mount('#app')
