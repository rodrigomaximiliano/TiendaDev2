<template>
   <v-menu
        v-model="isMenuOpen"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        :style="menuPositionStyle"
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
          <v-list-item @click="navigateTo('/create-product')" class="dropdown-item">
            <v-list-item-title>Crear Producto</v-list-item-title>
          </v-list-item>
          <v-list-item @click="navigateTo('/mis-productos')" class="dropdown-item">
            <v-list-item-title>Mis Productos</v-list-item-title>
          </v-list-item>
          <v-list-item @click="navigateTo('/mi_cuenta')" class="dropdown-item">
            <v-list-item-title>Mi Cuenta</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
  </template>
  
  <script>
  export default {
  name: "DropMenu",
  computed: {
    username() {
      return localStorage.getItem("username") || null;
    },
    isAuthenticated() {
      return !!localStorage.getItem("token");
    },
    menuPositionStyle() {
      return {
        left: `${this.menuPosition.left}px`,
        top: `${this.menuPosition.top}px`
      };
    }
  },
  data() {
    return {
      isMenuOpen: false,
      menuPosition: {
        left: 0,
        top: 0
      },
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.$router.push("/login");
    },
    navigateTo(route) {
      this.isMenuOpen = false; // Cerrar menú
      this.$router.push(route);
    },
    openMenu(event) {
      const button = event.target.getBoundingClientRect();
      this.menuPosition.left = button.left;
      this.menuPosition.top = button.bottom;
      this.isMenuOpen = true;
    }
  },
};
</script>
  
  <style scoped>
  /* Estilos para el dropdown */
  .dropdown-menu {
    background-color: #32b8cf;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 0;
    margin-top: 8px;
  }
  .dropdown-item {
    transition: background-color 0.2s ease-in-out;
  }
  .dropdown-item:hover {
    background-color: rgba(93, 135, 212, 0.1);
  }
  </style>
  