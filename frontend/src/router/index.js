import { createRouter, createWebHistory } from 'vue-router'
import StudentHomeView from '../views/StudentHomeView.vue'
import AccountView from '../views/AccountView'
import RegisterView from '@/views/RegisterView'
import LoginView from '../views/LoginView.vue'
import UsersView from '../views/UsersView.vue'
import ForgotView from '../views/ForgotView.vue'
import RegisterDone from '@/components/RegisterDone'
import DayPlanView from "@/views/DayPlanView";
import CreateRoundView from "@/views/CreateRoundView.vue";
import AdminMailTemplateView from "@/views/AdminMailTemplateView.vue";
import CreateMailTemplateView from "@/views/CreateMailTemplateView.vue";
import Unauthorized from "@/views/Unauthorized";
import BuildingPageStudent from "@/views/BuildingPageStudent";
import InfoScreenBuilding from "@/components/student/InfoScreenBuilding";
import StudentCreatePost from "@/views/StudentCreatePost";
import StudentPostView from "@/views/StudentPostView";
import StudentEditPost from "@/views/StudentEditPost";
import HomeView from "@/views/HomeView";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/student_home',
    name: 'student_home',
    component: StudentHomeView
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
    path: '/mail-template/create',
    name: 'create_mail-template',
    component: CreateMailTemplateView
  },
  {
    path: '/mail-template/:id',
    name: 'mail-template',
    component: AdminMailTemplateView
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
    path: '/unauthorized',
    name: 'unauthorized',
    component: Unauthorized
  },
  {
    path: '/building_student',
    name: 'building_student',
    component: BuildingPageStudent
  },
  {
    path: '/building_info',
    name: 'building_info',
    component: InfoScreenBuilding
  },
  {
    path: '/student_post_view',
    name: 'student_post_view',
    component: StudentPostView
  },
  {
    path: '/student_post',
    name: 'student_post',
    component: StudentCreatePost
  },
  {
    path: '/student_post_edit',
    name: 'student_post_edit',
    component: StudentEditPost
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
