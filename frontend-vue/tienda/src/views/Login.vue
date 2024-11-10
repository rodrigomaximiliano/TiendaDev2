<template>
  <div>
    <Navbar />
    <v-container fluid class="d-flex align-center justify-center" style="height: 100vh;">
      <v-card>
        <v-card-title class="headline text-center">Iniciar Sesión</v-card-title>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="username"
              label="Usuario"
              :rules="[v => !!v || 'Usuario es requerido']"
              required
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Contraseña"
              type="password"
              :rules="[v => !!v || 'Contraseña es requerida']"
              required
            ></v-text-field>
            <v-btn :disabled="!valid" @click="login" color="primary" class="mt-4" block>
              Iniciar Sesión
            </v-btn>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="goToRegister">¿No tienes una cuenta? Regístrate</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import Navbar from '@/components/Navbar.vue';  // Asegúrate de usar la ruta correcta

export default {
  name: 'Login',
  components: {
    Navbar 
  },
  setup() {
    const username = ref('');
    const password = ref('');
    const valid = ref(false);
    const router = useRouter();

    const login = async () => {
      try {
        const response = await axios.post('http://localhost:8000/auth/login', {
          username: username.value,
          password: password.value,
        });

        localStorage.setItem("token", response.data.access_token);
        localStorage.setItem("username", response.data.username);  // Guardamos el nombre de usuario
        
        router.push('/');
      } catch (error) {
        console.error(error);
      }
    };

    const goToRegister = () => {
      router.push('/register');
    };

    return { username, password, valid, login, goToRegister };
  }
};
</script>
