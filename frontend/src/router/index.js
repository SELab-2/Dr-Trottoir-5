import { createRouter, createWebHistory } from 'vue-router'
import StudentHomeView from '../views/StudentHomeView.vue'
import RegisterView from '@/views/RegisterView'
import LoginView from '../views/LoginView.vue'
import UsersView from '../views/UsersView.vue'
import RegisterDone from '@/components/RegisterDone'
import DayPlanView from "@/views/DayPlanView";
import BuildingPageStudent from "@/views/BuildingPageStudent";
import InfoScreenBuilding from "@/components/student/InfoScreenBuilding";
import StudentCreatePost from "@/views/StudentCreatePost";
import StudentPostView from "@/views/StudentPostView";
import StudentEditPost from "@/views/StudentEditPost";

const routes = [
  {
    path: '/',
    name: 'student_home',
    component: StudentHomeView
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
