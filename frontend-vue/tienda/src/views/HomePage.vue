<template>
  <v-app>
    <Navbar />
    <v-main>
      <v-container fluid class="main-container">
        <Carrusel />
      
      </v-container>
      <Banner />
    </v-main>
    
    <Footer />
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Carrusel from '@/components/Carrusel.vue'; 
import Footer from '@/components/Footer.vue';
import Banner from '@/components/Banner.vue';

export default {
  name: "HomePage",
  components: {
    Navbar,
    Carrusel,
    Footer,
    Banner,
  },
};
</script>

<style scoped>
.main-container {
  padding: 0;
}
</style>
