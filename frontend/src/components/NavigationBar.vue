<template>
  <v-navigation-drawer v-model="drawer" temporary :location="smallScreen ? 'bottom' : 'right'" :class="smallScreen ? 'h-75' : 'py-10'">
    <v-spacer></v-spacer>
    <v-list density="compact" nav>
      <v-list-item prepend-icon="mdi-view-dashboard" to="/" title="Dashboard" value="home"></v-list-item>
      <v-list-item prepend-icon="mdi-calendar-blank" title="Nieuwe planning" value="nieuwe planning"></v-list-item>
      <v-list-item prepend-icon="mdi-bike" title="Rondes" value="rondes"></v-list-item>
      <v-list-item prepend-icon="mdi-office-building" title="Gebouwen" value="gebouwen"></v-list-item>
      <v-list-item prepend-icon="mdi-account" title="Studenten" value="studenten"></v-list-item>
      <v-list-item prepend-icon="mdi-account-key" title="Syndicussen" value="syndicussen"></v-list-item>
      <v-list-item prepend-icon="mdi-email-outline" title="Templates" value="templates"></v-list-item>
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

export default {
  name: 'NavigationBar',
  data () {
    return {
      drawer: null,
      smallScreen: false
    }
  },
  beforeUnmount () {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.onResize, { passive: true })
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    onResize () {
      this.smallScreen = window.innerWidth < 700
    }
  }
}
</script>

<style scoped>

</style>
