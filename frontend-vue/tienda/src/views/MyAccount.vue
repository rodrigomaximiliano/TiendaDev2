<template>
  <v-app>
    <Navbar />
  <v-container>
    <h1>Mi Cuenta</h1>
    <!-- Formulario de perfil -->
    <v-form @submit.prevent="updateProfile" v-model="isFormValid">
      <v-text-field
        label="Usuario"
        v-model="username"
        disabled
        outlined
      ></v-text-field>

      <v-text-field
        label="Correo Electrónico"
        v-model="email"
        type="email"
        :rules="[emailRule]"
        outlined
      ></v-text-field>

      <v-btn 
        type="submit" 
        :disabled="!isFormValid" 
        color="primary"
      >
        Actualizar Perfil
      </v-btn>

      <v-divider class="my-4"></v-divider>

      <!-- Foto de perfil -->
      <v-img
        :src="profilePictureUrl"
        alt="Foto de perfil"
        class="my-4"
        max-width="150"
        max-height="150"
      ></v-img>

      <v-btn @click="openChangeProfilePictureDialog" color="secondary">
        Cambiar Foto de Perfil
      </v-btn>
    </v-form>
    
    <!-- Diálogo para cambiar la foto -->
    <v-dialog v-model="isChangeProfilePictureDialogOpen" max-width="400px">
      <v-card>
        <v-card-title class="headline">Cambiar Foto de Perfil</v-card-title>
        <v-card-text>
          <v-file-input
            label="Seleccionar imagen"
            v-model="newProfilePicture"
            accept="image/*"
            outlined
          ></v-file-input>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="isChangeProfilePictureDialogOpen = false" color="grey">Cancelar</v-btn>
          <v-btn @click="updateProfilePicture" color="primary">Actualizar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Cambiar contraseña -->
    <v-divider class="my-4"></v-divider>
    <v-form @submit.prevent="updatePassword">
      <v-text-field
        label="Nueva Contraseña"
        v-model="newPassword"
        type="password"
        outlined
      ></v-text-field>
      <v-btn type="submit" color="primary">Cambiar Contraseña</v-btn>
    </v-form>
  </v-container>
</v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
export default {
  components: {
    Navbar,
  },
  data() {
    return {
      username: '',
      email: '',
      profilePictureUrl: '',
      newProfilePicture: null,
      newPassword: '',
      isFormValid: false,
      isChangeProfilePictureDialogOpen: false,
      emailRule: [
        v => !!v || 'El correo electrónico es requerido',
        v => /.+@.+\..+/.test(v) || 'El correo electrónico debe ser válido',
      ],
    };
  },
  async created() {
    try {
      const response = await fetch('http://localhost:8000/mi_cuenta/mi_cuenta', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const data = await response.json();
      this.username = data.username;
      this.email = data.email;
      this.profilePictureUrl = data.profile_picture || '/static/uploads/default_profile.jpg'; // Imagen predeterminada
    } catch (error) {
      console.error("Error al cargar los datos de la cuenta:", error);
      alert("No se pudieron cargar los datos de la cuenta.");
    }
  },
  methods: {
    async updateProfile() {
      try {
        const response = await fetch('http://localhost:8000/mi_cuenta/mi_cuenta', {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email: this.email }),
        });

        if (response.ok) {
          alert('Perfil actualizado correctamente');
        } else {
          throw new Error('Error al actualizar el perfil');
        }
      } catch (error) {
        console.error("Error al actualizar el perfil:", error);
        alert('Error al actualizar perfil');
      }
    },
    openChangeProfilePictureDialog() {
      this.isChangeProfilePictureDialogOpen = true;
    },
    async updateProfilePicture() {
      const formData = new FormData();
      formData.append('file', this.newProfilePicture);
      
      try {
        const response = await fetch('http://localhost:8000/mi_cuenta/profile-picture', {
          method: 'PUT',
          headers: {
            'Accept': 'application/json',
          },
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          this.profilePictureUrl = data.profile_picture;
          this.isChangeProfilePictureDialogOpen = false;
          alert('Foto de perfil actualizada');
        } else {
          throw new Error('Error al actualizar la foto de perfil');
        }
      } catch (error) {
        console.error("Error al actualizar la foto de perfil:", error);
        alert('Error al actualizar la foto de perfil');
      }
    },
    async updatePassword() {
      try {
        const response = await fetch('http://localhost:8000/mi_cuenta/password', {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ new_password: this.newPassword }),
        });

        if (response.ok) {
          alert('Contraseña actualizada correctamente');
        } else {
          throw new Error('Error al cambiar la contraseña');
        }
      } catch (error) {
        console.error("Error al cambiar la contraseña:", error);
        alert('Error al cambiar la contraseña');
      }
    }
  },
};
</script>

<style scoped>
.v-container {
  max-width: 500px;
  margin: auto;
}

/* Estilo para los botones de acción */
.v-btn {
  margin-top: 16px;
}
</style>
