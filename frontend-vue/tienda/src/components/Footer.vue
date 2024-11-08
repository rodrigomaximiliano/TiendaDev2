<template>
  <v-footer color="#5d87d4" app>
    <v-row
      align="center"
      justify="space-between"
      class="py-4 px-10"
    >
      <v-col
        cols="12" md="6"
        class="text-center text-md-left"
      >
        <span class="white--text">© 2024 Tienda Devlights | Todos los derechos reservados.</span>
      </v-col>

      <v-col
        cols="12" md="6"
        class="text-center text-md-right social-icons"
      >
      <v-btn
  icon
  href="https://wa.me/"
  target="_blank"
  class="white--text"
>
  <v-icon color="#25d366">mdi-whatsapp</v-icon>
</v-btn>
        <v-btn
          icon
          href="https://www.instagram.com/"
          target="_blank"
          class="white--text"
        >
          <v-icon color="pink">mdi-instagram</v-icon>
        </v-btn>
        <!-- Usamos la ruta pública para cargar el logo de X desde la carpeta public -->
        <v-btn
  icon
  href="https://www.x.com/"
  target="_blank"
  class="white--text"
>
  <img src="/logodeX.jpg" alt="Logo de X" style="max-height: 20px;" />
</v-btn>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
.v-footer {
  width: 100%;
  background-color: #0e306e;
  padding: 20px;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 15px;
}

.social-icons .v-btn {
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.1);
}

.social-icons .v-btn:hover {
  background-color: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}
</style>
