<template>
  <v-container>
    <Navbar />
    <v-row justify="center" class="mt-10">
      <v-col cols="12" md="8">
        <v-card class="pa-5 elevation-4">
        
          <v-row align="center" justify="center">
            <v-col cols="12" md="4" class="text-center">
              <v-avatar size="150"> <!-- Tamaño aumentado aquí -->
                <img
                  :src="getPhotoUrl(user.photo_url)"
                  alt="Foto de Perfil"
                  class="avatar-img"
                />
              </v-avatar>
              <h3 class="font-weight-bold mt-3">{{ user.username }}</h3>
              <p class="text-subtitle-2 grey--text">{{ user.email }}</p>
            </v-col>
            <v-col cols="12" md="8">
              <v-list dense>
                <v-list-item>
                  <v-list-item-title class="font-weight-bold">Nombre Completo:</v-list-item-title>
                  <v-list-item-subtitle>{{ user.full_name }}</v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-col>
          </v-row>

          <v-divider class="mt-4 mb-4" />
          <v-row justify="center" align="center">
            <v-col cols="12" md="4">
              <v-btn color="primary" block large @click="goToEditProfile">
                Editar Perfil
              </v-btn>
            </v-col>
            <v-col cols="12" md="4">
              <v-btn color="secondary" block large @click="changePassword">
                Cambiar Contraseña
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>

    <!-- Snackbar -->
    <v-snackbar v-model="snackbar.show" :color="snackbar.color" timeout="3000">
      {{ snackbar.message }}
    </v-snackbar>
  </v-container>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

export default {
  components: { Navbar },
  data() {
    return {
      user: {
        username: "",
        full_name: "",
        email: "",
        photo_url: "",
      },
      snackbar: {
        show: false,
        message: "",
        color: "success",
      },
    };
  },
  created() {
    this.fetchUserProfile();
  },
  methods: {
    getPhotoUrl(photo_url) {
      const backendUrl = "http://localhost:8000";
      return photo_url
        ? `${backendUrl}${photo_url}`
        : "/static/images/default-avatar.png";
    },
    async fetchUserProfile() {
      try {
        const username = localStorage.getItem("username");
        if (!username) {
          this.showSnackbar("No se pudo obtener el nombre de usuario", "error");
          return;
        }
        const response = await axios.get(
          `http://localhost:8000/mi_cuenta/mi_cuenta?username=${username}`
        );
        this.user = response.data;
      } catch (error) {
        console.error("Error al cargar el perfil:", error);
        this.showSnackbar("No se pudo cargar el perfil", "error");
      }
    },
    showSnackbar(message, color) {
      this.snackbar.message = message;
      this.snackbar.color = color;
      this.snackbar.show = true;
    },
    goToEditProfile() {
      this.$router.push({ name: "EditProfile" });
    },
    changePassword() {
      this.$router.push({ name: "ChangePassword" });
    },
  },
};
</script>

<style scoped>
.mt-10 {
  margin-top: 40px;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.v-card {
  border-radius: 16px;
}

h3 {
  font-size: 1.5rem;
  margin: 0;
}

.v-btn {
  font-weight: bold;
}
</style>
