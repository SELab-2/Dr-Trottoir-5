<template>
  <v-container>
    <h2>all users</h2>
    <!-- Loading -->
    <div v-if="users.isLoading()">
      <h3>LOADING users</h3>
    </div>
    <div v-else-if="users.isSuccess()">
      <p v-for="u in users.requireData()">{{ u.email }}</p>
    </div>

    <h2>The currently logged in user</h2>
    <!-- Loading -->
    <div v-if="user.isLoading()">
      <h3>LOADING users</h3>
    </div>
    <div v-else-if="user.isSuccess()">
      <p>{{ user.requireData().email }}</p>
    </div>
  </v-container>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import UserService from "@/api/services/UserService";

/*
 view is just for testing purposes, will be removed
*/

export default defineComponent({
  name: 'UsersView',
  data() {
    return {
      user: UserService.get(),
      users: UserService.getUsers()
    }
  }
})
</script>
