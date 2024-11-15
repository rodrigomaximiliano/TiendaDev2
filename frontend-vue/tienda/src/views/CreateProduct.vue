<template>
  <div class="create-product">
    <h2>Crear Nuevo Producto</h2>
    
    <form @submit.prevent="submitProduct">
      <div class="form-group">
        <label for="name">Nombre del Producto</label>
        <input type="text" id="name" v-model="product.name" required />
      </div>

      <div class="form-group">
        <label for="description">Descripción</label>
        <textarea id="description" v-model="product.description" required></textarea>
      </div>

      <div class="form-group">
        <label for="price">Precio</label>
        <input type="number" id="price" v-model="product.price" min="0" required />
      </div>

      <div class="form-group">
        <label for="quantity">Cantidad</label>
        <input type="number" id="quantity" v-model="product.quantity" min="0" required />
      </div>

      <button type="submit" :disabled="isLoading">Crear Producto</button>
    </form>

    <div v-if="message" :class="message.type">
      <p>{{ message.text }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      product: {
        name: '',
        description: '',
        price: 0,
        quantity: 0,
      },
      isLoading: false,
      message: null,
    };
  },
  methods: {
    async submitProduct() {
      this.isLoading = true;
      try {
        // Obtener el token de localStorage
        const token = localStorage.getItem('token');
        
        if (!token) {
          throw new Error("No se encontró el token de autenticación.");
        }

        // Enviar la solicitud POST al servidor, solo con el token en los encabezados
        const response = await axios.post('http://localhost:8000/store/create', this.product, {
          headers: {
            'Authorization': `Bearer ${token}`,  // Enviar el token en los encabezados
          }
        });

        // Mostrar mensaje de éxito
        this.message = {
          type: 'success',
          text: response.data.msg || 'Producto creado exitosamente.',
        };

        // Resetear el formulario
        this.product = {
          name: '',
          description: '',
          price: 0,
          quantity: 0,
        };
      } catch (error) {
        // Manejo de errores
        this.message = {
          type: 'error',
          text: error.response?.data?.detail || error.message || 'Hubo un error al crear el producto.',
        };
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped>
.create-product {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.create-product h2 {
  text-align: center;
}

.form-group {
  margin-bottom: 1em;
}

.form-group label {
  display: block;
  margin-bottom: 0.5em;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.8em;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 1em;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.2em;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
}

.success {
  color: green;
}

.error {
  color: red;
}
</style>
