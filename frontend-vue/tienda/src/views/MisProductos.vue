<template>
  <v-container fluid>
    <Navbar />
    <v-divider class="my-6" />

    <v-row v-if="loading" justify="center" class="my-6">
      <v-col cols="12" class="text-center">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </v-col>
    </v-row>

    <v-row justify="center" class="mb-1">
      <v-col cols="12" md="8" lg="6" class="text-center">
        <div class="py-2 px-6 rounded-lg elevation-2" style="background-color: #f5f5f5;">
          <v-icon size="36" color="#1976d2" class="mb-1">mdi-cart-outline</v-icon>
          <h2 class="text-h4 font-weight-bold mb-1" style="color: #1976d2;">Mis productos en venta</h2>
          <p class="text-subtitle-2" style="color: #546e7a;">Administra y visualiza tus productos.</p>
        </div>
      </v-col>
    </v-row>

    <v-row>
      <v-col v-for="product in products" :key="product.id" cols="12" sm="6" md="3">
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
            <v-btn text color="red" @click="confirmDeleteProduct(product.id)">Eliminar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>Editar Producto</v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field v-model="localEditedProduct.name" label="Nombre" required outlined dense />
            <v-textarea v-model="localEditedProduct.description" label="Descripción" required outlined dense />
            <v-text-field v-model="localEditedProduct.price" label="Precio" type="number" required outlined dense />
            <v-text-field v-model="localEditedProduct.quantity" label="Cantidad" type="number" required outlined dense />
            <v-file-input label="Cambiar Imagen" @change="updateProductImage" accept="image/*" outlined dense />
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
import { ref, onMounted } from "vue";
import Swal from "sweetalert2";

export default {
  components: { Navbar },
  setup() {
    const store = useProductManagerStore();
    const { products, loading, fetchProducts, saveProduct, deleteProduct } = store;

    const dialog = ref(false);
    const localEditedProduct = ref({});

    // Cargar productos al inicio
    onMounted(async () => {
      await fetchProducts();
    });

    const openEditDialog = (product) => {
      localEditedProduct.value = { ...product };
      dialog.value = true;
    };

    const updateProductImage = (file) => {
      if (file && file instanceof File) {
        localEditedProduct.value.imagen = file;
      }
    };

    const saveChanges = async () => {
      try {
        await saveProduct(localEditedProduct.value);
        dialog.value = false;
      } catch (error) {
        console.error("Error al guardar los cambios:", error);
      }
    };

    const confirmDeleteProduct = (id) => {
      Swal.fire({
        title: "¿Estás seguro?",
        text: "Este producto será eliminado permanentemente.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
      }).then(async (result) => {
        if (result.isConfirmed) {
          await deleteProduct(id);
        }
      });
    };

    return {
      products,
      dialog,
      localEditedProduct,
      openEditDialog,
      saveChanges,
      confirmDeleteProduct,
      loading,
    };
  },
};
</script>
