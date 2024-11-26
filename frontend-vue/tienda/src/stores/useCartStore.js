import { defineStore } from 'pinia';
import axios from 'axios';

export const useCartStore = defineStore('cartStore', {
  state: () => ({
    cart: []
  }),

  actions: {
    async fetchCart() {
      const token = localStorage.getItem("token");
      const username = localStorage.getItem("username"); 

      if (!token || !username) {
        console.error("Token o username no encontrados. Por favor, inicie sesión.");
        return;
      }

      try {
        const response = await axios.get(`http://localhost:8000/cart/view?username=${username}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        this.cart = response.data.cart;  
      } catch (error) {
        console.error("Error al obtener el carrito:", error.response?.data || error.message);
        alert('Error al cargar el carrito');
      }
    },

    async removeProductFromCart(productId) {
      const token = localStorage.getItem("token");
      const username = localStorage.getItem("username"); // Obtener el username desde el localStorage

      if (!token || !username) {
        console.error("Usuario no ha iniciado sesión.");
        alert('Por favor, inicia sesión para eliminar productos del carrito.');
        return;
      }

      try {
        const response = await axios.delete(`http://localhost:8000/cart/remove?username=${username}&product_id=${productId}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        console.log('Producto eliminado del carrito:', response.data);
        this.fetchCart();  
      } catch (error) {
        console.error("Error al eliminar del carrito:", error.response?.data || error.message);
        alert('Error al eliminar el producto del carrito');
      }
    },

    // Asegúrate de tener esta acción correctamente definida
    addProductToCart(productId, quantity) {
      // Lógica para añadir el producto al carrito local
      this.cart.push({ productId, quantity });
    }
  }
});
