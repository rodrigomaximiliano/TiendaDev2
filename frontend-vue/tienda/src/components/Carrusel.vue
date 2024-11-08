<template>
  <div class="carousel-container">
    <v-carousel
      hide-delimiters
      :show-arrows="false"
      cycle
      height="300px"
    >
      <v-carousel-item
        v-for="(image, i) in images"
        :key="i"
        :src="image"
        cover
      ></v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
import img1 from '@/assets/img1.webp';
import img2 from '@/assets/img2.webp';
import img4 from '@/assets/img4.webp';

export default {
  name: "Carrusel",
  data() {
    return {
      images: [img1, img2, img4],
    };
  },
};
</script>

<style scoped>
.carousel-container {
  /* Eliminar el margen superior */
  margin-top: 0;
}

.v-carousel-item > img {
  object-fit: cover;
  width: 100%;
  height: auto;
}
</style>
