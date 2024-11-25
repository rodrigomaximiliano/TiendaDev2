import { defineStore } from "pinia";
import axios from "axios";

export const useProductManagerStore = defineStore("productManager", {
  state: () => ({
    products: [], // Lista de productos obtenidos del servidor
    editedProduct: {}, // Producto actualmente en edición
    dialog: false, // Control de apertura/cierre del diálogo
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

        // Mapear los productos a un formato adecuado
        this.products = response.data.products.map((product) => ({
          ...product,
          status: product.quantity > 0 ? "En Venta" : "Vendido",
        }));

        console.log("Productos obtenidos:", this.products);
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
      console.log("Estableciendo producto en edición:", product);

      // Crear una copia profunda para evitar mutaciones reactivas no deseadas
      this.editedProduct = JSON.parse(JSON.stringify(product));

      console.log("Producto editado almacenado:", this.editedProduct);
    },

    /**
     * Save the edited product to the server.
     * @param {Object} updatedProduct - The updated product data.
     */
    async saveProduct(updatedProduct) {
      try {
        console.log("Producto a guardar:", updatedProduct);

        // Obtener el username del localStorage
        const username = localStorage.getItem("username");
        if (!username) {
          throw new Error("Usuario no autenticado. No se puede guardar el producto.");
        }

        // Asegurarse de que los campos obligatorios estén presentes
        if (!updatedProduct.name || !updatedProduct.price || !updatedProduct.quantity) {
          throw new Error("Faltan campos obligatorios como nombre, precio o cantidad.");
        }

        // Verificar si el username se obtuvo correctamente
        console.log("Username:", username);

        // Crear un objeto FormData para enviar datos de la forma correcta
        const formData = new FormData();
        formData.append("name", updatedProduct.name);
        formData.append("description", updatedProduct.description);
        formData.append("price", updatedProduct.price);
        formData.append("quantity", updatedProduct.quantity);

        // Si existe una imagen nueva, agregarla al FormData
        if (updatedProduct.imagen) {
          formData.append("file", updatedProduct.imagen);
        }

        // Añadir el username
        formData.append("username", username);

        const url = `http://localhost:8000/store/products/${updatedProduct.id}?username=${username}`;
        console.log("Enviando datos a:", url);

        // Enviar la solicitud PUT con FormData
        const response = await axios.put(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",  // Asegúrate de que sea 'multipart/form-data'
          },
          withCredentials: true,  // Para mantener las credenciales si es necesario
        });

        console.log("Respuesta del servidor:", response);

        if (response.status === 200) {
          alert("Producto actualizado exitosamente");
          await this.fetchProducts(); // Refrescar productos después de guardar
        } else {
          throw new Error(response.data.msg || "Error al actualizar el producto");
        }
      } catch (error) {
        console.error("Error al guardar producto:", error.response?.data || error.message);
        if (error.response?.data?.detail) {
          console.log("Detalles del error:", error.response.data.detail);
        }
        alert("Hubo un error al guardar el producto. Revisa la consola para más detalles.");
      }
    },

    /**
     * Delete a product from the server and update the state.
     * @param {string} id - The product id to delete.
     */
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
  }
});
