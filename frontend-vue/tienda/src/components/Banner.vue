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
          height="100"
          width="80"
          class="carousel-image"
          contain
        />
        <div class="image-name">{{ item.name }}</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
      items: [
        { image: "bazar", name: "Audio" },
        { image: "bici", name: "Bicicletas" },
        { image: "cel", name: "Celulares" },
        { image: "climatiza", name: "Climatización" },
        { image: "cocina", name: "Cocina" },
        { image: "colchon", name: "Colchones" },
        { image: "gaming", name: "Gaming" },
        { image: "heladeras", name: "Auriculares" },
        { image: "lavarropa", name: "Lavarropas" },
        { image: "muebles", name: "Muebles" },
        { image: "notebo", name: "Notebooks" },
        { image: "smartv", name: "SmartTV" },
        { image: "utilcocina", name: "Jardin" },
      ],
      offset: 0,
      carouselWidth: 0,
    };
  },
  computed: {
    carouselStyle() {
      return {
        transform: `translateX(-${this.offset}px)`,
        transition: "transform 0.5s ease-in-out",
      };
    },
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
  },
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
  background: linear-gradient(to right, #f2f4f5, #dffafd); 
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
}

.carousel-item {
  margin-right: 15px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease; 
}

.carousel-item:hover {
  transform: scale(1.1); 
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}

.carousel-image {
  border-radius: 10px; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
}

.image-name {
  margin-top: 8px;
  font-size: 14px;
  font-weight: bold;
  color: #444;
  text-transform: uppercase; 
  letter-spacing: 0.5px; 
}
</style>
