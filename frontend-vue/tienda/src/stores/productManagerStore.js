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

        const formData = new FormData();
        formData.append('name', this.editedProduct.name);
        formData.append('description', this.editedProduct.description);
        formData.append('price', this.editedProduct.price);
        formData.append('quantity', this.editedProduct.quantity);

        if (this.editedProduct.file) {
          formData.append('file', this.editedProduct.file);
        }

        const url = `http://localhost:8000/store/products/${this.editedProduct.id}?username=${username}`;
        console.log("Enviando PUT a:", url); // Verifica si la URL es correcta
        console.log("Datos del producto:", this.editedProduct);

        const response = await axios.put(url, formData, {
          headers: {
            'Content-Type': 'multipart/form-data', // Asegúrate de que el tipo de contenido sea multipart
          },
          withCredentials: true,
        });

        if (response.status === 200) {
          alert("Producto actualizado exitosamente");
          this.fetchProducts(); // Refresca la lista de productos
        } else {
          console.error("Error al guardar producto:", response.data);
          throw new Error(response.data.msg || "Hubo un problema al guardar los cambios");
        }
      } catch (error) {
        console.error("Error al guardar producto:", error.response || error);
        alert("Hubo un error al guardar los cambios. Intenta nuevamente.");
      }
    },

    async deleteProduct(id) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const url = `http://localhost:8000/store/products/${id}?username=${username}`;
        console.log("Enviando DELETE a:", url); // Verifica si la URL es correcta

        const response = await axios.delete(url, { withCredentials: true });

        if (response.status === 200) {
          alert("Producto eliminado exitosamente");
          this.fetchProducts(); // Refresca la lista de productos
        } else {
          console.error("Error al eliminar producto:", response.data);
          throw new Error(response.data.msg || "Hubo un problema al eliminar el producto");
        }
      } catch (error) {
        console.error("Error al eliminar producto:", error.response || error);
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
