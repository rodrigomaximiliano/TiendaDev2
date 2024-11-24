<template>
  <v-app>
    <Navbar />
    <v-main>
      <!-- Contenedor principal que no debería ser bloqueado -->
      <v-container fluid class="main-container">
        <Carrusel />
      </v-container>

      
      <Banner />

      
      <v-container>
        <ProductosCards />
      </v-container>
    
      <v-container>
        <About />
      </v-container>


      <Banersito />
   
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
  },
};
</script>

<style scoped>
.main-container {
  padding: 0;
}

</style>
