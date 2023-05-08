<template>
  <v-container>
    <h2>all users</h2>
    <!-- Loading -->
    <div v-if="users.isLoading()" :key="loaded.users">
      <h3>LOADING users</h3>
    </div>
    <div v-else-if="users.isSuccess()">
      <p v-for="u in users.requireData()" :key="u.email">{{ u.email }}</p>
    </div>

    <h2>The currently logged in user</h2>
    <!-- Loading -->
    <div v-if="user.isLoading()" :key="loaded.user">
      <h3>LOADING users</h3>
    </div>
    <div v-else-if="user.isSuccess()">
      <p>{{ user.requireData().email }}</p>
    </div>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import UserService from '@/api/services/UserService'
import { RequestHandler } from '@/api/RequestHandler'

/*
 view is just for testing purposes, will be removed
*/

export default defineComponent({
  name: 'UsersView',
  data () {
    return {
      user: RequestHandler.handle(UserService.get(), {
        id: 'getUserError',
        style: 'SNACKBAR'
      }),
      users: RequestHandler.handle(UserService.getUsers(), {
        id: 'getUsersError',
        style: 'SNACKBAR'
      }),
      loaded: {}
    }
  },
  created () {
    this.user.finally(() => { this.loaded.user = true }).catch(() => {})
    this.users.finally(() => { this.loaded.users = true }).catch(() => {})
  }
})
</script>
