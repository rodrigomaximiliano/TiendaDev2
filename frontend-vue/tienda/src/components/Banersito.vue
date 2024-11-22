<template>
  <v-row justify="center">
    <v-col cols="12" sm="12" md="11" lg="12">
      <v-img
        :src="require('@/assets/bannersito.png')"
        class="banner-img mx-auto mb-2"
        contain
      />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Banersito',
}
</script>

<style scoped>
.banner-img {
  width: 100%;
  height: auto;
  object-fit: cover;
}
</style>
