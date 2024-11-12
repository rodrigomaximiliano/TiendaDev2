import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';
import 'vuetify/dist/vuetify.min.css';
import axios from './axios';
import '@mdi/font/css/materialdesignicons.css';
import { createPinia } from 'pinia'; 




const app = createApp(App);

const pinia = createPinia();
app.use(pinia);
app.use(vuetify);
app.use(router);
app.mount('#app');
app.config.globalProperties.$axios = axios;