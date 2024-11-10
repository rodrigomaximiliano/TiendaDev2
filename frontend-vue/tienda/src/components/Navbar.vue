<template>
  <v-app-bar app color="#5d87d4">
    <v-img 
      src="/logo.svg" 
      alt="Logo" 
      max-width="150" 
      class="mr-4 d-flex align-center logo-transition"
    ></v-img>

    <v-text-field
      v-model="searchQuery"
      append-icon="mdi-magnify"
      label="Buscar productos"
      class="search-bar"
      hide-details
      solo
      clearable
      :style="{ maxWidth: '350px' }"
      outlined
      dense
      :rules="[value => value.length >= 3 || 'Ingrese al menos 3 caracteres']"
    ></v-text-field>

    <v-spacer></v-spacer>

    <v-btn text to="/" class="ml-4 white--text button-hover">
      <v-icon left>mdi-home</v-icon> Inicio
    </v-btn>

    <v-btn text to="/store/products" class="ml-4 white--text button-hover">
      <v-icon left>mdi-cart</v-icon> Ver productos
    </v-btn>

    <template v-if="isAuthenticated">
      <v-btn text to="/cart" class="ml-4 white--text button-hover">
        <v-icon left>mdi-cart</v-icon> Carrito
      </v-btn>

      <v-btn text class="ml-4 white--text button-hover">
        <v-icon left>mdi-account</v-icon> {{ username }}
      </v-btn>

      <v-btn text @click="logout" class="ml-4 white--text button-hover">
        <v-icon left>mdi-logout</v-icon> Cerrar sesión
      </v-btn>
    </template>

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
      searchQuery: "",
      username: localStorage.getItem("username") || null,
    };
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem("token");
    },
  },
  watch: {
    isAuthenticated(newVal) {
      if (newVal) {
        this.username = localStorage.getItem("username");
      } else {
        this.username = null;
      }
    }
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.username = null;
      this.$router.push("/login");
    },
  },
};
</script>