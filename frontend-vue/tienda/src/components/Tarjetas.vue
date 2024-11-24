<template>
  <v-container class="text-center">
    <!-- Título de la sección -->
    <h3 class="mb-4 text-[48px] font-semibold">Servicios</h3>
    <p class="mx-auto w-full max-w-[955px] px-4 text-[17px] lg:text-[26px] xl:w-[955px]">
      En nuestra tienda en línea entendemos que cada vendedor y comprador tiene necesidades y objetivos únicos. 
      Por eso, nuestros servicios están diseñados para cubrir todos los aspectos necesarios para optimizar tu experiencia de compra y venta, 
      ayudando a los vendedores a expandir sus negocios y a los compradores a encontrar lo que buscan de manera eficiente.
    </p>

    <!-- Tarjetas de servicios -->
    <v-row class="mt-8" dense>
      <v-col cols="12" md="4" class="d-flex justify-center" v-for="(service, index) in services" :key="index">
        <div class="flip-card">
          <v-card class="flip-card-inner">
            <v-card-title>
              <v-icon class="service-icon" color="primary">{{ service.icon }}</v-icon>
              <span class="headline">{{ service.title }}</span>
            </v-card-title>
            <v-card-text>
              {{ service.description }}
            </v-card-text>
          </v-card>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "ServiceCards",
  data() {
    return {
      services: [
        {
          icon: 'mdi-account-multiple',
          title: 'Ampliación de Vendedores',
          description: ' Si eres un vendedor, puedes aumentar tu visibilidad y alcanzar más clientes con herramientas que te permiten gestionar tu inventario, realizar ventas de manera efectiva y maximizar tu potencial de negocio.'
        },
        {
          icon: 'mdi-web',
          title: 'Desarrollo Web para Tienda Online',
          description: 'Nuestra plataforma está diseñada para ofrecerte una experiencia de compra optimizada para todo tipo de dispositivos.'
        },
        {
          icon: 'mdi-settings',
          title: 'Funcionalidades Personalizadas',
          description: 'Si necesitas características específicas para tu tienda, como opciones avanzadas de pago, gestión de inventario o personalización de productos, podemos integrarlas para mejorar la experiencia de compra y venta.'
        },
        {
          icon: 'mdi-cellphone',
          title: 'Aplicación Móvil',
          description: 'Con nuestra app móvil, tanto compradores como vendedores pueden acceder a la tienda en cualquier momento y lugar, realizar compras, seguir pedidos, vender productos y gestionar su tienda de forma sencilla y segura.'
        },
        {
          icon: 'mdi-palette',
          title: 'Diseño UX/UI',
          description: 'Nuestro equipo se encarga de diseñar interfaces atractivas y fáciles de usar, garantizando que tanto compradores como vendedores disfruten de una experiencia de navegación rápida y agradable.'
        },
        {
          icon: 'mdi-chart-line',
          title: 'Análisis de Datos',
          description: 'Ofrecemos servicios de análisis de datos para ayudarte a mejorar tu negocio, analizando el comportamiento de los compradores, las tendencias de productos y las ventas para tomar decisiones informadas.'
        }
      ]
    };
  }
};
</script>

<style scoped>
.flip-card {
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.service-card {
  width: 100%;
  max-width: 320px;
  margin: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.flip-card-inner .v-card {
  backface-visibility: hidden;
}

.flip-card-inner .v-card:nth-child(2) {
  transform: rotateY(180deg);
}

.service-icon {
  font-size: 48px;
  margin-right: 16px;
}

.headline {
  font-size: 18px;
  font-weight: 600;
}

.v-card-title {
  display: flex;
  align-items: center;
  padding-bottom: 8px;
  font-size: 20px;
}

.v-card-text {
  font-size: 14px;
  color: #555;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .service-card {
    max-width: 100%;
  }
}
</style>
