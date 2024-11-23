<template>
  <v-container class="mt-5">
    <!-- Tarjetas informativas -->
    <v-row justify="center" align="start" class="mb-8">
      <v-col
        v-for="(item, index) in cards"
        :key="index"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card class="pa-4 card-hover" elevation="2">
          <!-- Parte superior con gradiente -->
          <div class="header-gradient"></div>

          <!-- Contenido del texto -->
          <v-card-title class="mt-5 text-h5 font-weight-bold text-primary">
            {{ item.title }}
          </v-card-title>
          <v-card-text class="mt-4 text-body-1 text-secondary">
            {{ item.text }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Sección de estadísticas -->
    <v-row justify="center" align="center">
      <v-col
        v-for="(stat, index) in stats"
        :key="index"
        cols="12"
        sm="6"
        md="3"
      >
        <v-card
          class="stat-card d-flex flex-column justify-center align-center"
          elevation="4"
        >
          <div class="stat-number text-h3 font-weight-bold text-info">
            {{ getAnimatedNumber(stat.number) }}
            <span class="text-sm align-top">{{ stat.symbol }}</span>
          </div>
          <div class="stat-label text-h6 font-weight-medium">
            {{ stat.label }}
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const cards = [
      {
        title: "¿Quiénes somos?",
        text: "Somos una plataforma de ventas en línea que vende y permite vender a personas y negocios vender sus productos fácilmente.",
      },
      {
        title: "¿Dónde estamos?",
        text: "Nuestra sede está en Corrientes, Argentina pero nuestra plataforma está disponible para vendedores de todo el mundo.",
      },
      {
        title: "¿Cómo lo hacemos?",
        text: "Con una interfaz fácil de usar y funciones sólidas, lo ayudamos a enumerar, administrar y vender sus productos con facilidad.",
      },
    ];

    const stats = [
      {
        number: 200,
        symbol: "+",
        label: "Productos entregados con éxito",
      },
      {
        number: 97,
        symbol: "%",
        label: "Satisfacción excepcional de nuestros clientes",
      },
      {
        number: 70,
        symbol: "+",
        label: "Empleados trabajando en todo Argentina",
      },
      {
        number: 40,
        symbol: "+",
        label: "Clientes confían en nuestro trabajo",
      },
    ];

    const animatedNumbers = ref({});

    const startCounter = () => {
      stats.forEach((stat) => {
        let currentValue = 0;
        const targetValue = stat.number;
        const step = Math.ceil(targetValue / 50); // Incrementar en pasos más pequeños
        const interval = setInterval(() => {
          currentValue += step;
          if (currentValue >= targetValue) {
            currentValue = targetValue;
            clearInterval(interval);
          }
          animatedNumbers.value[stat.number] = currentValue;
        }, 20);
      });
    };

    const getAnimatedNumber = (number) => {
      return animatedNumbers.value[number] || 0;
    };

    onMounted(() => {
      startCounter();
    });

    return {
      cards,
      stats,
      getAnimatedNumber,
    };
  },
};
</script>

<style scoped>
.card-hover {
  transition: all 0.3s ease-in-out;
  border-radius: 12px;
}
.card-hover:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.header-gradient {
  height: 12px;
  background: linear-gradient(135deg, #5d87d4 0%, #00c6ff 100%);
  border-radius: 6px;
}

.stat-card {
  background: linear-gradient(135deg, #e3f2fd, #bbdefb);
  border-radius: 12px;
  text-align: center;
  transition: transform 0.3s ease;
}
.stat-card:hover {
  transform: scale(1.05);
}

.stat-number {
  color: #1976d2;
}
.stat-label {
  color: #424242;
}
</style>
