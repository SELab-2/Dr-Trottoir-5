import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '@/views/RegisterView'
import LoginView from '../views/LoginView.vue'
import UsersView from '../views/UsersView.vue'
import ForgotView from '../views/ForgotView.vue'
import RegisterDone from '@/components/RegisterDone'
import DayPlanView from "@/views/DayPlanView";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/student_home',
    name: 'student_home',
    component: RegisterDone
  },
  {
    path: '/syndicus_home',
    name: 'syndicus_home',
    component: RegisterDone
  },
  {
    path: '/admin_home',
    name: 'admin_home',
    component: RegisterDone
  },
  {
    path: '/resident_home',
    name: 'resident_home',
    component: RegisterDone
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/register_done',
    name: 'register_done',
    component: RegisterDone
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/forgot',
    name: 'forgot',
    component: ForgotView
  },
  {
    path: '/users',
    name: 'users',
    component: UsersView
  },
  {
    path: '/dagplanning',
    name: 'dagplanning',
    component: DayPlanView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
