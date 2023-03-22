<template>
  <v-sheet width="300" class="mx-auto">
    <v-form @submit.prevent>
      <v-text-field
        v-model="email"
        label="email"
      ></v-text-field>
      <v-text-field
        v-model="password"
        label="Wachtwoord"
      ></v-text-field>
      <v-btn @click="login" block class="mt-2">Submit</v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
import { loginUser } from '@/authorized'
export default {
  name: 'LoginPage',
  data: () => ({
    email: '',
    password: ''
  }),
  methods: {
    login () {
      loginUser(this.email, this.password)
    }
  }
}
</script>

<style scoped>

</style>
