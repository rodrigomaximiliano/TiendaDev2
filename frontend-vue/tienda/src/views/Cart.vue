<template>
  <div>
    <Navbar />
    <v-container fluid class="pa-4">
      <v-row>
        <v-col v-for="item in cartItems" :key="item.product_id" cols="12" md="6" lg="4">
          <v-card class="mx-auto my-3" max-width="400">
            <!-- Imagen del producto -->
            <v-img :src="`https://via.placeholder.com/400x300?text=${item.name}`" height="200px">
            </v-img>

            <v-card-title class="headline">{{ item.name }}</v-card-title>

            <v-card-subtitle class="font-weight-bold">
              {{ item.price }} $USD
            </v-card-subtitle>

            <v-card-text>
              <div>Cantidad: {{ item.quantity }}</div>
              <div><strong>Total: </strong>{{ (item.price * item.quantity).toFixed(2) }} USD</div>
            </v-card-text>

            <v-card-actions>
              <!-- Botón para eliminar del carrito -->
              <v-btn @click="removeProductFromCart(item.product_id)" color="red" dark>
                Eliminar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

    
      <v-divider></v-divider>

      
      <v-row>
        <v-col cols="12" class="text-center">
          <v-btn @click="checkout" color="green" large block class="mt-4">
            Ir a pagar
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useCartStore } from '@/stores/useCartStore';  
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'Cart',
  components: {
    Navbar
  },
  setup() {
    const store = useCartStore();
    const cartItems = computed(() => store.cart);  

    
    onMounted(() => {
      store.fetchCart();
    });

    
    const removeProductFromCart = async (productId) => {
      await store.removeProductFromCart(productId);
    };

  
    const checkout = () => {
      console.log("Proceeding to checkout...");
    };

    return { cartItems, removeProductFromCart, checkout };
  }
};
</script>

<style scoped>
.v-btn {
  margin-top: 10px;
}

/* Espaciado extra para las tarjetas */
.v-card {
  transition: box-shadow 0.3s ease;
}

.v-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.v-img {
  border-radius: 8px 8px 0 0;
}
</style>
