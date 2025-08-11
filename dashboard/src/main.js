import { createApp } from 'vue'
import SimpleApp from './SimpleApp.vue'
import './style.css'

// Create Vue app
const app = createApp(SimpleApp)

// Mount the app
app.mount('#app')