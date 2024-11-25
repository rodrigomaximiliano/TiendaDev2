
# TiendaDev2 Proyecto final cursada en la empresa DevLights

TiendaDev2 es una aplicación web de comercio electrónico desarrollada con **FastAPI** en el backend y **Vue.js** en el frontend.

## Descripción

Este proyecto busca proporcionar una plataforma sencilla para la compra y venta de productos, con una arquitectura que separa el backend y el frontend.

## Tecnologías

- **Backend**: FastAPI, Python
- **Frontend**: Vue.js, JavaScript
- **Base de datos**: MongoDB Atlas

## Instalación

### Backend

1. Clona el repositorio:
   ```
   git clone https://github.com/rodrigomaximiliano/TiendaDev2.git
   ```

2. Navega al directorio del backend:
   ```
   cd TiendaDev2/backend-fastapi
   ```

3. Crea y activa un entorno virtual:
   ```
   poetry shell
   ```


4. Instala las dependencias usando Poetry:
   ```
   poetry install
   ```

5. Corre la aplicación:
   ```
   poetry run uvicorn main:app --reload
   ```

### Frontend

1. Navega al directorio del frontend:
   ```
   cd TiendaDev2/frontend-vue
   ```

2. Instala las dependencias:
   ```
   npm install
   ```

3. Corre la aplicación:
   ```
   npm run serve
   ```

## Uso

1. Abre el navegador y accede a la aplicación frontend en `http://localhost:8080` (o el puerto que se indique en la consola).
2. El backend estará disponible en `http://localhost:8000`.


