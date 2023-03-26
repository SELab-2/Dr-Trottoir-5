<template>
  <v-navigation-drawer v-model="drawer" temporary touchless :location="smallScreen ? 'bottom' : 'right'" :class="smallScreen ? 'h-75' : 'py-10'">
    <v-spacer></v-spacer>
    <v-list density="compact" nav>
      <v-list-item prepend-icon="mdi-home-account" v-if="!this.isAdminOrSu()" to="/" title="Home" value="dashboard"></v-list-item>
      <v-list-item prepend-icon="mdi-view-dashboard" v-if="this.isAdminOrSu()" to="/" title="Dashboard" value="dashboard"></v-list-item>
      <v-list-item prepend-icon="mdi-calendar-blank" v-if="this.isAdminOrSu()" title="Nieuwe planning" value="nieuwe planning"></v-list-item>
      <v-list-item prepend-icon="mdi-bike" v-if="this.isAdminOrSu()" title="Rondes" value="rondes"></v-list-item>
      <v-list-item prepend-icon="mdi-office-building" v-if="this.isAdminOrSu()" title="Gebouwen" value="gebouwen"></v-list-item>
      <v-list-item prepend-icon="mdi-account" to="/users/" v-if="this.isAdminOrSu()" title="Studenten" value="studenten"></v-list-item>
      <v-list-item prepend-icon="mdi-account-key" v-if="this.isAdminOrSu()" title="Syndicussen" value="syndicussen"></v-list-item>
      <v-list-item prepend-icon="mdi-email-outline" v-if="this.isAdminOrSu()" title="Templates" value="templates"></v-list-item>
      <v-list-item prepend-icon="mdi-account-circle" to="/account/" title="Account" value="account"></v-list-item>
      <v-list-item prepend-icon="mdi-logout" :active="false" @click="logoutUser(); show = false" title="Logout" value="logout"></v-list-item>
    </v-list>
    <v-divider></v-divider>
  </v-navigation-drawer>
  <v-app-bar color="primary">
    <template v-slot:prepend>
      <v-app-bar-nav-icon v-if="smallScreen" @click="this.goBack()" color="secondary" icon="mdi-arrow-left" ></v-app-bar-nav-icon>
      <v-app-bar-title>
        <v-img src="../assets/logo.png" height="75px" width="150px"/>
      </v-app-bar-title>
    </template>
    <template v-slot:append>
      <v-app-bar-nav-icon v-if="show" color="secondary" @click="drawer = !drawer"></v-app-bar-nav-icon>
    </template>
  </v-app-bar>
</template>

<script>

import { onMounted, onBeforeUnmount, ref } from 'vue'
import { request, logoutUser } from '@/authorized'
import router from '@/router'

export default {
  name: 'NavigationBar',
  methods: { logoutUser },
  setup () {
    const role = ref('')
    const drawer = ref(false)
    const smallScreen = ref(false)
    const show = ref(window.location.pathname !== '/login' && window.location.pathname !== '/register')

    const isAdminOrSu = () => {
      return role.value === 'AD' || role.value === 'SU'
    }
    const goBack = () => {
      return router.go(-1)
    }
    const onResize = () => {
      smallScreen.value = window.innerWidth < 700
    }

    const getRole = async () => {
      const response = await request('/api/role/', 'GET')
      role.value = response !== undefined && 'role' in response ? response.role : ''
    }

    onMounted(async () => {
      await getRole()

      onResize()
      window.addEventListener('resize', onResize, { passive: true })
      window.addEventListener('login', () => { show.value = true; getRole() })
      window.addEventListener('logout', () => { show.value = false })
    })
    onBeforeUnmount(() => {
      if (typeof window !== 'undefined') {
        window.removeEventListener('resize', onResize, { passive: true })
      }
    })
    return {
      drawer,
      smallScreen,
      role,
      show,
      isAdminOrSu,
      goBack
    }
  }
}
</script>

<style scoped>

</style>
