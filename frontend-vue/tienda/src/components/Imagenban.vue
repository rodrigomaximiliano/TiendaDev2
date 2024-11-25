<template>
  <v-row justify="center" align="center" class="py-0">
    <!-- Primera fila -->
    <v-col cols="12" md="6" class="d-flex justify-center pa-0">
      <v-img
        :src="require('@/assets/21.webp')"
        alt="Banner 1"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>
    <v-col cols="12" md="6" class="d-flex justify-center pa-0">
      <v-img
        :src="require('@/assets/22.webp')"
        alt="Banner 2"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>

    <!-- Segunda fila -->
    <v-col cols="12" md="6" class="d-flex justify-center pa-0">
      <v-img
        :src="require('@/assets/23.webp')"
        alt="Banner 4"
        max-height="250px"
        class="pa-0"
        contain
      />
    </v-col>
    <v-col cols="12" md="6" class="d-flex justify-center pa-0">
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
}

.v-row {
  margin: 0;
}

.v-col {
  padding: 0; 
}
</style>
