<template>
  <v-navigation-drawer v-model="drawer" :class="smallScreen ? 'h-75' : 'py-10'" :location="smallScreen ? 'bottom' : 'right'" temporary
                       touchless>
    <v-spacer></v-spacer>
    <v-list density="compact" nav>
      <v-list-item v-if="!this.isAdminOrSu()" prepend-icon="mdi-home-account" title="Home" to="/"
                   value="dashboard"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-view-dashboard" title="Dashboard" to="/"
                   value="dashboard"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-calendar-blank" title="Nieuwe planning"
                   value="nieuwe planning"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-bike" title="Rondes" value="rondes"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-office-building" title="Gebouwen"
                   value="gebouwen"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-account" title="Studenten"
                   value="studenten"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-account-key" title="Syndicussen"
                   value="syndicussen"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu()" prepend-icon="mdi-email-outline" title="Templates"
                   value="templates"></v-list-item>
      <v-list-item prepend-icon="mdi-account-circle" title="Account" to="/account/" value="account"></v-list-item>
      <v-list-item prepend-icon="mdi-logout" @click="this.logout()" title="Logout" value="logout"></v-list-item>
    </v-list>
    <v-divider></v-divider>
  </v-navigation-drawer>
  <v-app-bar color="primary">
    <template v-slot:prepend>
      <v-app-bar-nav-icon v-if="smallScreen" color="secondary" icon="mdi-arrow-left"
                          @click="this.goBack()"></v-app-bar-nav-icon>
      <v-app-bar-title>
        <v-img height="75px" src="../assets/logo.png" width="150px"/>
      </v-app-bar-title>
    </template>
    <template v-slot:append>
      <v-app-bar-nav-icon color="secondary" @click="drawer = !drawer"></v-app-bar-nav-icon>
    </template>
  </v-app-bar>
</template>

<script lang="ts">

import { onMounted, onBeforeUnmount, ref, defineComponent } from 'vue'
import router from '@/router'
import AuthService from "@/api/services/AuthService";

export default defineComponent({
  name: 'NavigationBar',
  methods: {
    async isAdminOrSu(): Promise<Boolean> {
      const user = this.$store.getters['session/currentUser'];
      return user.then(() => this.$store.getters['session/isAdmin']).catch(() => false);
    }
  },
  setup() {
    const drawer = ref(false)
    const smallScreen = ref(false)

    const logout = () => {
      return AuthService.handleLogout()
    }

    const goBack = () => {
      return router.back()
    }
    const onResize = () => {
      smallScreen.value = window.innerWidth < 700
    }
    onMounted(async () => {
      onResize()
      window.addEventListener('resize', onResize, { passive: true })
    })
    onBeforeUnmount(() => {
      if (typeof window !== 'undefined') {
        window.removeEventListener('resize', onResize)
      }
    })
    return {
      drawer,
      smallScreen,
      goBack,
      logout
    }
  }
})
</script>

<style scoped>

</style>
