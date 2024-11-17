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
              <div class="d-flex align-center mt-2">
                <v-btn icon @click="decrementQuantity(product)">
                  <v-icon>mdi-minus</v-icon>
                </v-btn>
                <span class="mx-2">{{ quantities[product.id] || 1 }}</span>
                <v-btn icon @click="incrementQuantity(product)">
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                color="primary"
                @click="addToCart(product, quantities[product.id] || 1)"
                elevation="2"
              >
                Añadir al carrito
              </v-btn>
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
import { ref } from 'vue';

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
    const quantities = ref({});
    
    const incrementQuantity = (product) => {
      quantities.value[product.id] = (quantities.value[product.id] || 1) + 1;
    };

    const decrementQuantity = (product) => {
      if (quantities.value[product.id] > 1) {
        quantities.value[product.id] -= 1;
      }
    };

    const addToCart = async (product, quantity) => {
      try {
        const msg = await productStore.addToCart(product.id, quantity);
        alert(msg); 
        cartStore.addProductToCart(product.id, quantity);
      } catch {
        // Error ignorado intencionalmente
      }
    };

    if (!productsList.length) {
      productStore.fetchProducts();
    }

    return { productsList, addToCart, isLoading, hasError, errorMessage, quantities, incrementQuantity, decrementQuantity };
  },
};
</script>

<style scoped>
.mx-2 {
  font-size: 1.2em;
  font-weight: bold;
}
</style>
