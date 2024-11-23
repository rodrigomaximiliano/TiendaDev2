<template>
  <v-footer app height="auto" class="footer-container">
    <v-container>
      <v-row justify="space-between" align="center" class="mb-4">
        <!-- Información de la empresa -->
        <v-col
          cols="12"
          md="4"
          class="text-center text-md-left"
        >
          <h3 class="footer-title">Tienda Devlights</h3>
          <p class="footer-description">
            Innovando para un futuro mejor. Encuentra lo que necesitas en nuestra tienda, donde la tecnología y la calidad son prioridad.
          </p>
        </v-col>

        <!-- Enlaces rápidos -->
        <v-col
          cols="12"
          md="4"
          class="text-center"
        >
          <h4 class="footer-title">Enlaces útiles</h4>
          <ul class="footer-links">
            <li><a href="/about" class="footer-link">Sobre nosotros</a></li>
            <li><a href="/contact" class="footer-link">Contacto</a></li>
            <li><a href="/faq" class="footer-link">Preguntas frecuentes</a></li>
            <li><a href="/terms" class="footer-link">Términos y condiciones</a></li>
          </ul>
        </v-col>

        <!-- Redes sociales -->
        <v-col
          cols="12"
          md="4"
          class="text-center text-md-right"
        >
          
          <div class="social-icons">
            <v-btn
              icon
              href="https://wa.me/"
              target="_blank"
              class="social-btn"
            >
              <v-icon color="#25d366">mdi-whatsapp</v-icon>
            </v-btn>
            <v-btn
              icon
              href="https://www.instagram.com/"
              target="_blank"
              class="social-btn"
            >
              <v-icon color="#e4405f">mdi-instagram</v-icon>
            </v-btn>
            <v-btn
              icon
              href="https://www.x.com/"
              target="_blank"
              class="social-btn"
            >
              <img
                src="/logodeX.jpg"
                alt="Logo de X"
                style="max-height: 24px;"
              />
            </v-btn>
            <v-btn
              icon
              href="https://www.facebook.com/"
              target="_blank"
              class="social-btn"
            >
              <v-icon color="#3b5998">mdi-facebook</v-icon>
            </v-btn>
          </div>
        </v-col>
      </v-row>

      <!-- Línea divisoria -->
      <v-divider class="my-4"></v-divider>

      <!-- Derechos reservados -->
      <v-row>
        <v-col cols="12" class="text-center">
          <p class="footer-rights">© 2024 Tienda Devlights | Todos los derechos reservados.</p>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
.footer-container {
  background: linear-gradient(135deg, #5d87d4 0%, #00c6ff 100%);
  color:whitesmoke;
  padding: 30px 0;
  box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.1);
}

.footer-title {
  font-weight: bold;
  font-size: 1.5rem;
  margin-bottom: 15px;
}

.footer-description {
  font-size: 0.9rem;
  line-height: 1.5;
  opacity: 0.8;
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 8px;
}

.footer-link {
  text-decoration: none;
  color: whitesmoke;
  font-weight: 500;
  transition: color 0.3s;
}

.footer-link:hover {
  color: #01579b;
}

.social-icons {
  display: flex;
  justify-content: center; /* Centra los íconos */
  gap: 15px;
}

.social-btn {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transition: transform 0.3s, background-color 0.3s;
}

.social-btn:hover {
  background-color: rgba(255, 255, 255, 0.4);
  transform: scale(1.2);
}

.footer-rights {
  font-size: 0.85rem;
  opacity: 0.7;
}
</style>
