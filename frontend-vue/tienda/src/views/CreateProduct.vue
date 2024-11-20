<template>
  <v-app>
    <Navbar />
    <v-container class="mt-6" max-width="800">
      <v-row justify="center">
        <v-col cols="12">
          <v-card elevation="8" rounded class="pa-6">
            <!-- Título -->
            <v-card-title class="headline text-center text-primary">
              Crear Nuevo Producto
            </v-card-title>

            <!-- Subtítulo -->
            <v-card-subtitle class="text-center mb-4 text-muted">
              Completa los detalles del producto para agregarlo a la tienda.
            </v-card-subtitle>

            <!-- Formulario -->
            <v-form @submit.prevent="submitProduct" v-model="valid">
              <v-card-text>
                <v-container fluid>
                  <v-row>
                    <!-- Columna izquierda -->
                    <v-col cols="12" md="6">
                      <!-- Nombre -->
                      <v-text-field
                        v-model="product.name"
                        label="Nombre del Producto"
                        required
                        :rules="[rules.required]"
                        outlined
                        dense
                        class="mb-4"
                      ></v-text-field>

                      <!-- Descripción -->
                      <v-textarea
                        v-model="product.description"
                        label="Descripción"
                        required
                        :rules="[rules.required]"
                        outlined
                        dense
                        rows="4"
                        class="mb-4"
                      ></v-textarea>

                      <!-- Precio -->
                      <v-text-field
                        v-model="product.price"
                        label="Precio ($)"
                        type="number"
                        min="0"
                        required
                        :rules="[rules.required, rules.positiveNumber]"
                        outlined
                        dense
                        class="mb-4"
                      ></v-text-field>
                    </v-col>

                    <!-- Columna derecha -->
                    <v-col cols="12" md="6">
                      <!-- Cantidad -->
                      <v-text-field
                        v-model="product.quantity"
                        label="Cantidad"
                        type="number"
                        min="0"
                        required
                        :rules="[rules.required, rules.positiveNumber]"
                        outlined
                        dense
                        class="mb-4"
                      ></v-text-field>

                      <!-- Imagen -->
                      <v-file-input
                        v-model="product.image"
                        label="Selecciona una Imagen"
                        accept="image/*"
                        required
                        :rules="[rules.required]"
                        outlined
                        dense
                        prepend-icon="mdi-image"
                        class="mb-4"
                      ></v-file-input>

                      <!-- Previsualización -->
                      <v-img
                        v-if="product.image"
                        :src="product.image"
                        max-height="200"
                        contain
                        class="rounded-lg mt-4"
                        alt="Previsualización de la imagen"
                      ></v-img>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <!-- Botón Crear -->
              <v-card-actions class="justify-center">
                <v-btn
                  :loading="isLoading"
                  :disabled="isLoading || !valid"
                  type="submit"
                  color="primary"
                  elevation="2"
                  large
                  class="hover-grow"
                >
                  Crear Producto
                </v-btn>
              </v-card-actions>
            </v-form>

            <!-- Mensaje de éxito o error -->
            <v-alert 
              v-if="message" 
              :type="message.type" 
              dismissible 
              class="mt-4"
            >
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
import { useProductCreateStore } from '@/stores/useProductCreateStore'; // Store
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'CreateProduct',
  components: {
    Navbar,
  },
  setup() {
    const productStore = useProductCreateStore();

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

    const isLoading = computed(() => productStore.isLoading);
    const message = computed(() => productStore.message);

    const submitProduct = async () => {
      const isSuccess = await productStore.createProduct(product.value);
      if (isSuccess) resetForm();
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
/* Margen superior para separar del Navbar */
.mt-6 {
  margin-top: 3rem;
}

/* Sombra adicional para tarjetas */
.v-card {
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.v-card:hover {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  transform: translateY(-3px);
}

/* Efecto de crecimiento para botones */
.hover-grow {
  transition: transform 0.2s ease;
}

.hover-grow:hover {
  transform: scale(1.05);
}

/* Espaciado entre elementos */
.mb-4 {
  margin-bottom: 1.5rem;
}

.mt-4 {
  margin-top: 1rem;
}

.text-primary {
  color: #1976d2;
}

.text-muted {
  color: #757575;
}
</style>
