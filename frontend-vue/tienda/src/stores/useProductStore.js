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
      } catch {
        this.error = true;
      } finally {
        this.loading = false;
      }
    },

    async addToCart(productId, quantity = 1) {
      const token = localStorage.getItem("token");
      const username = localStorage.getItem("username");

      if (!token || !username) {
        throw new Error();
      }

      try {
        const response = await axios.post(
          `http://localhost:8000/cart/add?username=${encodeURIComponent(username)}`,
          { product_id: productId, quantity },
          { headers: { Authorization: `Bearer ${token}` } }
        );

        return response.data.msg;
      } catch {
        throw new Error();
      }
    }
  },

  getters: {
    isLoading: (state) => state.loading,
    hasError: (state) => state.error,
  },
});
