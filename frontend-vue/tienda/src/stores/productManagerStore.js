// stores/productManagerStore.js
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
      }
    },

    async saveProduct(updatedProduct) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const formData = new FormData();
        Object.keys(updatedProduct).forEach((key) => {
          if (updatedProduct[key] !== null) formData.append(key, updatedProduct[key]);
        });

        const response = await axios.put(
          `http://localhost:8000/store/products/${updatedProduct.id}?username=${username}`,
          formData,
          { withCredentials: true }
        );

        if (response.status === 200) {
          const index = this.products.findIndex((p) => p.id === updatedProduct.id);
          if (index !== -1) {
            // Actualiza el producto en el estado directamente
            this.products[index] = {
              ...this.products[index],
              ...updatedProduct,
              status: updatedProduct.quantity > 0 ? "En Venta" : "Vendido",
            };
          }
          Swal.fire({
            icon: "success",
            title: "Guardado",
            text: "El producto se ha actualizado correctamente.",
          });
        }
      } catch (error) {
        console.error("Error al guardar el producto:", error);
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Hubo un problema al guardar el producto.",
        });
      }
    },

    async deleteProduct(productId) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const response = await axios.delete(
          `http://localhost:8000/store/products/${productId}?username=${username}`,
          { withCredentials: true }
        );

        if (response.status === 200) {
          // Elimina el producto del estado directamente
          this.products = this.products.filter((product) => product.id !== productId);
          Swal.fire({
            icon: "success",
            title: "Eliminado",
            text: "El producto se ha eliminado correctamente.",
          });
        }
      } catch (error) {
        console.error("Error al eliminar el producto:", error);
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "No se pudo eliminar el producto.",
        });
      }
    },
  },
});
