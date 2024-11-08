<template>
    <v-container>
      <h1>Mi Cuenta</h1>
      <v-form @submit.prevent="updateProfile">
        <v-text-field label="Usuario" v-model="username" disabled></v-text-field>
        <v-text-field label="Correo electrónico" v-model="email"></v-text-field>
        <v-btn type="submit">Actualizar Perfil</v-btn>
      </v-form>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        email: ''
      }
    },
    async created() {
      const response = await this.axios.get('/mi_cuenta')
      this.username = response.data.username
      this.email = response.data.email
    },
    methods: {
      async updateProfile() {
        try {
          await this.axios.put('/mi_cuenta', {
            email: this.email
          })
          alert('Perfil actualizado correctamente')
        } catch (error) {
          alert('Error al actualizar perfil')
        }
      }
    }
  }
  </script>
  