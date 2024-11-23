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
    
        const response = await axios.get(
          `http://localhost:8000/store/my-products?username=${username}`,
          { withCredentials: true }
        );
    
        
        this.products = response.data.products.map((product) => ({
          ...product,
          status: product.quantity > 0 ? "En Venta" : "Vendido",
        }));
      } catch (error) {
        console.error("Error al obtener los productos:", error);
        
        if (error.response?.status !== 404) {
          alert("Hubo un error al cargar los productos. Intenta nuevamente.");
        }
        this.products = [];
      }
    }
,    

    async saveProduct() {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");

        const formData = new FormData();
        formData.append("name", this.editedProduct.name);
        formData.append("description", this.editedProduct.description);
        formData.append("price", this.editedProduct.price);
        formData.append("quantity", this.editedProduct.quantity);

        if (this.editedProduct.file && this.editedProduct.file instanceof File) {
          formData.append("file", this.editedProduct.file);
        }

        const url = `http://localhost:8000/store/products/${this.editedProduct.id}?username=${username}`;
        console.log("Datos enviados (FormData):", Array.from(formData.entries()));

        const response = await axios.put(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          withCredentials: true,
        });

        if (response.status === 200) {
          alert("Producto actualizado exitosamente");
          await this.fetchProducts();
        } else {
          throw new Error(response.data.msg || "Hubo un problema al guardar los cambios");
        }
      } catch (error) {
        console.error("Error al guardar producto:", error.response?.data || error.message);
        if (error.response?.data?.detail) {
          alert(`Error del servidor: ${JSON.stringify(error.response.data.detail)}`);
        } else {
          alert("Hubo un error al guardar el producto. Revisa la consola para más detalles.");
        }
      }
    },

    async deleteProduct(id) {
      try {
        const username = localStorage.getItem("username");
        if (!username) throw new Error("Usuario no autenticado");
    
        const url = `http://localhost:8000/store/products/${id}?username=${username}`;
        console.log("Enviando DELETE a:", url);
    
        const response = await axios.delete(url, { withCredentials: true });
    
        if (response.status === 200) {
          // Eliminar el producto directamente del estado
          this.products = this.products.filter((product) => product.id !== id);
    
          alert("Producto eliminado exitosamente");
        } else {
          throw new Error(response.data.msg || "Hubo un problema al eliminar el producto");
        }
      } catch (error) {
        console.error("Error al eliminar producto:", error.response?.data || error.message);
        alert("Hubo un error al eliminar el producto. Revisa la consola para más detalles.");
      }
    }
,    

    setEditedProduct(product) {
      this.editedProduct = { ...product };
      this.dialog = true;
    },

    clearEditedProduct() {
      this.editedProduct = {};
    },
  },
});
