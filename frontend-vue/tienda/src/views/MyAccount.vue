<template>
  <v-container>
    <h1>Mi Cuenta</h1>
    <v-form @submit.prevent="updateProfile">
      <v-text-field label="Usuario" v-model="username" disabled></v-text-field>
     
      <v-btn type="submit">Actualizar Perfil</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import api from '../axios'; // Importa api aquí

export default {
  data() {
    return {
      username: '',
    };
  },
  async created() {
    try {
      const response = await api.get('/mi_cuenta'); // Usa api.get en lugar de this.$axios.get
      this.username = response.data.username;
      this.email = response.data.email;
    } catch (error) {
      console.error("Error al cargar los datos de la cuenta:", error);
      alert("No se pudieron cargar los datos de la cuenta.");
    }
  },
  methods: {
    async updateProfile() {
      try {
        await api.put('/mi_cuenta', { // Usa api.put en lugar de this.$axios.put
          email: this.email
        });
        alert('Perfil actualizado correctamente');
      } catch (error) {
        console.error("Error al actualizar el perfil:", error);
        alert('Error al actualizar perfil');
      }
    }
  }
};
</script>

<style scoped>
.v-container {
  max-width: 500px;
  margin: auto;
}
</style>
