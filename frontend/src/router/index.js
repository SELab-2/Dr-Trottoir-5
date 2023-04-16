import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AccountView from '../views/AccountView'
import RegisterView from '@/views/RegisterView'
import LoginView from '../views/LoginView.vue'
import UsersView from '../views/UsersView.vue'
import ForgotView from '../views/ForgotView.vue'
import RegisterDone from '@/components/RegisterDone'
import DayPlanView from "@/views/DayPlanView";
import CreateRoundView from "@/views/CreateRoundView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
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
    path: '/create_round',
    name: 'create_round',
    component: CreateRoundView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
