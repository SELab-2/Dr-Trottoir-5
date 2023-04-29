<template>
  <v-navigation-drawer v-model="drawer" :class="smallScreen ? 'h-75' : 'py-10'" :location="smallScreen ? 'bottom' : 'right'" temporary
                       touchless>
    <v-spacer></v-spacer>
    <v-list density="compact" nav>
      <v-list-item v-if="!this.isAdminOrSu" prepend-icon="mdi-home-account" title="Home" to="/"
                   value="dashboard"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-view-dashboard" title="Dashboard" :to="{name: 'admin_home'}"
                   value="dashboard"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-calendar-blank" title="Studenten Templates" :to="{name: 'studenttemplates'}"
                   value="studenten templates"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-bike" title="Rondes" :to="{name: 'rounds'}"
                   value="rondes"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-office-building" title="Gebouwen" :to="{name: 'buildings'}"
                   value="gebouwen"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-account" title="Studenten" :to="{name: 'students'}"
                   value="studenten"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-account-key" title="Syndicussen" :to="{name: 'syndici'}"
                   value="syndicussen"></v-list-item>
      <v-list-item v-if="this.isAdminOrSu" prepend-icon="mdi-email-outline" title="Email Templates" :to="{name: 'mailtemplates'}"
                   value="email templates"></v-list-item>
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
import { UserRole } from '@/api/models/UserRole';

export default defineComponent({
  name: 'NavigationBar',
  data: () => ({
    isAdminOrSu: false
  }),
  async beforeCreate() {
    this.isAdminOrSu = await this.$store.getters['session/isAdmin'];
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
