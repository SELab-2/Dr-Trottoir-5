<template>
  <v-container>
    <v-col class="align-center py-8">
      <v-sheet class="mx-auto rounded-xl w-75" color="black">
        <v-img src="../assets/logo.png" class="mx-auto w-75"/>
      </v-sheet>
      <v-form @submit.prevent class="mx-auto w-50 my-8">
        <v-text-field
          v-model="email"
          label="e-mail"
        ></v-text-field>
        <v-text-field
          v-model="password"
          type="password"
          label="Wachtwoord"
        ></v-text-field>
        <div class="error" v-if="error !== ''">{{error.message}}</div>
        <router-link to="/forgot">Wachtwoord vergeten?</router-link>
        <v-btn @click="login" block class="mt-2">Login</v-btn>
      </v-form>
      <v-row class="mx-auto justify-center">
        <div class="mx-2">Geen account?</div>
        <router-link to="/register">Maak nieuw account</router-link>
      </v-row>
    </v-col>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue'
import { loginUser } from '@/authorized'

export default defineComponent({
  name: 'LoginView',
  data: () => ({
    email: '',
    password: '',
    error: '',
    prevRoute: '/'
  }),
  beforeRouteEnter (to, from, next) {
    next(vm => {
      if (from !== undefined) {
        vm.prevRoute = from.path
      }
    })
  },
  methods: {
    async login () {
      this.error = await loginUser(this.email, this.password, this.prevRoute)
    }
  }
})
</script>
