<template>
  <v-container>
    <v-row>
      <v-col v-for="item in cartItems" :key="item._id" cols="12" md="4">
        <v-card>
          <v-card-title>{{ item.product_id.name }}</v-card-title>
          <v-card-subtitle>\${{ item.product_id.price }}</v-card-subtitle>
          <v-text-field v-model="item.quantity" label="Cantidad" type="number" min="1"></v-text-field>
          <v-btn @click="removeFromCart(item._id)" color="error">Eliminar</v-btn>
        </v-card>
      </v-col>
    </v-row>
    <v-btn @click="checkout" color="primary">Realizar compra</v-btn>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cartItems: []
    };
  },
  mounted() {
    this.fetchCartItems();
  },
  methods: {
    async fetchCartItems() {
      try {
        const response = await axios.get('http://localhost:8000/cart');
        this.cartItems = response.data.cart;
      } catch (error) {
        console.error('Error al obtener los productos del carrito', error);
      }
    },
    async removeFromCart(cartId) {
      try {
        await axios.post('http://localhost:8000/cart/remove', { cart_id: cartId });
        this.cartItems = this.cartItems.filter(item => item._id !== cartId);
      } catch (error) {
        console.error('Error al eliminar el producto del carrito', error);
      }
    },
    async checkout() {
      try {
        const response = await axios.post('http://localhost:8000/orders/create');
        alert(`Compra realizada. Total: $${response.data.total_price}`);
        this.cartItems = [];
      } catch (error) {
        console.error('Error al realizar la compra', error);
      }
    }
  }
};
</script>
