<template>
  <v-app>
    <Navbar />
    
    <v-container class="mt-5" max-width="600">
      <v-row>
        <v-col cols="12">
          <v-card>
            <v-card-title>
              <span class="headline">Crear Nuevo Producto</span>
            </v-card-title>
            
            <v-card-subtitle>
              Rellena los detalles del producto y haz clic en "Crear Producto" para agregarlo a la tienda.
            </v-card-subtitle>

            <v-form @submit.prevent="submitProduct" v-model="valid">
              <v-card-text>
                <v-text-field
                  v-model="product.name"
                  label="Nombre del Producto"
                  required
                  :rules="[rules.required]"
                ></v-text-field>
                
                <v-textarea
                  v-model="product.description"
                  label="Descripción"
                  required
                  :rules="[rules.required]"
                ></v-textarea>
                
                <v-text-field
                  v-model="product.price"
                  label="Precio"
                  type="number"
                  min="0"
                  required
                  :rules="[rules.required, rules.positiveNumber]"
                ></v-text-field>
                
                <v-text-field
                  v-model="product.quantity"
                  label="Cantidad"
                  type="number"
                  min="0"
                  required
                  :rules="[rules.required, rules.positiveNumber]"
                ></v-text-field>

                <!-- Campo para seleccionar imagen -->
                <v-file-input
                  v-model="product.image"
                  label="Selecciona una Imagen"
                  accept="image/*"
                  required
                  :rules="[rules.required]"
                ></v-file-input>

              </v-card-text>

              <v-card-actions>
                <v-btn
                  :loading="isLoading"
                  :disabled="isLoading || !valid"
                  type="submit"
                  color="primary"
                >
                  Crear Producto
                </v-btn>
              </v-card-actions>

              <v-alert v-if="message" :type="message.type" dismissible>
                {{ message.text }}
              </v-alert>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios';
import Navbar from '../components/Navbar.vue';  // Importar el componente Navbar

export default {
  components: {
    Navbar
  },
  data() {
    return {
      product: {
        name: '',
        description: '',
        price: 0,
        quantity: 0,
        image: null,  // Nuevo campo para la imagen
      },
      isLoading: false,
      message: null,
      valid: false,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        positiveNumber: value => value > 0 || 'Debe ser un número positivo.',
      },
    };
  },
  methods: {
    async submitProduct() {
      this.isLoading = true;
      try {
        const token = localStorage.getItem('token');
        
        if (!token) {
          throw new Error("No se encontró el token de autenticación.");
        }

        // Obtener el username del token o de otro lugar
        const username = localStorage.getItem('username');
        if (!username) {
          throw new Error("No se encontró el username.");
        }

        // Crear un FormData para enviar los datos incluyendo la imagen
        const formData = new FormData();
        formData.append('name', this.product.name);
        formData.append('description', this.product.description);
        formData.append('price', this.product.price);
        formData.append('quantity', this.product.quantity);
        formData.append('image', this.product.image);  // Agregar imagen al FormData

        const response = await axios.post(`http://localhost:8000/store/create?username=${username}`, formData, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'multipart/form-data',  // Especificar que se envía un formulario con archivos
          }
        });

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
          image: null,
        };
      } catch (error) {
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
/* Estilos personalizados para mejorar la vista */
.v-btn {
  width: 100%;
}

.v-card {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.v-card-title {
  text-align: center;
  font-weight: bold;
}

.v-text-field, .v-textarea, .v-file-input {
  margin-bottom: 20px;
}

.v-alert {
  margin-top: 20px;
}

@media (max-width: 600px) {
  .v-btn {
    width: 100%;
  }
}
</style>
