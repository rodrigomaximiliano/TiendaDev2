<template>
  <v-container fluid>
    <Navbar />
    <v-divider class="my-6" />

    <!-- Título -->
    <v-row justify="center" class="mb-1">
      <v-col cols="12" md="8" lg="6" class="text-center">
        <div class="py-2 px-6 rounded-lg elevation-2" style="background-color: #f5f5f5;">
          <v-icon size="36" color="#1976d2" class="mb-1">mdi-cart-outline</v-icon>
          <h2 class="text-h4 font-weight-bold mb-1" style="color: #1976d2;">Mis productos en venta</h2>
          <p class="text-subtitle-2" style="color: #546e7a;">Administra y visualiza tus productos.</p>
        </div>
      </v-col>
    </v-row>

    <!-- Listado de productos -->
    <v-row>
      <v-col
        v-for="product in products"
        :key="product.id"
        cols="12"
        sm="6"
        md="3"
      >
        <v-card outlined class="elevation-2">
          <v-img
            :src="product.imagen ? `http://localhost:8000${product.imagen}` : 'https://via.placeholder.com/300x200'"
            alt="Imagen del producto"
            height="200px"
          />
          <v-card-title class="text-h6">{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.description }}</v-card-subtitle>
          <v-card-text>
            <div><strong>Precio:</strong> ${{ product.price }}</div>
            <div><strong>Cantidad:</strong> {{ product.quantity }}</div>
            <v-chip :color="product.status === 'Vendido' ? 'red' : 'green'" dark small>
              {{ product.status }}
            </v-chip>
          </v-card-text>
          <v-card-actions class="d-flex justify-space-between">
            <v-btn text color="primary" @click="openEditDialog(product)">Editar</v-btn>
            <v-btn text color="red" @click="deleteProduct(product.id)">Eliminar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- Diálogo para editar producto -->
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>Editar Producto</v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field
              v-model="localEditedProduct.name"
              label="Nombre"
              required
              outlined
              dense
            />
            <v-textarea
              v-model="localEditedProduct.description"
              label="Descripción"
              required
              outlined
              dense
            />
            <v-text-field
              v-model="localEditedProduct.price"
              label="Precio"
              type="number"
              required
              outlined
              dense
            />
            <v-text-field
              v-model="localEditedProduct.quantity"
              label="Cantidad"
              type="number"
              required
              outlined
              dense
            />
            <v-file-input
              label="Cambiar Imagen"
              @change="updateProductImage"
              accept="image/*"
              outlined
              dense
            />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="dialog = false">Cancelar</v-btn>
          <v-btn text color="primary" @click="saveChanges">Guardar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import { useProductManagerStore } from "@/stores/productManagerStore";
import { ref } from "vue";

export default {
  components: { Navbar },
  setup() {
    const store = useProductManagerStore();
    const { products, setEditedProduct } = store;

    const dialog = ref(false); // Local dialog control
    const localEditedProduct = ref({}); // Local copy of edited product

    // Abre el diálogo y configura el producto a editar
    const openEditDialog = (product) => {
      console.log("Editando producto:", product); // Depuración
      setEditedProduct(product); // Actualiza el store
      localEditedProduct.value = { ...product }; // Copia local del producto
      dialog.value = true; // Abre el diálogo
    };

    // Actualizar la imagen del producto
    const updateProductImage = (file) => {
      if (file && file instanceof File) {
        localEditedProduct.value.imagen = file; // Guardar el archivo seleccionado en la propiedad imagen
      }
    };

    // Guardar cambios del producto
    const saveChanges = async () => {
      try {
        await store.saveProduct(localEditedProduct.value); // Pasa los datos al store
        dialog.value = false; // Cerrar el diálogo
      } catch (error) {
        console.error("Error al guardar los cambios:", error);
      }
    };

    // Eliminar producto
    const deleteProduct = async (id) => {
      await store.deleteProduct(id);
    };

    store.fetchProducts();

    return {
      products,
      dialog,
      localEditedProduct,
      openEditDialog,
      updateProductImage,
      saveChanges,
      deleteProduct,
    };
  },
};
</script>

<style scoped>
.v-card-actions {
  padding-left: 16px;
  padding-right: 16px;
}
</style>
