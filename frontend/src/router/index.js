import TrashContainerEdit from '@/components/containerTemplates/containers/TrashContainerEdit.vue'
import { createRouter, createWebHistory } from 'vue-router'
import StudentHomeView from '../views/StudentHomeView.vue'
import AccountView from '../views/AccountView'
import RegisterView from '@/views/RegisterView'
import LoginView from '../views/LoginView.vue'
import UsersView from '../views/UsersView.vue'
import CreateBuildingView from '@/views/admin/CreateBuildingView'
import ForgotView from '../views/ForgotView.vue'
import RegisterDone from '@/components/RegisterDone'
import DayPlanView from "@/views/DayPlanView";
import BuildingList from "@/views/listViews/BuildingList";
import RoundList from "@/views/listViews/RoundList";
import StudentList from "@/views/listViews/StudentList";
import SyndicusList from "@/views/listViews/SyndicusList";
import TemplateList from "@/views/listViews/TemplateList";
import CreateRoundView from "@/views/CreateRoundView.vue";
import AdminMailTemplateView from "@/views/AdminMailTemplateView.vue";
import CreateMailTemplateView from "@/views/CreateMailTemplateView.vue";
import Unauthorized from "@/views/Unauthorized";
import BuildingPageStudent from "@/views/BuildingPageStudent";
import InfoScreenBuilding from "@/components/student/InfoScreenBuilding";
import StudentCreatePost from "@/views/StudentCreatePost";
import StudentPostView from "@/views/StudentPostView";
import StudentEditPost from "@/views/StudentEditPost";
import CreateLocationView from "@/views/admin/CreateLocationView";
import AdminBuildingView from "@/views/admin/AdminBuildingView";
import HomeView from "@/views/HomeView.vue";
import StudentTemplateView from "@/views/student_template/StudentTemplateView.vue";
import StudentTemplateEditView from "@/views/student_template/StudentTemplateEditView.vue";
import StudentTemplateAddView from "@/views/student_template/StudentTemplateAddView.vue";
import RondeDagplanningenView from "@/views/student_template/RondeDagplanningenView.vue";
import DagplanningEditView from "@/views/student_template/DagplanningEditView.vue";
import DagplanningAddView from "@/views/student_template/DagplanningAddView.vue";
import TrashTemplateBuildingsList from '@/components/containerTemplates/buildings/TrashTemplateBuildingsList.vue'
import TrashTemplateContainersList from '@/components/containerTemplates/containers/TrashTemplateContainersList.vue'
import TrashContainerTemplateList from '@/components/containerTemplates/TrashContainerTemplateList.vue'
import TrashContainerCreate from '@/components/containerTemplates/containers/TrashContainerCreate.vue'
import TrashContainerTemplateCreate from '@/components/containerTemplates/TrashContainerTemplateCreate.vue'
import TrashContainerTemplateEdit from '@/components/containerTemplates/TrashContainerTemplateEdit.vue'
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
    path: '/location/create',
    name: 'create_location',
    component: CreateLocationView
  },
  {
    path: '/building/create',
    name: 'create_building',
    component: CreateBuildingView
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
    path: '/building/:id',
    name: 'admin_building',
    props: true,
    component: AdminBuildingView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView
  },
  {
    path: '/studenttemplates',
    name: 'studenttemplates',
    component: StudentTemplateView
  },
    {
    path: '/studenttemplates/add',
    name: 'add_studenttemplate',
    component: StudentTemplateAddView
  },
  {
    path: '/studenttemplates/:id',
    name: 'studenttemplate',
    component: StudentTemplateEditView
  },
  {
    path: '/studenttemplates/:template_id/rondes/:ronde_id',
    name: 'ronde_dagplanningen',
    component: RondeDagplanningenView
  },
  {
    path: '/studenttemplates/:template_id/rondes/:ronde_id/dagplanningen/:dag_id',
    name: 'dagplanning_edit',
    component: DagplanningEditView
  },
  {
    path: '/studenttemplates/:template_id/rondes/:ronde_id/add',
    name: 'dagplanning_add',
    component: DagplanningAddView
  },
  {
    path: '/buildings',
    name: 'buildings',
    component: BuildingList
  },
  {
    path: '/rounds',
    name: 'rounds',
    component: RoundList
  },
  {
    path: '/students',
    name: 'students',
    component: StudentList
  },
  {
    path: '/syndicusen',
    name: 'syndicusen',
    component: SyndicusList
  },
  {
    path: '/mailtemplates',
    name: 'mailtemplates',
    component: TemplateList
  },
  {
    path: '/trashtemplates',
    name: 'trashtemplates',
    component: TrashContainerTemplateList
  },
  {
    path: '/trashtemplates/:id/edit',
    name: 'editTrashtemplates',
    component: TrashContainerTemplateEdit,
    props: true
  },
  {
    path: '/trashtemplates/create',
    name: 'createTrashtemplates',
    component: TrashContainerTemplateCreate,
    props: true
  },
  {
    path: '/trashtemplates/:id/containers',
    name: 'trashtemplateContainers',
    component: TrashTemplateContainersList,
    props: true
  },
  {
    path: '/trashtemplates/:id/containers/create',
    name: 'createTrashtemplateContainers',
    component: TrashContainerCreate,
    props: true
  },
  {
    path: '/trashtemplates/:id/containers/:containerId/edit',
    name: 'editTrashtemplateContainers',
    component: TrashContainerEdit,
    props: true
  },
  {
    path: '/trashtemplates/:id/buildings',
    name: 'trashtemplateBuildings',
    component: TrashTemplateBuildingsList,
    props: true
  },
  {
    path: '/trashtemplates/:id/buildings/edit',
    name: 'editTrashtemplateBuildings',
    component: TrashContainerTemplateList, // TODO SWITCH TO BUILDINGS EDIT PAGE
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
