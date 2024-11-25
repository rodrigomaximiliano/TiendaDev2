<template>
  <v-container class="py-2">
    <Imagenban />
    
    <v-row
      justify="center"
      align="center"
      class="header-row"
      style="background: linear-gradient(135deg, #5d87d4 0%, #00c6ff 100%); padding: 2px 6px; border-radius: 4px;"
    >
      <v-col cols="12" class="text-center">
        <h1 class="header-title">Servicios</h1>
        <p class="header-subtitle">
          Sabemos que cada vendedor y comprador tiene necesidades únicas. Por eso, nuestros servicios están pensados para 
          ayudarte a optimizar tu experiencia de compra y venta.
        </p>
      </v-col>
    </v-row>

    <!-- Tarjetas -->
    <v-row justify="center" dense>
      <v-col
        cols="8"
        md="4"
        lg="4"
        v-for="(service, index) in services"
        :key="index"
        class="d-flex justify-center my-2"
      >
        <div class="flip-card">
          <div class="flip-card-inner">
            <!-- Lado Frontal -->
            <div class="flip-card-front rounded-lg bg-white shadow-card p-4">
              <div class="flex flex-col items-center gap-4">
                <v-icon :size="60" class="icon-color">{{ service.icon }}</v-icon>
                <h4 class="text-center text-h8 font-weight-bold text-primary">
                  {{ service.title }}
                </h4>
                <p class="text-center text-body-1 text-secondary">
                  {{ service.description }}
                </p>
              </div>
            </div>

            <!-- Lado Trasero -->
            <div class="flip-card-back rounded-lg bg-lightblue text-white p-4">
              <div class="flex flex-col items-center gap-4">
                <v-icon :size="60" class="icon-color">{{ service.icon }}</v-icon>
                <h4 class="text-center text-h8 font-weight-bold">
                  {{ service.title }}
                </h4>
                <p class="text-center text-body-1">
                  {{ service.details }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Imagenban from './Imagenban.vue'; 

export default {
  name: "ServiceCards",
  components: {
    Imagenban, 
  },
  data() {
    return {
      services: [
        {
          icon: "mdi-cellphone",
          title: "Aplicación Móvil",
          description:
            "Con nuestra app móvil, tanto compradores como vendedores pueden acceder a la tienda en cualquier momento y lugar.",
          details:
            "Realiza compras, sigue tus pedidos, vende productos y gestiona tu tienda de forma sencilla y segura desde tu dispositivo móvil.",
        },
        {
          icon: "mdi-palette",
          title: "Diseño UX/UI",
          description:
            "Nuestro equipo diseña interfaces atractivas y fáciles de usar que mejoran la experiencia de compra y venta.",
          details:
            "Creamos interfaces intuitivas para garantizar una navegación rápida, agradable y sin complicaciones para compradores y vendedores.",
        },
        {
          icon: "mdi-cart",
          title: "Tienda en Línea",
          description:
            "Nuestra plataforma permite a los usuarios comprar productos de manera sencilla y también vender sus propios artículos.",
          details:
            "Con herramientas avanzadas, puedes gestionar tu tienda personal, recibir pedidos y ampliar tu mercado mientras disfrutas de una experiencia de compra intuitiva y confiable.",
        },
        {
          icon: "mdi-store",
          title: "Marketplace",
          description:
            "Un espacio donde compradores y vendedores se conectan fácilmente para intercambiar productos.",
          details:
            "Crea tu perfil de vendedor, publica tus productos y accede a una audiencia global, mientras disfrutas de la comodidad de un ecosistema seguro y eficiente.",
        },
        {
          icon: "mdi-cloud",
          title: "Soluciones",
          description:
            "Gestionamos tus operaciones comerciales en la nube de forma sencilla, asegurando que la tienda esté siempre disponible y segura.",
          details:
            "Nuestros expertos en la nube garantizan un entorno seguro y escalable para que tu negocio crezca sin preocupaciones.",
        },
        {
          icon: "mdi-security",
          title: "Seguridad",
          description:
            "Protegemos tus activos digitales y los datos de tus clientes con nuestros servicios de seguridad avanzados.",
          details:
            "Ofrecemos protección contra amenazas, asegurando que la información de la tienda y clientes esté siempre segura.",
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Estilos específicos para las tarjetas */
.flip-card {
  perspective: 1000px;
  width: 100%;
  max-width: 320px;
  height: 350px;
  box-shadow: 0px 12px 24px rgba(0, 0, 0, 0.2);
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 8px 8px 0 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px;
  box-shadow: 12px 8px 10px rgba(0, 0, 0, 0.1);
}

.flip-card-front {
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

.flip-card-back {
  background-color: #a2cffe;
  transform: rotateY(180deg);
  color: white;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.15);
}

.shadow-card {
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
}

.icon-color {
  color: #5187f1;
}

.header-title {
  color: white;
  font-size: 1.8rem;
  font-weight: 700;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.6);
}

.header-subtitle {
  color: white;
  font-size: 1.1rem;
  margin-top: 4px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
}

.header-row {
  margin-top: 0px;
  margin-bottom: 12px;
}

.flip-card-front,
.flip-card-back {
  padding: 12px;
}
</style>
