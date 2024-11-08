<template>
  <v-app-bar app color="#5d87d4" dark elevate>
    <v-img 
      src="/logo.svg" 
      alt="Logo" 
      max-width="150" 
      class="mr-4 d-flex align-center logo-transition"
    ></v-img>


    <v-text-field
      v-model="searchQuery"
      append-icon="mdi-magnify"
      label="Buscar productos"
      class="search-bar"
      hide-details
      solo
      clearable
      :style="{ maxWidth: '350px' }"
      outlined
      dense
      :rules="[value => value.length >= 3 || 'Ingrese al menos 3 caracteres']"
    ></v-text-field>

    <v-spacer></v-spacer>

    <v-btn text to="/store/products" class="ml-4 white--text button-hover">
     Ver productos
    </v-btn>
    <v-btn text to="/login" class="ml-4 white--text button-hover">
      Iniciar sesión
    </v-btn>
    <v-btn text to="/register" class="ml-4 white--text button-hover">
      Registrarse
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      searchQuery: "",
    };
  },
};
</script>

<style scoped>


.v-btn {
  font-size: 1.1rem;
  text-transform: none;
  font-weight: 400;
  border-radius: 20px;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
}

.v-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: scale(1.05);
}

.v-app-bar {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 0 24px;
  background-color: #9540a7;
}

.logo-transition:hover {
  transform: scale(1.1);
  transition: transform 0.3s ease-in-out;
}

.button-hover:hover {
  background-color: rgba(255, 255, 255, 0.15);
  transform: scale(1.05);
}

.search-bar {
  margin-right: 16px;
  transition: all 0.3s ease;
  max-width: 350px;
}

.search-bar input {
  font-size: 1rem;
}

.search-bar .v-input__control {
  border-radius: 30px;
  background-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.search-bar .v-input__append-inner {
  background-color: transparent;
}

.search-bar .v-input__append-inner .v-icon {
  color: rgba(255, 255, 255, 0.7);
}

.search-bar input:focus {
  border-color: #7e4baf;
  box-shadow: 0 0 12px rgba(126, 75, 175, 0.4);
}

.search-bar:hover {
  transform: scale(1.05);
}

@media (max-width: 600px) {
  .title {
    font-size: 1.3rem;
  }

  .mr-4 {
    margin-right: 20px;
  }

  .ml-4 {
    margin-left: 12px;
  }

  .search-bar {
    max-width: 200px;
  }
}
</style>
