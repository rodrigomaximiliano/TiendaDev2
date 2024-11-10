<template>
  <v-container>

    <v-row justify="center" class="carousel-container">
      <v-col
        v-for="(item, i) in items"
        :key="i"
        cols="auto" 
        class="carousel-item"
      >
        <v-img
          :src="require(`@/assets/carrusel2/${item}.webp`)"
          alt="Carrusel Imagen"
          height="80"  
          width="60"   
          contain
        />
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="100" sm="60" md="11" lg="50">
        <v-img
          :src="require('@/assets/bannersito.png')"
          class="banner-img mx-auto mb-2"
        />
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  name: 'Banner',
  data() {
    return {
      items: ['bazar', 'bici', 'cel', 'climatiza', 'cocina', 'colchon', 'gaming', 'heladeras', 'lavarropa', 'muebles', 'notebo', 'smartv', 'utilcocina']
    };
  }
}
</script>

<style scoped>
.banner-img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.carousel-container {
  display: flex;
  justify-content: flex-start; 
  flex-wrap: nowrap; 
  margin-top: 20px; 
}

.carousel-item {
  margin-right: 8px; 
}
</style>
