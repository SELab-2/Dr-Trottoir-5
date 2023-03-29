<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
    <NavigationBar/>
  </v-app>
</template>

<script>

import NavigationBar from '@/components/NavigationBar.vue'

export default {
  name: 'App',
  components: {
    NavigationBar
  },
  data: () => ({
    //
  })
}
</script>
