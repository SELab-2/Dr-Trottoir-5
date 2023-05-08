<template>
  <v-app-bar color="primary">
    <template v-slot:prepend>
      <v-app-bar-title>
        <v-img height="75px" src="../assets/logo.png" width="150px"/>
      </v-app-bar-title>
    </template>
    <template v-slot:append>
      <v-btn :to="login ? {name: 'register'} : {name: 'login'}" class="bg-secondary mx-3 mx-lg-6">{{login ? 'Aanmelden' : 'Login'}}</v-btn>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  name: 'LoginTopBar',
  props: {
    login: Boolean, default: () => true
  }
}
</script>

<style scoped>

</style>
