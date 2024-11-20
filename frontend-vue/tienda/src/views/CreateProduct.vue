<template>
  <v-app>
    <Navbar />
    <v-container class="mt-6" max-width="600">
      <v-row justify="center">
        <v-col cols="12" sm="10" md="8">
          <v-card elevation="6" rounded class="pa-5">
            <v-card-title class="headline text-center">Crear Nuevo Producto</v-card-title>
            <v-card-subtitle class="text-center mb-4">
              Completa los detalles del producto para agregarlo a la tienda.
            </v-card-subtitle>

            <v-form @submit.prevent="submitProduct" v-model="valid">
              <v-card-text>
                <!-- Nombre del Producto -->
                <v-text-field
                  v-model="product.name"
                  label="Nombre del Producto"
                  required
                  :rules="[rules.required]"
                  dense
                  class="mb-5"
                ></v-text-field>

                <!-- Descripción del Producto -->
                <v-textarea
                  v-model="product.description"
                  label="Descripción"
                  required
                  :rules="[rules.required]"
                  dense
                  class="mb-5"
                  rows="3"
                ></v-textarea>

                <!-- Precio del Producto -->
                <v-text-field
                  v-model="product.price"
                  label="Precio"
                  type="number"
                  min="0"
                  required
                  :rules="[rules.required, rules.positiveNumber]"
                  dense
                  class="mb-5"
                ></v-text-field>

                <!-- Cantidad del Producto -->
                <v-text-field
                  v-model="product.quantity"
                  label="Cantidad"
                  type="number"
                  min="0"
                  required
                  :rules="[rules.required, rules.positiveNumber]"
                  dense
                  class="mb-5"
                ></v-text-field>

                <!-- Imagen del Producto -->
                <v-file-input
                  v-model="product.image"
                  label="Selecciona una Imagen"
                  accept="image/*"
                  required
                  :rules="[rules.required]"
                  dense
                  class="mb-5"
                ></v-file-input>
              </v-card-text>

              <!-- Botón Crear Producto -->
              <v-card-actions class="justify-center">
                <v-btn
                  :loading="isLoading"
                  :disabled="isLoading || !valid"
                  type="submit"
                  color="primary"
                  large
                >
                  Crear Producto
                </v-btn>
              </v-card-actions>
            </v-form>

            <!-- Mensaje de éxito o error -->
            <v-alert v-if="message" :type="message.type" dismissible>
              {{ message.text }}
            </v-alert>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { ref, computed } from 'vue';
import { useProductCreateStore } from '@/stores/useProductCreateStore';  // Importa el store adecuado
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'CreateProduct',
  components: {
    Navbar,
  },
  setup() {
    const productStore = useProductCreateStore();  // Usa el store adecuado

    const product = ref({
      name: '',
      description: '',
      price: 0,
      quantity: 0,
      image: null,
    });

    const valid = ref(false);
    const rules = {
      required: (value) => !!value || 'Este campo es requerido.',
      positiveNumber: (value) => value > 0 || 'Debe ser un número positivo.',
    };

    const isLoading = computed(() => productStore.isLoading);  // Accede al estado de carga del store
    const message = computed(() => productStore.message);  // Accede al mensaje del store

    const submitProduct = async () => {
      const isSuccess = await productStore.createProduct(product.value);  // Llama la acción de crear producto
      if (isSuccess) {
        resetForm();
      }
    };

    const resetForm = () => {
      product.value = {
        name: '',
        description: '',
        price: 0,
        quantity: 0,
        image: null,
      };
    };

    return {
      product,
      valid,
      rules,
      isLoading,
      message,
      submitProduct,
    };
  },
};
</script>

<style scoped>
.v-btn {
  text-transform: none;
  font-weight: 500;
}

.v-card {
  transition: box-shadow 0.3s ease;
}

.v-card:hover {
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.v-alert {
  margin-top: 20px;
}

.text-center {
  text-align: center;
}

.mb-5 {
  margin-bottom: 1.5rem; /* Mayor espaciado entre los campos */
}

.mt-6 {
  margin-top: 4rem; /* Margen superior ajustado */
}

.pa-5 {
  padding: 24px; /* Padding adecuado para la tarjeta */
}

.v-container {
  max-width: 600px; /* Contenedor más ancho para un diseño equilibrado */
}

.v-row {
  justify-content: center;
}

.v-col {
  display: flex;
  justify-content: center;
}

.v-card-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

.v-card-subtitle {
  font-size: 1.1rem;
  color: #757575;
}

.v-text-field,
.v-textarea,
.v-file-input {
  font-size: 1rem; /* Tamaño de fuente más adecuado */
}

.v-btn {
  font-size: 1.1rem; /* Botón con tamaño adecuado */
  padding: 12px 24px; /* Padding para un botón más cómodo */
  border-radius: 8px; /* Bordes redondeados */
}
</style>
