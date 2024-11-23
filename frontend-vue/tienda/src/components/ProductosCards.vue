<template>
  <v-container>
    <!-- Encabezado estilizado -->
    <v-row
      justify="center"
      align="center"
      class="header-row"
      style="background: linear-gradient(135deg, #5d87d4 0%, #00c6ff 100%); padding: 2px 10px; border-radius: 8px;"
    >
      <v-col cols="12" class="text-center">
        <v-icon size="8" color="white" class="mb-2 animate-icon">
          mdi-star
        </v-icon>
        <!-- Título con estilo semibold -->
        <h1 class="header-title">
          ¡Descubre nuestros Productos!
        </h1>
        <!-- Subtítulo con estilo normal -->
        <p class="header-subtitle">
          ¿Tenés productos para vender? Registrate a nuestra plataforma y empieza a vender hoy mismo.
        </p>
      </v-col>
    </v-row>

    <!-- Mostrar productos como tarjetas -->
    <v-row justify="center" align="start" class="g-4 mt-6">
      <v-col
        v-for="product in products"
        :key="product.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card class="product-card" elevation="4">
          <!-- Imagen del producto con texto encima -->
          <v-img
            :src="product.imagen ? `http://localhost:8000${product.imagen}` : 'https://via.placeholder.com/300x200'"
            height="200"
            aspect-ratio="1.75"
            :alt="product.name"
            @error="imageError"
            class="product-image"
          >
            <v-row
              class="fill-height ma-0"
              align="end"
              justify="center"
              style="background: rgba(0, 0, 0, 0.5); color: white; border-radius: 4px 4px 0 0;"
            >
              <span class="headline px-2">{{ product.name }}</span>
            </v-row>
          </v-img>

          <!-- Detalles del producto -->
          <v-card-subtitle class="mt-3 text-center">
            <span class="price-tag">$ {{ formatPrice(product.price) }}</span>
            <v-chip v-if="product.isNew" color="green" small class="ml-2">
              Nuevo
            </v-chip>
            <v-chip v-if="product.isOnSale" color="red" small class="ml-2">
              En Oferta
            </v-chip>
          </v-card-subtitle>

          <v-card-text class="text-truncate text-center px-2" title="product.description">
            {{ product.description }}
          </v-card-text>

          <!-- Botón de acción -->
          <v-card-actions class="d-flex justify-center">
            <v-btn
              :disabled="product.stock === 0"
              color="primary"
              block
              @click="addToCart(product.id)"
            >
              Agregar al Carrito
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useProductStore } from "@/stores/useProductStore";
import { ref, onMounted } from "vue";

export default {
  name: "ProductosCards",
  setup() {
    const store = useProductStore();
    const currentPage = ref(store.page);
    const limit = store.limit;

    // Obtener productos
    const fetchProducts = () => {
      store.fetchProducts(currentPage.value, limit);
    };

    // Agregar producto al carrito
    const addToCart = async (productId) => {
      try {
        const msg = await store.addToCart(productId);
        alert(msg || "Producto agregado al carrito");
      } catch (error) {
        console.error("Error al agregar al carrito:", error);
        alert("Error al agregar el producto al carrito");
      }
    };

    // Formatear precio
    const formatPrice = (value) => Number(value).toLocaleString("es-ES");

    // Manejar error en imagen
    const imageError = (event) => {
      event.target.src = "https://via.placeholder.com/300x200";
    };

    onMounted(() => {
      fetchProducts();
    });

    return {
      products: store.products,
      currentPage,
      limit,
      fetchProducts,
      addToCart,
      formatPrice,
      imageError,
    };
  },
};
</script>

<style scoped>
/* Encabezado */
.header-title {
  color: white;
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.6);
}

.header-subtitle {
  color: white;
  font-size: 1.2rem;
  margin-top: 8px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
}

.header-row {
  margin-bottom: 40px;
}

.animate-icon {
  animation: bounce 1.5s infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

/* Tarjetas de producto */
.product-card {
  transition: transform 0.2s, box-shadow 0.2s;
  border-radius: 8px;
  background: #f9f9f9;
}

.product-card:hover {
  transform: scale(1.05);
  box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2);
}

.product-image {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  object-fit: cover;
}

.text-truncate {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.price-tag {
  font-weight: bold;
  color: #29c0fc;
}
</style>
