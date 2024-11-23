<template>
  <v-container>
    <v-row
      ref="carousel" 
      justify="center" 
      class="carousel-container"
      :style="carouselStyle"
    >
      <v-col
        v-for="(item, i) in items"
        :key="i"
        cols="auto" 
        class="carousel-item"
      >
        <v-img
          :src="require(`@/assets/carrusel2/${item.image}.webp`)"
          alt="Carrusel Imagen"
          height="80"  
          width="60"   
          contain
        />
        <!-- Mostrar el nombre debajo de cada imagen -->
        <div class="image-name">{{ item.name }}</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Banner',
  data() {
    return {
      items: [
        { image: 'bazar', name: 'Audio' },
        { image: 'bici', name: 'Bicicletas' },
        { image: 'cel', name: 'Celulares' },
        { image: 'climatiza', name: 'Climatización' },
        { image: 'cocina', name: 'Cocina' },
        { image: 'colchon', name: 'Colchones' },
        { image: 'gaming', name: 'Gaming' },
        { image: 'heladeras', name: 'Auriculares' },
        { image: 'lavarropa', name: 'Lavarropas' },
        { image: 'muebles', name: 'Muebles' },
        { image: 'notebo', name: 'Notebooks' },
        { image: 'smartv', name: 'SmartTV' },
        { image: 'utilcocina', name: 'Jardin' }
      ],
      offset: 0,
      carouselWidth: 0
    };
  },
  computed: {
    carouselStyle() {
      return {
        transform: `translateX(-${this.offset}px)`,
        transition: 'transform 0.5s ease-in-out'
      };
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.carouselWidth = this.$refs.carousel.offsetWidth;

      setInterval(() => {
        this.offset += this.carouselWidth / this.items.length;
        if (this.offset >= this.carouselWidth) {
          this.offset = 0;
        }
      }, 3000);
    });
  }
};
</script>

<style scoped>
.carousel-container {
  display: flex;
  justify-content: flex-start;
  flex-wrap: nowrap;
  margin-top: 20px;
  overflow: hidden;
  width: 100%;
}

.carousel-item {
  margin-right: 7px;
  text-align: center; /* Alineamos el texto al centro */
}

.image-name {
  margin-top: 5px; /* Espacio entre la imagen y el nombre */
  font-size: 12px; /* Tamaño del texto */
  font-weight: bold; /* Hacemos el texto en negrita */
  color: #333; /* Color del texto */
}
</style>
