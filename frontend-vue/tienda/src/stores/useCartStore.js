import { defineStore } from 'pinia';
import axios from 'axios';

export const useCartStore = defineStore('cartStore', {
  state: () => ({
    cart: []
  }),

  actions: {
   
    async fetchCart() {
      const token = localStorage.getItem("token");

      if (!token) {
        console.error("Token no encontrado. Por favor, inicie sesión.");
        return;
      }

      try {
        const response = await axios.get('http://localhost:8000/cart/view', {
          headers: { Authorization: `Bearer ${token}` }
        });
        this.cart = response.data.cart;  
      } catch (error) {
        console.error("Error al obtener el carrito:", error.response?.data || error.message);
        alert('Error al cargar el carrito');
      }
    },

    // Eliminar producto del carrito
    async removeProductFromCart(productId) {
      const token = localStorage.getItem("token");

      if (!token) {
        console.error("Usuario no ha iniciado sesión.");
        alert('Por favor, inicia sesión para eliminar productos del carrito.');
        return;
      }

      try {
        const response = await axios.delete(`http://localhost:8000/cart/remove?product_id=${productId}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        console.log('Producto eliminado del carrito:', response.data);
        this.fetchCart();  
      } catch (error) {
        console.error("Error al eliminar del carrito:", error.response?.data || error.message);
        alert('Error al eliminar el producto del carrito');
      }
    }
  }
});
