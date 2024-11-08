<template>
  <v-container>

    <Navbar />
    <v-main>
      <v-container>
        <h1>Bienvenido a Tienda Devlights</h1>
        <p>Encuentra productos de calidad a precios competitivos.</p>
      </v-container>
    </v-main>

    <v-footer color="#8e24aa" app dark>
      <v-col class="text-center white--text">&copy; 2024 Tienda Devlights</v-col>
    </v-footer>
  </v-container>
</template>

<script>

import Navbar from '@/components/Navbar.vue';

export default {
  name: "HomePage",
  components: {
    Navbar, 
  },
};
</script>

<style scoped>
.v-main {
  padding-top: 20px;
}
</style>
