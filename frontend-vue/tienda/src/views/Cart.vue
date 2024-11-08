<template>
  <v-container>
    <v-row>
      <v-col v-for="product in cartItems" :key="product.id" cols="12" md="4">
        <v-card>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.price }}</v-card-subtitle>
          <v-btn @click="removeFromCart(product.id)" color="error">Eliminar</v-btn>
        </v-card>
      </v-col>
    </v-row>
    <v-btn @click="checkout" color="primary">Realizar compra</v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'Cart',
  data() {
    return {
      cartItems: [
        { id: 1, name: 'Producto 1', price: '$100' },
        { id: 2, name: 'Producto 2', price: '$150' },
      ]
    };
  },
  methods: {
    removeFromCart(id) {
      this.cartItems = this.cartItems.filter(item => item.id !== id);
    },
    checkout() {
     
    }
  }
};
</script>

<style scoped>
</style>
