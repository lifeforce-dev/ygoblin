import Vue from 'vue';
import Router from 'vue-router';
import Card from '../components/card';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);
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
