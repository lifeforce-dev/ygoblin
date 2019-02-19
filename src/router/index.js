import Vue from 'vue';
import Router from 'vue-router';
import Card from '../components/card';

Vue.use(Router);
const routes = [
  {
    path: '/',
    component: Card
  }
];
const router = new Router({
  routes,
  mode: 'history'
});

export default router;
