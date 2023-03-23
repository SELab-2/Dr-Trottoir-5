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
import { defineComponent } from 'vue'
import { loginUser } from '@/authorized'

export default defineComponent({
  name: 'LoginView',
  data: () => ({
    email: '',
    password: '',
    prevRoute: null
  }),
  beforeRouteEnter (to, from, next) {
    next(vm => {
      vm.prevRoute = from
    })
  },
  methods: {
    login () {
      loginUser(this.email, this.password, this.prevRoute)
    }
  }
})
</script>
