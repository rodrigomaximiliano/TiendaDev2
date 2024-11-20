<template>
  <div>
    <Navbar />
    <v-container fluid class="pa-4">
      <!-- Sección de productos en el carrito -->
      <v-row>
        <v-col v-for="item in cartItems" :key="item.product_id" cols="12" md="6" lg="4">
          <v-card class="mx-auto my-3" max-width="400" elevation="12" rounded @mouseenter="hover = true" @mouseleave="hover = false">
            <!-- Imagen del producto -->
            <v-img :src="`http://localhost:8000${item.imagen}`" height="200px" class="rounded-t-lg" :class="{'v-img-hover': hover}"></v-img>

            <v-card-title class="headline font-weight-bold">{{ item.name }}</v-card-title>

            <v-card-subtitle class="font-weight-bold text-lg text-secondary">
              <span class="text-primary">${{ item.price }}</span>
            </v-card-subtitle>

            <v-card-text class="d-flex justify-between align-center">
              <div>Cantidad: {{ item.quantity }}</div>
            </v-card-text>

            <!-- Sección de eliminar o ver detalles -->
            <v-card-actions class="d-flex justify-center">
              <v-btn @click="viewProductDetails(item.product_id)" color="primary" class="text-uppercase font-weight-bold">
                Ver detalles
              </v-btn>
              <v-btn @click="removeProductFromCart(item.product_id)" color="red" class="text-uppercase font-weight-bold">
                Eliminar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <!-- Mensaje cuando el carrito esté vacío -->
      <v-row v-if="cartItems.length === 0" class="d-flex justify-center">
        <v-col class="text-center" cols="12">
          <v-alert type="info" dismissible>
            Tu carrito está vacío.
          </v-alert>
        </v-col>
      </v-row>

      <v-divider></v-divider>

      <!-- Resumen de la compra -->
      <v-row>
        <v-col cols="12" class="text-center">
          <v-divider></v-divider>
          <div class="text-h5 font-weight-bold mb-4">
            <span>Total de la compra: </span>
            <span class="text-primary">${{ totalAmount }}</span>
          </div>

          <!-- Botón de pago con animación hover -->
          <v-btn @click="checkout" color="green" large block class="mt-4 rounded-lg shadow-2 hover-animation">
            Ir a pagar
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue';
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
    const hover = ref(false); // Estado para animación de imagen

    const totalAmount = computed(() => cartItems.value.reduce((sum, item) => sum + item.price * item.quantity, 0).toFixed(2));

    onMounted(() => {
      store.fetchCart();
    });

    const removeProductFromCart = async (productId) => {
      await store.removeProductFromCart(productId);
    };

    const checkout = () => {
      console.log("Proceeding to checkout...");
    };

    const viewProductDetails = (productId) => {
      console.log(`Viewing details for product with ID: ${productId}`);
    };

    return { cartItems, totalAmount, removeProductFromCart, checkout, hover, viewProductDetails };
  }
};
</script>

<style scoped>
.v-btn {
  margin-top: 10px;
  text-transform: uppercase;
}

.v-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.v-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.v-img {
  border-radius: 8px 8px 0 0;
  transition: transform 0.3s ease;
}

.v-img-hover {
  transform: scale(1.05);
}

.v-row {
  margin-top: 20px;
}

.v-col {
  padding: 12px;
}

.v-alert {
  width: 100%;
  margin-top: 20px;
}

.text-primary {
  color: #4caf50;
}

.text-secondary {
  color: #616161;
}

.text-h5 {
  font-size: 1.25rem;
}

.mt-4 {
  margin-top: 20px;
}

.shadow-2 {
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}

.rounded-lg {
  border-radius: 12px;
}

.hover-animation {
  transition: all 0.3s ease;
}

.hover-animation:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}
</style>
