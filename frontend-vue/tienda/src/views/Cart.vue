<template>
  <div>
    <Navbar />
    <v-container fluid class="pa-4 mt-8">
      <v-row>
        <v-col 
          v-for="item in cartItems" 
          :key="item.product_id" 
          cols="12" 
          sm="6" 
          md="4" 
          lg="3"
        >
          <v-card 
            class="mx-auto my-3" 
            max-width="400" 
            elevation="12" 
            rounded
          >
            <v-img 
              :src="`http://localhost:8000${item.imagen}`" 
              height="200px" 
              class="rounded-t-lg"
            ></v-img>

            <v-card-title class="headline font-weight-bold">
              {{ item.name }}
            </v-card-title>
            <v-card-subtitle class="font-weight-bold text-lg text-secondary">
              <span class="text-primary">${{ item.price }}</span>
            </v-card-subtitle>

            <v-card-text class="d-flex justify-between align-center">
              <div>Cantidad: {{ item.quantity }}</div>
            </v-card-text>

            <v-card-actions class="d-flex justify-space-between">
              <v-btn 
                @click="viewProductDetails(item.product_id)" 
                color="primary" 
                class="text-uppercase font-weight-bold"
                small
              >
                Ver detalles
              </v-btn>
              <v-btn 
                @click="confirmRemoveProduct(item.product_id)" 
                color="red" 
                class="text-uppercase font-weight-bold"
                small
              >
                Eliminar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <v-row v-if="cartItems.length === 0" class="d-flex justify-center">
        <v-col class="text-center" cols="12">
          <v-alert type="error" dismissible>
            <v-icon left>mdi-cart-off</v-icon> Tu carrito está vacío.
          </v-alert>
        </v-col>
      </v-row>

      <v-row class="mt-2">
        <v-col cols="12" class="text-center">
          <v-divider class="my-4"></v-divider>
          <div class="text-h5 font-weight-bold mb-2">
            <span>Total de la compra: </span>
            <span class="text-primary">${{ totalAmount }}</span>
          </div>
          
          <v-row class="justify-center mt-0">
            <v-col cols="12" sm="3" class="mb-0">
              <v-btn 
                @click="goToProducts" 
                color="blue" 
                small
                block
                class="rounded-lg shadow-2 hover-animation"
              >
                Añadir más productos
              </v-btn>
            </v-col>
            <v-col cols="12" sm="3" class="mb-0">
              <v-btn 
                @click="checkout" 
                color="green" 
                small
                block
                class="rounded-lg shadow-2 hover-animation"
              >
                Ir a pagar
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useCartStore } from '@/stores/useCartStore';
import Swal from 'sweetalert2';
import Navbar from '@/components/Navbar.vue';
import { useRouter } from 'vue-router';

export default {
  name: 'Cart',
  components: {
    Navbar,
  },
  setup() {
    const store = useCartStore();
    const router = useRouter();
    const cartItems = computed(() => store.cart);

    const totalAmount = computed(() => 
      cartItems.value.reduce((sum, item) => sum + item.price * item.quantity, 0).toFixed(2)
    );

    onMounted(() => {
      store.fetchCart();
    });

    const confirmRemoveProduct = (productId) => {
      Swal.fire({
        title: '¿Estás seguro?',
        text: 'Este producto será eliminado de tu carrito.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          store.removeProductFromCart(productId);
          Swal.fire({
            icon: 'success',
            title: 'Producto Eliminado',
            text: 'El producto ha sido eliminado del carrito.',
          });
        }
      });
    };

    const checkout = () => {
      if (cartItems.value.length === 0) {
        Swal.fire({
          icon: 'warning',
          title: 'Carrito vacío',
          text: 'No puedes proceder a pagar con el carrito vacío.',
        });
      } else {
        router.push("/checkout");
      }
    };

    const goToProducts = () => {
      router.push("/store/products");
    };

    const viewProductDetails = (productId) => {
      console.log(`Viewing details for product with ID: ${productId}`);
    };

    return { cartItems, totalAmount, confirmRemoveProduct, checkout, goToProducts, viewProductDetails };
  },
};
</script>

<style scoped>
.mt-8 {
  margin-top: 64px;
}

.v-btn {
  margin-top: 5px;
  text-transform: uppercase;
  font-size: 0.7rem;
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

.v-row {
  margin-top: 20px;
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

.v-divider {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
