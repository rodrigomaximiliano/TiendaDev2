<template>
  <v-app>
    <Navbar />
    <v-main>
      <!-- Carrusel (con padding ajustado) -->
      <v-container fluid class="pa-0">
        <Carrusel />
      </v-container>

      <!-- Banner con padding reducido -->
      <v-container fluid class="mt-0 pa-0">
        <Banner />
      </v-container>

      <!-- Productos Cards (con espacio controlado) -->
      <v-container fluid class="my-2">
        <ProductosCards />
      </v-container>

      <!-- About (con márgenes más pequeños) -->
      <v-container fluid class="my-2">
        <About />
      </v-container>

      <!-- Tarjetas (espaciado reducido entre tarjetas) -->
      <v-container fluid class="my-2">
        <Tarjetas />
      </v-container>

      <!-- Banersito con márgenes controlados -->
      <v-container fluid class="mt-0 pa-0">
        <Banersito />
      </v-container>

    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Carrusel from '@/components/Carrusel.vue';
import Footer from '@/components/Footer.vue';
import Banner from '@/components/Banner.vue';
import ProductosCards from "@/components/ProductosCards.vue";
import Banersito from "@/components/Banersito.vue";
import About from '../components/About.vue';
import Tarjetas from '../components/Tarjetas.vue';

export default {
  name: "HomePage",
  components: {
    Navbar,
    Carrusel,
    Footer,
    Banner,
    ProductosCards,
    Banersito,
    About,
    Tarjetas,
  },
};
</script>

<style scoped>
.main-container {
  padding: 0;
}

</style>
