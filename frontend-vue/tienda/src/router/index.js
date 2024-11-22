import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Cart from "../views/Cart.vue";
import MyAccount from "../views/MyAccount.vue";
import ProductList from "../views/ProductList.vue";
import CreateProduct from "../views/CreateProduct.vue";
import MisProductos from "@/views/MisProductos.vue";

const routes = [
  { path: "/", name: "home", component: HomePage },
  { path: "/login", name: "login", component: Login },
  { path: "/register", name: "register", component: Register },
  { path: "/cart", name: "cart", component: Cart },
  { path: "/mi_cuenta", name: "miCuenta", component: MyAccount },
  { path: "/store/products", name: "product-list", component: ProductList },
  { path: "/mis-productos", name: "MisProductos", component: MisProductos },
  { path: "/create-product", name: "CreateProduct", component: CreateProduct, meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
