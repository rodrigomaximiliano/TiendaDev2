<template>
  <v-container fluid>
    <Navbar />
    <v-divider class="my-6" />

    <v-row class="my-5">
      <v-col>
        <h2 class="text-center font-weight-bold">Mis Productos</h2>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" md="10" lg="8">
        <v-data-table
          :headers="headers"
          :items="products"
          item-value="id"
          class="elevation-3"
          :search="search"
          item-class="product-row"
        >
          <template v-slot:top>
            <v-toolbar flat color="primary">
              <v-toolbar-title class="white--text">Mis Productos en Venta</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                label="Buscar productos"
                prepend-icon="mdi-magnify"
                clearable
                class="mx-4"
                dense
              ></v-text-field>
            </v-toolbar>
          </template>

          <template v-slot:[`item.status`]="{ item }">
            <v-chip :color="item.status === 'Vendido' ? 'red' : 'green'" dark>
              {{ item.status }}
            </v-chip>
          </template>

          <template v-slot:[`item.description`]="{ item }">
            <v-tooltip bottom>
              <template #activator="{ on }">
                <v-btn color="primary" icon v-on="on" class="ml-4">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
              </template>
              <span>{{ item.description }}</span>
            </v-tooltip>
          </template>

          <template v-slot:[`item.actions`]="{ item }">
            <v-btn color="primary" @click="editProduct(item)" icon>
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn color="red" @click="deleteProduct(item.id)" icon>
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>

    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title class="headline">Editar Producto</v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field
              v-model="editedProduct.name"
              label="Nombre del Producto"
              required
              outlined
            ></v-text-field>
            <v-textarea
              v-model="editedProduct.description"
              label="Descripción"
              required
              outlined
            ></v-textarea>
            <v-text-field
              v-model="editedProduct.price"
              label="Precio"
              type="number"
              required
              outlined
            ></v-text-field>
            <v-text-field
              v-model="editedProduct.quantity"
              label="Cantidad"
              type="number"
              required
              outlined
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
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
import { computed } from 'vue';

export default {
  components: { Navbar },
  setup() {
    const productManagerStore = useProductManagerStore();

    const { products, search, editedProduct, dialog } = productManagerStore;
    const headers = [
      { text: "Nombre", value: "name" },
      { text: "Descripción", value: "description", align: 'start' },
      { text: "Precio", value: "price" },
      { text: "Cantidad", value: "quantity" },
      { text: "Estado", value: "status" },
      { text: "Acciones", value: "actions", sortable: false },
    ];

    const editProduct = (product) => {
      productManagerStore.setEditedProduct(product);
    };

    const saveChanges = () => {
      productManagerStore.saveProduct();
      productManagerStore.dialog = false;
    };

    const deleteProduct = (id) => {
      productManagerStore.deleteProduct(id);
    };

    productManagerStore.fetchProducts();

    return { products, search, editedProduct, dialog, headers, editProduct, saveChanges, deleteProduct };
  }
};
</script>
