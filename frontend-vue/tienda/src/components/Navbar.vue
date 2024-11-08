<template>
    <v-app-bar app color="#8e24aa" dark>
      <v-toolbar-title>Tienda Devlights</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/login">Iniciar sesión</v-btn>
      <v-btn text to="/register">Registrarse</v-btn>
      <v-btn icon to="/cart">
        <v-icon>mdi-cart</v-icon>
      </v-btn>
    </v-app-bar>
  </template>
  
  <script>
  export default {
    name: "Navbar",
  };
  </script>
  
  <style scoped>
  
  </style>
  