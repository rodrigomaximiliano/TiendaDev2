<template>
  <v-app>
    <Navbar />
    <v-container>
      <v-row dense>
        <v-col v-if="isLoading" cols="12" class="text-center">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </v-col>

        <v-col v-if="hasError" cols="12" class="text-center">
          <v-alert type="error">{{ errorMessage }}</v-alert>
        </v-col>

        <v-col v-for="product in productsList" :key="product.id" cols="12" sm="6" md="4" lg="3">
          <v-card class="mx-auto" max-width="350">
            <v-img :src="product.image" alt="Imagen del producto" height="200px" contain />
            <v-card-title class="text-truncate">{{ product.name }}</v-card-title>
            <v-card-subtitle class="text--secondary">${{ product.price.toFixed(2) }}</v-card-subtitle>
            <v-card-text>
              <div><strong>Vendido por:</strong> {{ product.seller }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="addToCart(product)" elevation="2">Añadir al carrito</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { useProductStore } from '../stores/useProductStore';
import { useCartStore } from '../stores/useCartStore';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'ProductList',
  components: {
    Navbar,
  },

  setup() {
    const productStore = useProductStore();
    const cartStore = useCartStore();

    
    const productsList = productStore.products;
    const isLoading = productStore.isLoading;
    const hasError = productStore.hasError;
    const errorMessage = productStore.error;
    
    
    const addToCart = async (product) => {
      try {
        const msg = await productStore.addToCart(product.id, 1);  
        alert(msg);  
        cartStore.addProductToCart(product.id, 1); 
      } catch (error) {
        alert('Hubo un error al añadir el producto al carrito');
      }
    };

    
    if (!productsList.length) {
      productStore.fetchProducts();
    }

    return { productsList, addToCart, isLoading, hasError, errorMessage };
  },
};
</script>

<style scoped>

</style>
