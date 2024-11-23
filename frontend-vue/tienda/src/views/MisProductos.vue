<template>
  <v-container fluid>
    <Navbar />
    <v-divider class="my-6" />

    <!-- Título más pequeño -->
    <v-row justify="center" class="mb-1">
  <v-col cols="4" md="2" lg="6" class="text-center">
    <div
      class="py-2 px-6 rounded-lg elevation-2"
      style="background-color: #f5f5f5;"
    >
      <v-icon size="36" color="#1976d2" class="mb-1">mdi-cart-outline</v-icon>
      <h2
        class="text-h4 font-weight-bold mb-1"
        style="color: #1976d2; text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);"
      >
        Mis productos en venta
      </h2>
      <p class="text-subtitle-2" style="color: #546e7a;">
        Administra y visualiza los productos que tienes en oferta.
      </p>
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
            <v-chip
              :color="product.status === 'Vendido' ? 'red' : 'green'"
              dark
              small
            >
              {{ product.status }}
            </v-chip>
          </v-card-text>
          <!-- Botones separados en extremos -->
          <v-card-actions class="d-flex justify-space-between">
            <v-btn text color="primary" @click="editProduct(product)"
              >Editar</v-btn
            >
            <v-btn text color="red" @click="deleteProduct(product.id)"
              >Eliminar</v-btn
            >
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
              v-model="editedProduct.name"
              label="Nombre"
              required
              outlined
              dense
            />
            <v-textarea
              v-model="editedProduct.description"
              label="Descripción"
              required
              outlined
              dense
            />
            <v-text-field
              v-model="editedProduct.price"
              label="Precio"
              type="number"
              required
              outlined
              dense
            />
            <v-text-field
              v-model="editedProduct.quantity"
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

export default {
  components: { Navbar },
  setup() {
    const store = useProductManagerStore();
    const { products, editedProduct, dialog } = store;

    const editProduct = (product) => {
      store.setEditedProduct(product);
    };

    const updateProductImage = (file) => {
      if (file && file instanceof File) {
        store.editedProduct.file = file;
      }
    };

    const saveChanges = async () => {
      await store.saveProduct();
      dialog.value = false;
    };

    const deleteProduct = async (id) => {
      await store.deleteProduct(id);
    };

    store.fetchProducts();

    return {
      products,
      editedProduct,
      dialog,
      editProduct,
      updateProductImage,
      saveChanges,
      deleteProduct,
    };
  },
};
</script>

<style scoped>
/* Reducido el tamaño de los márgenes */
.mb-4 {
  margin-bottom: 16px !important;
}

/* Título más pequeño */
.subtitle-1 {
  font-size: 1.6rem !important;
}

/* Botones bien espaciados */
.v-card-actions {
  padding-left: 16px;
  padding-right: 16px;
}
</style>
