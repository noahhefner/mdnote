import { createRouter, createWebHistory } from "vue-router";

import Login from "@/views/Login.vue";
import Home from "@/views/Home.vue";
import Editor from "@/views/Editor.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: Login,
    },
    {
      path: "",
      name: "home",
      component: Home,
    },
    {
      path: "/editor",
      name: "editor",
      component: Editor,
    },
  ],
});

export default router;
