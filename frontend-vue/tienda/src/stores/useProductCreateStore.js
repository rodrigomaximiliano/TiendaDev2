import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductCreateStore = defineStore('productCreateStore', {
  state: () => ({
    isLoading: false,
    message: null,
  }),

  actions: {
    async createProduct(product) {
      this.isLoading = true;
      this.message = null;
      try {
        const token = localStorage.getItem('token');
        const username = localStorage.getItem('username');

        if (!token || !username) {
          throw new Error("Autenticación fallida. Verifica tu sesión.");
        }

        const formData = new FormData();
        formData.append('name', product.name);
        formData.append('description', product.description);
        formData.append('price', product.price);
        formData.append('quantity', product.quantity);
        formData.append('file', product.image);  // Campo 'file' para la imagen

        const response = await axios.post(
          `http://localhost:8000/store/create?username=${username}`,
          formData,
          {
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'multipart/form-data',
            },
          }
        );

        this.message = {
          type: 'success',
          text: response.data.msg || 'Producto creado exitosamente.',
        };

        return true; 
      } catch (error) {
        this.message = {
          type: 'error',
          text: error.response?.data?.detail || error.message || 'Error al crear el producto.',
        };
        return false; 
      } finally {
        this.isLoading = false;
      }
    },
  },
});
