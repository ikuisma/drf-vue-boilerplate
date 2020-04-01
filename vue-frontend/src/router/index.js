import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Echo from "../views/Echo.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/echo",
    name: "Echo",
    component: Echo
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
