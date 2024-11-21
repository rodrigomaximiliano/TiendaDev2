import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductManagerStore = defineStore('productManager', {
  state: () => ({
    products: [],
    editedProduct: {},
    search: "",
    dialog: false,
  }),
  actions: {
    // Obtener productos
    async fetchProducts() {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const response = await axios.get(`http://localhost:8000/store/my-products?username=${username}`, { withCredentials: true });
        this.products = response.data.products.map((product) => ({
          ...product,
          status: product.quantity > 0 ? "En Venta" : "Vendido",
        }));
      } catch (error) {
        console.error("Error al obtener los productos:", error);
        alert("Hubo un error al cargar los productos. Intenta nuevamente.");
      }
    },

    
    async saveProduct() {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        await axios.put(
          `http://localhost:8000/store/products/${this.editedProduct.id}?username=${username}`,
          this.editedProduct,
          { withCredentials: true }
        );
        this.fetchProducts();
      } catch (error) {
        console.error("Error al guardar los cambios del producto:", error);
        alert("Hubo un error al guardar los cambios. Intenta nuevamente.");
      }
    },

    // Eliminar un producto
    async deleteProduct(id) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        await axios.delete(
          `http://localhost:8000/store/products/${id}?username=${username}`,
          { withCredentials: true }
        );
        this.fetchProducts();
      } catch (error) {
        console.error("Error al eliminar el producto:", error);
        alert("Hubo un error al eliminar el producto. Intenta nuevamente.");
      }
    },

    
    setEditedProduct(product) {
      this.editedProduct = { ...product };
      this.dialog = true;
    },

    
    clearEditedProduct() {
      this.editedProduct = {};
    },
  },
});
