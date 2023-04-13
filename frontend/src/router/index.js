import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AccountView from '../views/AccountView'
import RegisterView from '@/views/RegisterView'
import LoginView from '../views/LoginView.vue'
import UsersView from '../views/UsersView.vue'
import ForgotView from '../views/ForgotView.vue'
import RegisterDone from '@/components/RegisterDone'
import DayPlanView from "@/views/DayPlanView";
import BuildingList from "@/views/listViews/BuildingList";
import RoundList from "@/views/listViews/RoundList";
import StudentList from "@/views/listViews/StudentList";
import SyndicusList from "@/views/listViews/SyndicusList";
import TemplateList from "@/views/listViews/TemplateList";

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
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView
  },
  {
    path: '/gebouwen',
    name: 'gebouwen',
    component: BuildingList
  },
  {
    path: '/rondes',
    name: 'rondes',
    component: RoundList
  },
  {
    path: '/studenten',
    name: 'studenten',
    component: StudentList
  },
  {
    path: '/syndicussen',
    name: 'syndicussen',
    component: SyndicusList
  },
  {
    path: '/mailtemplates',
    name: 'mailtemplates',
    component: TemplateList
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
