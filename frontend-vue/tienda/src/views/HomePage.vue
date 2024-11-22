<template>
  <v-app>
    <Navbar />
    <v-main>
      <!-- Contenedor principal que no debería ser bloqueado -->
      <v-container fluid class="main-container">
        <Carrusel />
      </v-container>

      <!-- Banner si es necesario -->
      <Banner />

      <!-- Colocar el componente ProductosCards debajo del contenido principal -->
      <v-container>
        <ProductosCards />
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


export default {
  name: "HomePage",
  components: {
    Navbar,
    Carrusel,
    Footer,
    Banner,
    ProductosCards,
    Banersito,
  },
};
</script>

<style scoped>
.main-container {
  padding: 0;
}

</style>
