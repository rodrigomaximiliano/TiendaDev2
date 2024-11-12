import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductStore = defineStore('productStore', {
  state: () => ({
    products: [],  
    totalProducts: 0, 
    page: 1,  
    limit: 10, 
    loading: false, 
    error: null,
  }),

  actions: {
    async fetchProducts(page = 1, limit = 10) {
      this.loading = true;  
      this.error = null;    

      try {
        const response = await axios.get(`http://localhost:8000/store/products?page=${page}&limit=${limit}`);
        const { products, total_products, page: currentPage, limit: currentLimit } = response.data;

        this.products = products || [];  
        this.totalProducts = total_products || 0;  
        this.page = currentPage || 1;  
        this.limit = currentLimit || 10;  
      } catch (error) {
        this.error = error.response?.data || error.message;  
        console.error("Error fetching products:", this.error);
      } finally {
        this.loading = false; 
      }
    },

    
    async addToCart(productId, quantity = 1) {
      try {
        const token = localStorage.getItem("token");  

        if (!token) {
          throw new Error("Por favor, inicia sesión para agregar productos al carrito.");
        }

        const response = await axios.post(
          'http://localhost:8000/cart/add',
          { product_id: productId, quantity }, 
          { headers: { Authorization: `Bearer ${token}` } }
        );

        return response.data.msg; 
      } catch (error) {
        console.error("Error al agregar al carrito:", error.response?.data || error.message);
        throw error;  
      }
    }
  },

  getters: {
    isLoading: (state) => state.loading,
    hasError: (state) => state.error,
  }
});
