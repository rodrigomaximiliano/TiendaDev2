<template>
  <div>
    <v-app-bar app :style="{ background: 'linear-gradient(135deg, #5d87d4 0%, #00c6ff 100%)' }">
      <!-- Logo -->
      <v-img 
        src="/logo.svg" 
        alt="Logo" 
        max-width="150" 
        class="mr-6 ml-4 d-flex align-center logo-transition" 
      ></v-img>

      <v-spacer></v-spacer>

      <!-- Botones de navegación (ocultos en pantallas pequeñas) -->
      <div class="d-none d-md-flex">
        <v-btn text to="/" class="ml-4 white--text button-hover">
          <v-icon left>mdi-home</v-icon> Inicio
        </v-btn>

        <v-btn text to="/store/products" class="ml-4 white--text button-hover">
          <v-icon left>mdi-cart</v-icon> Productos
        </v-btn>

        <!-- Opciones para usuario autenticado -->
        <template v-if="isAuthenticated">
          <!-- Botón de carrito -->
          <v-btn text to="/cart" class="ml-4 white--text button-hover">
            <v-icon left>mdi-cart</v-icon> Carrito
          </v-btn>

          <!-- Menú desplegable de usuario -->
          <DropMenu :username="username" />

          <!-- Botón para cerrar sesión -->
          <v-btn text @click="logoutAndCloseDrawer" class="ml-4 white--text button-hover">
            <v-icon left>mdi-logout</v-icon> Cerrar sesión
          </v-btn>
        </template>

        <!-- Botones de autenticación -->
        <template v-else>
          <v-btn text to="/register" class="ml-4 white--text button-hover">
            <v-icon left>mdi-account-plus</v-icon> Registrarse
          </v-btn>
          <v-btn text to="/login" class="ml-4 white--text button-hover">
            <v-icon left>mdi-login</v-icon> Iniciar sesión
          </v-btn>
        </template>
      </div>

      <!-- Icono de menú en dispositivos pequeños -->
      <v-app-bar-nav-icon @click="drawer = !drawer" class="d-md-none"></v-app-bar-nav-icon>
    </v-app-bar>

    <!-- Drawer para móviles -->
    <v-navigation-drawer v-model="drawer" temporary class="custom-drawer">
      <v-list>
        <v-list-item to="/" @click="drawer = false">
          <v-list-item-title>Inicio</v-list-item-title>
        </v-list-item>
        <v-list-item to="/store/products" @click="drawer = false">
          <v-list-item-title>Productos</v-list-item-title>
        </v-list-item>
        <template v-if="isAuthenticated">
          <v-list-item to="/cart" @click="drawer = false">
            <v-list-item-title>Carrito</v-list-item-title>
          </v-list-item>
          <v-list-item to="/create-product" @click="drawer = false">
            <v-list-item-title>Crear Producto</v-list-item-title>
          </v-list-item>
          <v-list-item to="/mis-productos" @click="drawer = false">
            <v-list-item-title>Mis Productos</v-list-item-title>
          </v-list-item>
          <v-list-item to="/mi_cuenta" @click="drawer = false">
            <v-list-item-title>Mi Cuenta</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logoutAndCloseDrawer">
            <v-list-item-title>Cerrar sesión</v-list-item-title>
          </v-list-item>
        </template>
        <template v-else>
          <v-list-item to="/register" @click="drawer = false">
            <v-list-item-title>Registrarse</v-list-item-title>
          </v-list-item>
          <v-list-item to="/login" @click="drawer = false">
            <v-list-item-title>Iniciar sesión</v-list-item-title>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import DropMenu from "@/components/DropMenu.vue";

export default {
  name: "Navbar",
  components: {
    DropMenu,
  },
  computed: {
    username() {
      return localStorage.getItem("username") || null;
    },
    isAuthenticated() {
      return !!localStorage.getItem("token");
    },
  },
  data() {
    return {
      drawer: false, // Para gestionar el estado del drawer
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.$router.push("/login");
    },
    logoutAndCloseDrawer() {
      this.logout();  // Llama a logout
      this.drawer = false;  // Cierra el drawer
    },
  },
};
</script>

<style scoped>
/* Estilos generales para los botones */
.button-hover {
  transition: background-color 0.3s, box-shadow 0.3s;
}
.button-hover:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Estilo para el botón de usuario */
.user-button {
  display: flex;
  align-items: center;
}

/* Estilos para el logo */
.logo-transition {
  transition: transform 0.3s;
}
.logo-transition:hover {
  transform: scale(1.05);
}

/* Estilos para el drawer */
.custom-drawer {
  background: linear-gradient(135deg, #dee4f0 0%, #00c6ff 100%);
  border-radius: 10px 0 0 10px;
  padding-top: 20px;
}

.v-list-item {
  transition: background-color 0.3s;
}

.v-list-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}

.v-list-item-title {
  font-size: 16px;
  font-weight: 500;
}
</style>
