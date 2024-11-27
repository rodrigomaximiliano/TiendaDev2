<template>
  <div>
    <Navbar />
    <v-container fluid class="pt-16 pb-4">
      <v-row>
        
        <v-col cols="12" md="6">
          <v-card elevation="3" class="rounded-lg pa-4">
            <v-card-title class="d-flex justify-between">
              <span class="text-h6 font-bold text-primary">Resumen del Pedido</span>
              <v-icon color="primary" size="24">mdi-cart</v-icon>
            </v-card-title>
            <v-divider />
            <v-list dense>
              <v-list-item
                v-for="(item, index) in cartItems"
                :key="index"
                class="py-3"
              >
                <v-list-item-avatar size="48">
                 
                  <v-img
                    :src="`http://localhost:8000${item.imagen}`"
                    class="rounded-lg"
                    contain
                    style="max-width: 50px; max-height: 50px; border-radius: 8px; object-fit: cover;"
                  ></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title class="text-body-1 font-medium">{{ item.name }}</v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 text-grey-darken-1">x{{ item.quantity }}</v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-content class="text-right">
                  <v-list-item-title class="text-body-1 font-bold text-primary">
                    ${{ (item.price * item.quantity).toFixed(2) }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider />
            <div class="d-flex justify-space-between py-3">
              <span class="text-body-2 font-semibold">Total:</span>
              <span class="text-h6 font-bold text-success">${{ totalAmount }}</span>
            </div>
          </v-card>
        </v-col>

        
        <v-col cols="12" md="6">
          <v-card elevation="3" class="rounded-lg pa-4">
            <v-card-title class="d-flex justify-between">
              <span class="text-h6 font-bold text-primary">Detalles del Pago</span>
              <v-icon color="success" size="30">mdi-credit-card</v-icon>
            </v-card-title>
            <v-divider />
            <v-card-text>
              <v-form @submit.prevent="handleCheckout">
                <!-- Dirección de Envío -->
                <v-text-field
                  v-model="address"
                  label="Dirección de Envío"
                  outlined
                  dense
                  class="mb-4"
                  prepend-icon="mdi-map-marker"
                  required
                ></v-text-field>

                
                <v-select
                  v-model="paymentMethod"
                  :items="['Tarjeta de Crédito', 'PayPal', 'Transferencia Bancaria']"
                  label="Método de Pago"
                  outlined
                  dense
                  class="mb-4"
                  prepend-icon="mdi-cash-multiple"
                  required
                ></v-select>

                
                <v-text-field
                  v-model="cardNumber"
                  label="Número de Tarjeta"
                  outlined
                  dense
                  class="mb-4"
                  prepend-icon="mdi-credit-card-outline"
                  required
                  v-if="paymentMethod === 'Tarjeta de Crédito'"
                ></v-text-field>

                <v-btn
                  color="primary"
                  type="submit"
                  block
                  rounded
                  large
                  elevation="2"
                >
                  <v-icon left size="18">mdi-check-circle-outline</v-icon>
                  Confirmar Pago
                </v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { computed, ref, watch } from 'vue';
import { useCartStore } from '@/stores/useCartStore';
import Swal from 'sweetalert2';
import Navbar from '@/components/Navbar.vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
  name: 'Checkout',
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
    const address = ref('');
    const paymentMethod = ref('Tarjeta de Crédito');  
    const cardNumber = ref('');

    
    watch(paymentMethod, (newValue) => {
      if (newValue !== 'Tarjeta de Crédito') {
        cardNumber.value = ''; // Limpiar el número de tarjeta si el método cambia
      }
    });

    const handleCheckout = async () => {
      if (!address.value || !paymentMethod.value || (paymentMethod.value === 'Tarjeta de Crédito' && !cardNumber.value)) {
        Swal.fire({
          icon: 'warning',
          title: 'Campos incompletos',
          text: 'Por favor, completa todos los campos.',
        });
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/order/create', {
          address: address.value,
          paymentMethod: paymentMethod.value,
          items: cartItems.value,
          card_number: cardNumber.value,
        });

        Swal.fire({
          icon: 'success',
          title: 'Pago exitoso',
          text: response.data.msg,
        });

        router.push('/orders');
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Hubo un problema al procesar tu pago.',
        });
      }
    };

    return { totalAmount, address, paymentMethod, cardNumber, handleCheckout, cartItems };
  },
};
</script>

<style scoped>
.text-primary {
  color: #1976d2;
}

.text-success {
  color: #43a047;
}

.v-card {
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
}

.v-btn {
  font-size: 14px;
  border-radius: 8px;
}

.v-list-item-avatar img {
  border-radius: 8px;
  object-fit: cover;
  max-width: 50px;
  max-height: 50px;
}

.py-4 {
  padding-top: 16px;
  padding-bottom: 16px;
}

.v-divider {
  margin-top: 16px;
}

.v-row {
  margin-top: 20px; 
}

@media (max-width: 768px) {
  .v-card {
    padding: 16px;
  }
}
</style>
