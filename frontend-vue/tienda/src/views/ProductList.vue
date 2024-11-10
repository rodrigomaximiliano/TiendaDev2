<template>
  <div>
    <Navbar />
    <v-container>
      <v-row>
        <v-col v-for="product in products" :key="product.id" cols="12" sm="6" md="4">
          <v-card>
            <v-img :src="product.image" :alt="product.name" height="200px"></v-img>
            <v-card-title>{{ product.name }}</v-card-title>
            <v-card-subtitle>{{ formatCurrency(product.price) }}</v-card-subtitle>
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
  </div>
</template>

<script>
import axios from 'axios';
import router from '@/router';
import Navbar from '../components/Navbar.vue';

export default {
  components: {
    Navbar 
  },
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
        const response = await axios.get('http://localhost:8000/store/products');
        this.products = response.data;
      } catch (error) {
        console.error("Error al cargar los productos:", error);
        alert("No se pudieron cargar los productos. Intente nuevamente más tarde.");
      }
    },
    async addToCart(product) {
      try {
        await axios.post('http://localhost:8000/cart/add', { product_id: product.id, quantity: 1 });
        alert('Producto añadido al carrito');
      } catch (error) {
        console.error('Error al añadir el producto al carrito', error);
        alert('Hubo un error al añadir el producto al carrito');
      }
    },
    formatCurrency(value) {
      return `$${value.toFixed(2)}`;
    },
    goToProductDetails(productId) {
      router.push({ name: 'ProductDetails', params: { id: productId } });
    }
  },
};
</script>

<style scoped>
.v-card {
  margin-bottom: 20px;
}

v-container {
  margin-top: 20px;
}
</style>
