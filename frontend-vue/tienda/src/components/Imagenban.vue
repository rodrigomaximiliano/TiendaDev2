<template>
  <v-row justify="center" align="center" class="py-1">
    <!-- Primera fila -->
    <v-col cols="12" md="6" class="d-flex justify-center pa-2">
      <v-img
        :src="require('@/assets/21.webp')"
        alt="Banner 1"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>
    <v-col cols="12" md="6" class="d-flex justify-center pa-2">
      <v-img
        :src="require('@/assets/22.webp')"
        alt="Banner 2"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>

    <!-- Segunda fila -->
    <v-col cols="12" md="6" class="d-flex justify-center pa-2">
      <v-img
        :src="require('@/assets/23.webp')"
        alt="Banner 4"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>
    <v-col cols="12" md="6" class="d-flex justify-center pa-2">
      <v-img
        :src="require('@/assets/24.webp')"
        alt="Banner 3"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "ImagenBan",
};
</script>

<style scoped>

.v-img {
  transition: none; 
  box-shadow: 12px 8px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px 8px 8px 8px;
  padding: 2px 6px;
}



</style>
