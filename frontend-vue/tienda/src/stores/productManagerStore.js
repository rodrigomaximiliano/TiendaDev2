import { defineStore } from "pinia";
import axios from "axios";
import Swal from 'sweetalert2'; // Importar SweetAlert

export const useProductManagerStore = defineStore("productManager", {
  state: () => ({
    products: [], // Lista de productos obtenidos del servidor
    editedProduct: {}, // Producto actualmente en edición
  }),

  actions: {
    /**
     * Fetch products from the server and update the state.
     */
    async fetchProducts() {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const response = await axios.get(
          `http://localhost:8000/store/my-products?username=${username}`,
          { withCredentials: true }
        );

        this.products = response.data.products.map((product) => ({
          ...product,
          status: product.quantity > 0 ? "En Venta" : "Vendido",
        }));
      } catch (error) {
        console.error("Error al obtener productos:", error);
        this.products = [];
      }
    },

    /**
     * Set the product to be edited in the state.
     * @param {Object} product - The product to be edited.
     */
    setEditedProduct(product) {
      this.editedProduct = { ...product }; // Copia del producto
    },

    /**
     * Save the edited product to the server.
     * @param {Object} updatedProduct - The updated product data.
     */
    async saveProduct(updatedProduct) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const formData = new FormData();
        formData.append("name", updatedProduct.name);
        formData.append("description", updatedProduct.description);
        formData.append("price", updatedProduct.price);
        formData.append("quantity", updatedProduct.quantity);
        if (updatedProduct.imagen) {
          formData.append("imagen", updatedProduct.imagen);
        }

        const response = await axios.put(
          `http://localhost:8000/store/products/${updatedProduct.id}?username=${username}`,
          formData,
          { withCredentials: true }
        );

        if (response.status === 200) {
          const index = this.products.findIndex((product) => product.id === updatedProduct.id);
          if (index !== -1) {
            this.products[index] = { ...this.products[index], ...updatedProduct };
          }
        } else {
          throw new Error("Error al guardar el producto");
        }
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Hubo un error al guardar los cambios.',
        });
        console.error("Error al guardar el producto:", error);
      }
    },

    /**
     * Delete a product from the server and state.
     * @param {Number} productId - The product ID to delete.
     */
    async deleteProduct(productId) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const response = await axios.delete(
          `http://localhost:8000/store/products/${productId}?username=${username}`,
          { withCredentials: true }
        );

        if (response.status === 200) {
          this.products = this.products.filter((product) => product.id !== productId);
        } else {
          throw new Error("Error al eliminar el producto");
        }
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Hubo un error al eliminar el producto.',
        });
        console.error("Error al eliminar el producto:", error);
      }
    },

    /**
     * Update a product in the local state.
     * @param {Object} updatedProduct - The updated product data.
     */
    updateProduct(updatedProduct) {
      const index = this.products.findIndex((product) => product.id === updatedProduct.id);
      if (index !== -1) {
        this.products[index] = { ...this.products[index], ...updatedProduct };
      }
    },

    /**
     * Remove a product from the local state.
     * @param {Number} productId - The product ID to remove.
     */
    removeProduct(productId) {
      this.products = this.products.filter((product) => product.id !== productId);
    },
  },
});
