<template>
  <div>
  <Navbar />
  <v-container fluid class="d-flex align-center justify-center" style="height: 100vh;">
    <v-card>
      <v-card-title class="headline text-center">Registrarse</v-card-title>
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

          <v-btn :disabled="!valid" @click="register" color="primary" class="mt-4" block>
            Registrarse
          </v-btn>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="goToLogin">¿Ya tienes una cuenta? Inicia sesión</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'Register',
  components: {
    Navbar 
  },
  setup() {
    const username = ref('');
    const password = ref('');
    const valid = ref(false);
    const router = useRouter();

    const register = async () => {
      try {
        await axios.post('http://localhost:8000/auth/register', {
          username: username.value,
          password: password.value,
        });
        router.push('/login');
      } catch (error) {
        console.error(error);
      }
    };

    const goToLogin = () => {
      router.push('/login');
    };

    return { username, password, valid, register, goToLogin };
  }
};
</script>

<style scoped>
.v-card {
  max-width: 400px;
  margin: auto;
}
</style>
