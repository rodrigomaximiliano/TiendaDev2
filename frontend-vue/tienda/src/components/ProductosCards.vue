<template>
  <v-container>
    <!-- Encabezado -->
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
        <h1 class="header-title">¡Descubre nuestros Productos!</h1>
        <p class="header-subtitle">
          ¿Tenés productos para vender? Registrate a nuestra plataforma y empieza a vender hoy mismo.
        </p>
      </v-col>
    </v-row>

    <!-- Productos -->
    <v-row justify="center" align="start" class="g-4 mt-6">
      <v-col
        v-for="product in limitedProducts"
        :key="product.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card class="product-card" elevation="4">
          <!-- Imagen -->
          <v-img
            :src="product.imagen ? `http://localhost:8000${product.imagen}` : 'https://via.placeholder.com/300x200'"
            height="200"
            aspect-ratio="1.75"
            :alt="product.name"
            @error="imageError"
            class="product-image"
          />

          <!-- Detalles -->
          <v-card-subtitle class="mt-3 text-center">
            <span class="price-tag">$ {{ formatPrice(product.price) }}</span>
            <v-chip v-if="product.isNew" color="green" small class="ml-2">Nuevo</v-chip>
            <v-chip v-if="product.isOnSale" color="red" small class="ml-2">En Oferta</v-chip>
          </v-card-subtitle>
          <v-card-text class="text-truncate text-center px-2" title="product.description">
            {{ product.description }}
          </v-card-text>

          <!-- Acción -->
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
import { ref, computed, onMounted } from "vue";

export default {
  name: "ProductosCards",
  setup() {
    const store = useProductStore();

    // Obtener productos
    const fetchProducts = () => {
      store.fetchProducts();
    };

    // Productos limitados
    const limitedProducts = computed(() => store.products.slice(0, 4));

    // Agregar al carrito
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

    // Manejo de error de imagen
    const imageError = (event) => {
      event.target.src = "https://via.placeholder.com/300x200";
    };

    onMounted(() => {
      fetchProducts();
    });

    return {
      limitedProducts,
      addToCart,
      formatPrice,
      imageError,
    };
  },
};
</script>

<style scoped>

.header-title {
  color: white;
  font-size: 2.5rem;
  font-weight: 700;
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

/* Tarjetas */
.product-card {
  position: relative;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.3s ease;
  border-radius: 8px;
  border-color: rgba(0, 0, 0, 0.7);
  background: whitesmoke;
  
}

.product-card:hover {
  transform: scale(1.05);
  box-shadow: 12px 12px 24px rgba(0, 0, 0, 0.2);
}

.product-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 200%;
  height: 100%;
  background: linear-gradient(90deg, rgba(29, 24, 24, 0) 0%, rgba(255, 255, 255, 0.4) 50%, rgba(255, 255, 255, 0) 100%);
  transition: all 0.4s ease;
  transform: skewX(-20deg);
  z-index: 2;
}

.product-card:hover::before {
  left: 100%;
  transition: all 0.4s ease;
}

.product-image {
  border-radius: 8px 8px 0 0;
  object-fit: cover;
}

/* Precio */
.price-tag {
  font-weight: bold;
  color: #29c0fc;
}
</style>
