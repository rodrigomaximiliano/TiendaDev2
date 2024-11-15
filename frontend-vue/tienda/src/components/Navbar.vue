<template>
  <v-app-bar app color="#5d87d4">
    <!-- Logo -->
    <v-img 
      src="/logo.svg" 
      alt="Logo" 
      max-width="150" 
      class="mr-6 d-flex align-center logo-transition" 
    ></v-img>

    <v-spacer></v-spacer>

    <!-- Botones de navegación -->
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
      <v-menu
        v-model="isMenuOpen"
        :close-on-content-click="false"
        :style="{ left: `${menuPosition.left}px`, top: `${menuPosition.top}px` }"
        transition="scale-transition"
        offset-y
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            text
            v-bind="attrs"
            v-on="on"
            @click="openMenu"
            class="ml-4 white--text button-hover user-button"
          >
            <v-icon left>mdi-account</v-icon> {{ username }}
            <v-icon right>mdi-chevron-down</v-icon>
          </v-btn>
        </template>

        <v-list class="dropdown-menu">
          <v-list-item @click="goToCreateProduct" class="dropdown-item">
            <v-list-item-title>Crear Producto</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToMyAccount" class="dropdown-item">
            <v-list-item-title>Mi Cuenta</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <!-- Botón para cerrar sesión -->
      <v-btn text @click="logout" class="ml-4 white--text button-hover">
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
  </v-app-bar>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      username: localStorage.getItem("username") || null,
      isMenuOpen: false,
      menuPosition: {
        
      
      },
    };
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem("token");
    },
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.username = null;
      this.$router.push("/login");
    },
    goToCreateProduct() {
      this.isMenuOpen = false; // Cerrar menú
      this.$router.push("/create-product");
    },
    goToMyAccount() {
      this.isMenuOpen = false; // Cerrar menú
      this.$router.push("/my-account");
    },
    openMenu(event) {
      // Captura la posición del botón en el que se hace clic
      const button = event.target.getBoundingClientRect();
      
      // Calcula la posición del menú con base en la posición del botón
      this.menuPosition.left = button.left;
      this.menuPosition.top = button.bottom;

      this.isMenuOpen = true;
    }
  },
};
</script>

<style scoped>
/* Estilos generales para los botones */
.button-hover {
  transition: background-color 0.3s;
}
.button-hover:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
}

/* Estilo para el botón de usuario */
.user-button {
  display: flex;
  align-items: center;
}

/* Estilos para el dropdown */
.dropdown-menu {
  background-color: #ffffff; /* Fondo más suave */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra suave */
  border-radius: 8px;
  padding: 0;
  margin-top: 8px;
}
.dropdown-item {
  transition: background-color 0.2s ease-in-out;
}
.dropdown-item:hover {
  background-color: rgba(93, 135, 212, 0.1); /* Color de hover más suave */
}

/* Estilos para el logo */
.logo-transition {
  transition: transform 0.3s;
}
.logo-transition:hover {
  transform: scale(1.05);
}
</style>
