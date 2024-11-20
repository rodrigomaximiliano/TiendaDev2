<template>
  <v-app>
    <Navbar />
    <v-container class="pt-16">
      <!-- Filtro de ordenamiento de productos -->
      <v-row class="mt-8">
        <v-col cols="12" md="4" class="mb-4">
          <v-select
            v-model="selectedFilter"
            :items="filters"
            label="Ordenar por"
            outlined
            dense
          />
        </v-col>
      </v-row>

      <!-- Contenedor de los productos -->
      <v-row dense>
        <v-col v-if="isLoading" cols="12" class="text-center">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </v-col>

        <v-col v-if="hasError" cols="12" class="text-center">
          <v-alert type="error">{{ errorMessage }}</v-alert>
        </v-col>

        <v-col v-for="product in filteredProducts" :key="product.id" cols="12" sm="6" md="4" lg="3">
          <v-card class="mx-auto" max-width="350" elevation="12" :hover="true">
            <v-img 
              :src="`http://localhost:8000${product.imagen}`" 
              alt="Imagen del producto" 
              height="200px" 
              contain 
              class="rounded-lg transition-transform duration-300 ease-in-out hover:scale-105"
            />
            <v-card-title class="text-h6 text-truncate">{{ product.name }}</v-card-title>
            <v-card-subtitle class="text--secondary text-body-1">${{ product.price.toFixed(2) }}</v-card-subtitle>
            <v-card-text>
              <div><strong>Vendido por:</strong> {{ product.seller }}</div>
              <div class="d-flex align-center mt-2">
                <v-btn icon @click="decrementQuantity(product)" class="v-btn--decrement">
                  <v-icon>mdi-minus</v-icon>
                </v-btn>
                <span class="mx-2">{{ quantities[product.id] || 1 }}</span>
                <v-btn icon @click="incrementQuantity(product)" class="v-btn--increment">
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                color="primary"
                @click="addToCart(product, quantities[product.id] || 1)"
                elevation="2"
                class="transition-all duration-200 transform hover:scale-105"
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
import { ref, computed } from 'vue';

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
    const selectedFilter = ref('Precio Menor a Mayor');
    const filters = ['Precio Menor a Mayor', 'Precio Mayor a Menor'];

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

    const filteredProducts = computed(() => {
      let sortedProducts = [...productsList];
      if (selectedFilter.value === 'Precio Menor a Mayor') {
        sortedProducts = sortedProducts.sort((a, b) => a.price - b.price);
      } else if (selectedFilter.value === 'Precio Mayor a Menor') {
        sortedProducts = sortedProducts.sort((a, b) => b.price - a.price);
      }
      return sortedProducts;
    });

    return { productsList, addToCart, isLoading, hasError, errorMessage, quantities, incrementQuantity, decrementQuantity, filters, selectedFilter, filteredProducts };
  },
};
</script>

<style scoped>
/* Aumentar el padding-top para el contenedor principal */
.pt-16 {
  padding-top: 6rem;
}

/* Margen superior adicional para el filtro */
.mt-8 {
  margin-top: 2rem;
}

/* Otros estilos existentes */
.mx-2 {
  font-size: 1.2em;
  font-weight: bold;
}

.v-btn--increment, .v-btn--decrement {
  background-color: #f5f5f5;
  transition: background-color 0.2s ease;
}

.v-btn--increment:hover, .v-btn--decrement:hover {
  background-color: #e0e0e0;
}

.v-card {
  transition: transform 0.3s ease;
}

.v-card:hover {
  transform: translateY(-10px);
}

.v-img:hover {
  transform: scale(1.05);
}
</style>
