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
import AdminMailTemplateView from "@/views/AdminMailTemplateView.vue";
import CreateMailTemplateView from "@/views/CreateMailTemplateView.vue";
import Unauthorized from "@/views/Unauthorized";
import BuildingPageStudent from "@/views/BuildingPageStudent";
import InfoScreenBuilding from "@/components/student/InfoScreenBuilding";
import StudentCreatePost from "@/views/StudentCreatePost";
import StudentPostView from "@/views/StudentPostView";
import StudentEditPost from "@/views/StudentEditPost";
import CreateLocationView from "@/views/admin/CreateLocationView";
import HomeView from "@/views/HomeView.vue";
import DashboardView from "@/views/admin/DashboardView.vue";
import AdminStudentInfoUser from "@/views/admin/AdminStudentInfoUser";
import RegisterUserList from "@/views/listViews/RegisterUserList";
import AdminStudentInfoUserEdit from "@/views/admin/AdminStudentInfoUserEdit";
import AdminBuildingInfoEditView from "@/views/admin/AdminBuildingInfoEditView";
import AdminBuildingInfoView from "@/views/admin/AdminBuildingInfoView";
import StudentTemplateView from "@/views/student_template/StudentTemplateView.vue";
import StudentTemplateEditView from "@/views/student_template/StudentTemplateEditView.vue";
import StudentTemplateAddView from "@/views/student_template/StudentTemplateAddView.vue";
import RondeDagplanningenView from "@/views/student_template/RondeDagplanningenView.vue";
import DagplanningEditView from "@/views/student_template/DagplanningEditView.vue";
import DagplanningAddView from "@/views/student_template/DagplanningAddView.vue";
import CreateSyndicusView from "@/views/admin/CreateSyndicusView";
import AdjustSyndicusView from "@/views/admin/AdjustSyndicusView";
import TrashTemplateBuildingsList from '@/components/containerTemplates/buildings/TrashTemplateBuildingsList.vue'
import TrashTemplateBuildingEdit from '@/components/containerTemplates/buildings/TrashTemplateBuildingEdit.vue'
import TrashTemplateBuildingAdd from '@/components/containerTemplates/buildings/TrashTemplateBuildingAdd.vue'
import TrashTemplateContainersList from '@/components/containerTemplates/containers/TrashTemplateContainersList.vue'
import TrashContainerTemplateList from '@/components/containerTemplates/TrashContainerTemplateList.vue'
import TrashContainerCreate from '@/components/containerTemplates/containers/TrashContainerCreate.vue'
import TrashContainerTemplateCreate from '@/components/containerTemplates/TrashContainerTemplateCreate.vue'
import TrashContainerEdit from '@/components/containerTemplates/containers/TrashContainerEdit.vue'
import LocationList from "@/views/listViews/LocationList";
import CreateEditRoundView from "@/views/admin/CreateEditRoundView.vue";
import AdminRoundView from "@/views/admin/AdminRoundView.vue";
import SendMailView from "@/views/admin/SendMailView.vue";
import SyndicusHome from "@/views/syndicus/SyndicusHome.vue";
import BuildingView from "@/views/BuildingView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/student',
    name: 'student_home',
    component: StudentHomeView
  },
  {
    path: '/syndicus',
    name: 'syndicus_home',
    component: SyndicusHome
  },
  {
    path: '/gebouw/:id',
    name: 'building_page',
    component: BuildingView,
    props: true
  },
  {
    path: '/admin',
    name: 'admin_home',
    component: DashboardView
  },
  {
    path: '/bewoner',
    name: 'resident_home',
    component: RegisterDone
  },
  {
    path: '/registreer',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/verstuurd',
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
    // TODO verwijderen
    path: '/users',
    name: 'users',
    component: UsersView
  },
  {
    path: '/admin/locaties',
    name: 'locations',
    component: LocationList
  },
  {
    path: '/admin/locatie/aanmaken',
    name: 'create_location',
    component: CreateLocationView
  },
  {
    path: '/admin/gebouw/aanmaken',
    name: 'create_building',
    component: CreateBuildingView
  },
  {
    path: '/admin/mailtemplate/aanmaken',
    name: 'create_mail-template',
    component: CreateMailTemplateView
  },
  {
    path: '/admin/mailtemplate/:id/aanpassen',
    name: 'mail-template-edit',
    component: AdminMailTemplateView
  },
  {
    path: '/student/dagplanning',
    name: 'dagplanning',
    component: DayPlanView
  },
  {
    path: '/admin/ronde/aanmaken',
    name: 'create_round',
    component: CreateEditRoundView
  },
  {
    path: '/admin/ronde/:id/aanpassen',
    name: 'edit_round',
    props: true,
    component: CreateEditRoundView
  },
  {
    path: '/verboden',
    name: 'unauthorized',
    component: Unauthorized
  },
  {
    path: '/student/gebouw',
    name: 'building_student',
    component: BuildingPageStudent
  },
  {
    path: '/student/gebouw/info',
    name: 'building_info',
    component: InfoScreenBuilding
  },
  {
    path: '/student/gebouw/taak',
    name: 'student_post_view',
    component: StudentPostView
  },
  {
    path: '/student/gebouw/taak/post',
    name: 'student_post',
    component: StudentCreatePost
  },
  {
    path: '/student/gebouw/taak/aanpassen',
    name: 'student_post_edit',
    component: StudentEditPost
  },
  {
    path: '/admin/gebouw/:id',
    name: 'admin_info_building',
    props: true,
    component: AdminBuildingInfoView
  },
  {
    path: '/admin/gebouw/:id/aanpassen',
    name: 'admin_edit_building',
    props: true,
    component: AdminBuildingInfoEditView
  },
  {
    path: '/admin/syndicus/aanmaken',
    name: 'syndicus_create',
    component: CreateSyndicusView
  },
  {
    path: '/admin/syndicus/aanpassen',
    name: 'syndicus_adjust',
    component: AdjustSyndicusView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView
  },
  {
    path: '/admin/studenttemplates',
    name: 'studenttemplates',
    component: StudentTemplateView
  },
    {
    path: '/admin/studenttemplate/aanmaken',
    name: 'add_studenttemplate',
    component: StudentTemplateAddView
  },
  {
    path: '/admin/studenttemplate/:id',
    name: 'studenttemplate',
    component: StudentTemplateEditView
  },
  {
    path: '/admin/studenttemplate/:template_id/ronde/:ronde_id',
    name: 'ronde_dagplanningen',
    component: RondeDagplanningenView
  },
  {
    path: '/admin/studenttemplate/:template_id/ronde/:ronde_id/dagplanning/:dag_id',
    name: 'dagplanning_edit',
    component: DagplanningEditView
  },
  {
    path: '/admin/studenttemplate/:template_id/ronde/:ronde_id/dagplanning/aanmaken',
    name: 'dagplanning_add',
    component: DagplanningAddView
  },
  {
    path: '/admin/gebouwen',
    name: 'buildings',
    component: BuildingList
  },
  {
    path: '/admin/rondes',
    name: 'rounds',
    component: RoundList
  },
  {
    path: '/admin/studenten',
    name: 'students',
    component: StudentList
  },
  {
    path: '/admin/studenten/registreer',
    name: 'admin_user_register',
    component: RegisterUserList
  },
  {
    path: '/admin/syndici',
    name: 'syndici',
    component: SyndicusList
  },
  {
    path: '/admin/mailtemplates',
    name: 'mailtemplates',
    component: TemplateList
  },
  {
    path: '/admin/send_mail/:id/post/:postId',
    name: 'send_mail',
    props: true,
    component: SendMailView
  },
  {
    path: '/admin/gebruiker/:id',
    name: 'admin_info_user',
    props: true,
    component: AdminStudentInfoUser
  },
  {
    path: '/admin/gebruiker/:id/aanpassen',
    name: 'admin_edit_user',
    props: true,
    component: AdminStudentInfoUserEdit
  },
  {
    path: '/admin/afvaltemplates',
    name: 'trashtemplates',
    component: TrashContainerTemplateList
  },
  {
    path: '/admin/afvaltemplate/aanmaken',
    name: 'createTrashtemplates',
    component: TrashContainerTemplateCreate,
    props: true
  },
  {
    path: '/admin/afvaltemplate/:id/containers',
    name: 'trashtemplateContainers',
    component: TrashTemplateContainersList,
    props: true
  },
  {
    path: '/admin/afvaltemplate/:id/container/aanmaken',
    name: 'createTrashtemplateContainers',
    component: TrashContainerCreate,
    props: true
  },
  {
    path: '/admin/afvaltemplate/:id/container/:containerId/aanpassen',
    name: 'editTrashtemplateContainers',
    component: TrashContainerEdit,
    props: true
  },
  {
    path: '/admin/afvaltemplate/:id/gebouwen',
    name: 'trashtemplateBuildings',
    component: TrashTemplateBuildingsList,
    props: true
  },
  {
    path: '/admin/afvaltemplate/:id/gebouw/:gebouwId/aanpassen',
    name: 'editTrashtemplateBuilding',
    component: TrashTemplateBuildingEdit,
    props: true
  },
  {
    path: '/admin/afvaltemplate/:id/gebouw/toevoegen',
    name: 'addBuildingsToTrashTemplate',
    component: TrashTemplateBuildingAdd,
    props: true
  },
  {
    path: '/admin/ronde',
    name: 'adminRoundView',
    component: AdminRoundView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
