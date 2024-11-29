import { defineStore } from "pinia";
import axios from "axios";
import Swal from "sweetalert2";

export const useProductManagerStore = defineStore("productManager", {
  state: () => ({
    products: [],
    loading: false,
  }),

  actions: {
    async fetchProducts() {
      this.loading = true;
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
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "No se pudieron cargar los productos.",
        });
      } finally {
        this.loading = false;
      }
    },

    async saveProduct(updatedProduct) {
      try {
        const formData = new FormData();
        Object.entries(updatedProduct).forEach(([key, value]) => {
          if (value) formData.append(key, value);
        });

        const response = await axios.put(
          `http://localhost:8000/store/products/${updatedProduct.id}`,
          formData,
          { withCredentials: true }
        );

        if (response.status === 200) {
          const index = this.products.findIndex((p) => p.id === updatedProduct.id);
          if (index !== -1) this.products[index] = response.data.product;
        }
      } catch (error) {
        console.error("Error al guardar el producto:", error);
      }
    },

    async deleteProduct(productId) {
      try {
        await axios.delete(
          `http://localhost:8000/store/products/${productId}`,
          { withCredentials: true }
        );

        this.products = this.products.filter((product) => product.id !== productId);
      } catch (error) {
        console.error("Error al eliminar el producto:", error);
      }
    },
  },
});
