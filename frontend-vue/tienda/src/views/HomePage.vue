<template>
  <v-app>
    <Navbar />
    <v-main>
      <v-container fluid class="main-container">
        <Carrusel />
        <v-container>
          <h1>Bienvenido a Tienda Devlights</h1>
          <p>Encuentra productos de calidad a precios competitivos.</p>
        </v-container>
      </v-container>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Carrusel from '@/components/Carrusel.vue'; 
import Footer from '@/components/Footer.vue';

export default {
  name: "HomePage",
  components: {
    Navbar,
    Carrusel,
    Footer,
  },
};
</script>

<style scoped>
.main-container {
  padding: 0;
}
</style>
