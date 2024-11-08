import { createRouter, createWebHistory } from 'vue-router'; 
import HomePage from '../views/HomePage.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Cart from '../views/Cart.vue';
import MyAccount from '../views/MyAccount.vue';
import ProductList from '../views/ProductList.vue';

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/login', name: 'login', component: Login },
  { path: '/register', name: 'register', component: Register },
  { path: '/cart', name: 'cart', component: Cart },
  { path: '/mi_cuenta', name: 'my-account', component: MyAccount },
  { path: '/store/products', name: 'product-list', component: ProductList },
];

const router = createRouter({
  history: createWebHistory(), 
  routes
});

export default router;
