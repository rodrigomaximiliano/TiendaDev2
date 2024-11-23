<template>
    <v-container class="mt-5">
      <v-row justify="center" align="start">
        <v-col v-for="(item, index) in cards" :key="index" cols="12" md="4">
          <v-card class="pa-4" :style="cardStyles">
            <!-- Parte superior pintada con un color suave -->
            <div class="header" :style="headerStyles"></div>
  
            <div class="text-content">
              <!-- Título con estilo similar -->
              <v-card-title class="mt-5 text-h5 font-weight-semibold" :style="titleStyles">
                {{ item.title }}
              </v-card-title>
              <!-- Texto con estilo similar -->
              <v-card-text class="mt-4 text-body-1" :style="textStyles">
                {{ item.text }}
              </v-card-text>
            </div>
          </v-card>
        </v-col>
      </v-row>
  
      <!-- Estadísticas -->
      <v-row justify="center" align="center" class="mt-4">
        <v-col v-for="(stat, index) in stats" :key="index" cols="12" sm="6" md="3">
          <v-card class="d-flex justify-center align-center pa-4" :style="statCardStyles">
            <div class="flex flex-col items-center">
              <!-- Número con estilo semibold -->
              <div class="text-h3 font-weight-semibold text-[#377DB6]">
                {{ getAnimatedNumber(stat.number) }}<span class="ml-[-5px]">{{ stat.symbol }}</span>
              </div>
              <!-- Etiqueta con estilo semibold -->
              <h3 class="text-h6 font-weight-semibold text-[#212121]">{{ stat.label }}</h3>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  
  export default {
    setup() {
      const cards = [
        {
          title: "¿Quiénes somos?",
          text: "Somos una plataforma de ventas en línea que vende y permite vender a personas y negocios vender sus productos fácilmente."
        },
        {
          title: "¿Dónde estamos?",
          text: "Nuestra sede está en Corrientes, Argentina pero nuestra plataforma está disponible para vendedores de todo el mundo."
        },
        {
          title: "¿Cómo lo hacemos?",
          text: "Con una interfaz fácil de usar y funciones sólidas, lo ayudamos a enumerar, administrar y vender sus productos con facilidad."
        }
      ];
  
      const stats = [
        {
          number: 200,
          symbol: '+',
          label: 'Productos entregados con éxito'
        },
        {
          number: 97,
          symbol: '%',
          label: 'Satisfacción excepcional de nuestros clientes'
        },
        {
          number: 70,
          symbol: '+',
          label: 'Empleados trabajando en todo Argentina'
        },
        {
          number: 40,
          symbol: '+',
          label: 'Clientes confían en nuestro trabajo'
        }
      ];
  
      const animatedNumbers = ref({});
  
      const startCounter = () => {
        stats.forEach(stat => {
          let currentValue = 0;
          const targetValue = stat.number;
          const step = Math.ceil(targetValue / 100); // Incrementar en pasos
  
          // Función para incrementar los números
          const updateNumber = () => {
            currentValue += step;
            if (currentValue >= targetValue) {
              currentValue = targetValue; // Asegurarse de no exceder el número objetivo
              clearInterval(interval); // Detener la animación
            }
            animatedNumbers.value[stat.number] = currentValue; // Actualizar el número en el objeto reactivo
          };
  
          // Intervalo para actualizar el número
          const interval = setInterval(updateNumber, 10); // Intervalo de actualización
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
        animatedNumbers,
        startCounter,
        getAnimatedNumber
      };
    }
  };
  </script>
  
  <style scoped>
  .v-card {
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .v-card:hover {
    transform: scale(1.05);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
  }
  </style>
  