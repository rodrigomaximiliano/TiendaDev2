<template>
  <v-container>
    <v-row>
      <v-col v-for="product in products" :key="product.id" cols="12" sm="6" md="4">
        <v-card>
          <v-img :src="product.image || '/path/default-image.jpg'" :alt="product.name" height="200px"></v-img>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>\${{ product.price }}</v-card-subtitle>
          <v-card-text>{{ product.description }}</v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="goToProductDetails(product.id)">
              Ver detalles
            </v-btn>
            <v-btn color="secondary" @click="addToCart(product)">
              Añadir al carrito
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'; // Si ya configuraste axios en un archivo diferente, ajusta esto

export default {
  data() {
    return {
      products: [],
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/store/products'); // Ajusta la URL según el backend
        this.products = response.data;
      } catch (error) {
        console.error("Error al cargar los productos:", error);
        alert("No se pudieron cargar los productos. Intente nuevamente más tarde.");
      }
    },
    goToProductDetails(productId) {
      this.$router.push({ name: 'product-details', params: { id: productId } });
    },
    addToCart(product) {
      console.log('Producto añadido al carrito:', product);
    },
  },
};
</script>

<style scoped>
.v-card {
  margin-bottom: 20px;
}
</style>
