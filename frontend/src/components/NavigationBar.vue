<template>
  <v-navigation-drawer v-model="drawer" temporary touchless :location="smallScreen ? 'bottom' : 'right'" :class="smallScreen ? 'h-75' : 'py-10'">
    <v-spacer></v-spacer>
    <v-list density="compact" nav>
      <v-list-item prepend-icon="mdi-home-account" v-if="!this.isAdminOrSu()" to="/" title="Home" value="dashboard"></v-list-item>
      <v-list-item prepend-icon="mdi-view-dashboard" v-if="this.isAdminOrSu()" to="/" title="Dashboard" value="dashboard"></v-list-item>
      <v-list-item prepend-icon="mdi-calendar-blank" v-if="this.isAdminOrSu()" title="Nieuwe planning" value="nieuwe planning"></v-list-item>
      <v-list-item prepend-icon="mdi-bike" v-if="this.isAdminOrSu()" title="Rondes" value="rondes"></v-list-item>
      <v-list-item prepend-icon="mdi-office-building" v-if="this.isAdminOrSu()" title="Gebouwen" value="gebouwen"></v-list-item>
      <v-list-item prepend-icon="mdi-account" v-if="this.isAdminOrSu()" title="Studenten" value="studenten"></v-list-item>
      <v-list-item prepend-icon="mdi-account-key" v-if="this.isAdminOrSu()" title="Syndicussen" value="syndicussen"></v-list-item>
      <v-list-item prepend-icon="mdi-email-outline" v-if="this.isAdminOrSu()" title="Templates" value="templates"></v-list-item>
      <v-list-item prepend-icon="mdi-account-circle" to="/account/" title="Account" value="account"></v-list-item>
      <v-list-item prepend-icon="mdi-logout" title="Logout" value="logout"></v-list-item>
    </v-list>
    <v-divider></v-divider>
  </v-navigation-drawer>
  <v-app-bar color="primary">
    <template v-slot:prepend>
      <v-app-bar-title>
        <v-img src="../assets/logo.png" height="75px" width="150px"/>
      </v-app-bar-title>
    </template>
    <template v-slot:append>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </template>
  </v-app-bar>
</template>

<script>

import { onMounted, onBeforeUnmount, ref } from 'vue'
import { request } from '@/authorized'

export default {
  name: 'NavigationBar',
  setup () {
    const role = ref('')
    const drawer = ref(false)
    const smallScreen = ref(false)

    const isAdminOrSu = () => {
      return role.value === 'AD' || role.value === 'SU'
    }

    const onResize = () => {
      smallScreen.value = window.innerWidth < 700
    }
    onMounted(async () => {
      const response = await request('/api/role/', 'GET')
      role.value = 'role' in response ? response.role : ''

      onResize()
      window.addEventListener('resize', onResize, { passive: true })
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
      isAdminOrSu
    }
  }
}
</script>

<style scoped>

</style>
