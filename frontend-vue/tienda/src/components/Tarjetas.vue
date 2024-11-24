<template>
  <v-container class="py-12">
    
    <v-row justify="center" class="mb-16">
  <v-col cols="12" md="10" class="text-center">
    <!-- Título -->
    <h2 class="text-[48px] sm:text-[56px] lg:text-[64px] font-semibold text-gray-800 mb-6">
      Nuestros Servicios
    </h2>
    <!-- Descripción -->
    <p class="text-[18px] sm:text-[20px] lg:text-[24px] text-gray-600 mx-auto max-w-[950px] px-4 opacity-80">
      Sabemos que cada vendedor y comprador tiene necesidades únicas. Por eso, nuestros servicios están pensados para 
      ayudarte a optimizar tu experiencia de compra y venta, ofreciendo herramientas poderosas que te permiten expandir tu negocio y encontrar lo que buscas de manera eficiente.
    </p>
  </v-col>
</v-row>


    <!-- Tarjetas -->
    <v-row justify="center" dense>
      <v-col
        cols="12"
        md="4"
        lg="4"
        v-for="(service, index) in services"
        :key="index"
        class="d-flex justify-center my-4"
      >
        <div class="flip-card">
          <div class="flip-card-inner">
            <!-- Lado Frontal -->
            <div class="flip-card-front rounded-lg bg-white shadow-card p-6">
              <div class="flex flex-col items-center gap-5">
                <v-icon :size="60" class="icon-color">{{ service.icon }}</v-icon>
                <h4 class="text-center text-[24px] font-semibold text-gray-800">
                  {{ service.title }}
                </h4>
                <p class="text-center text-[15px] text-gray-600 leading-relaxed">
                  {{ service.description }}
                </p>
              </div>
            </div>

            <!-- Lado Trasero -->
            <div class="flip-card-back rounded-lg bg-lightblue text-white p-6">
              <div class="flex flex-col items-center gap-5">
                <v-icon :size="60" class="icon-color">{{ service.icon }}</v-icon>
                <h4 class="text-center text-[24px] font-semibold">
                  {{ service.title }}
                </h4>
                <p class="text-center text-[15px] leading-relaxed">
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
export default {
  name: "ServiceCards",
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
            "Nuestro equipo se encarga de diseñar interfaces atractivas y fáciles de usar que mejoran la experiencia de compra y venta.",
          details:
            "Creamos interfaces intuitivas para garantizar una navegación rápida, agradable y sin complicaciones para compradores y vendedores.",
        },
        {
          icon: "mdi-web",
          title: "Desarrollo Web",
          description:
            "Desarrollamos sitios web robustos y optimizados para todos los dispositivos, para que tu tienda online funcione perfectamente en cualquier pantalla.",
          details:
            "Desde diseños responsivos hasta integraciones avanzadas, nos aseguramos de que tu tienda en línea sea eficaz y fácil de usar.",
        },
        {
          icon: "mdi-cog",
          title: "Software Personalizado",
          description:
            "Ofrecemos soluciones de software a medida para satisfacer las necesidades específicas de tu negocio de ventas en línea.",
          details:
            "Nuestro equipo de ingenieros trabaja con las últimas tecnologías para entregar soluciones escalables y eficientes, adaptadas a tus requerimientos.",
        },
        {
          icon: "mdi-cloud",
          title: "Soluciones en la Nube",
          description:
            "Migramos y gestionamos tus operaciones comerciales en la nube de forma sencilla, asegurando que tu tienda esté siempre disponible y segura.",
          details:
            "Nuestros expertos en la nube garantizan un entorno seguro y escalable para que tu negocio crezca sin preocupaciones.",
        },
        {
          icon: "mdi-security",
          title: "Ciberseguridad",
          description:
            "Protege tus activos digitales y los datos de tus clientes con nuestros servicios de ciberseguridad avanzados.",
          details:
            "Ofrecemos protección contra amenazas cibernéticas, asegurando que la información de tu tienda y clientes esté siempre segura.",
        },
      ],
    };
  },
};
</script>

<style scoped>
.flip-card {
  perspective: 1000px;
  width: 100%;
  max-width: 320px;
  height: 350px;
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
  border-radius: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.flip-card-front {
  background-color: white;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

.flip-card-back {
  background-color: #a2cffe; 
  transform: rotateY(180deg);
  color: white;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.15);
}


h2 {
  font-family: "Inter", sans-serif;
  margin-bottom: 16px;
}

p {
  font-family: "Inter", sans-serif;
  color: #4d4d4d;
}


.shadow-card {
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
}


.icon-color {
  color: #5187f1; 
}
</style>
