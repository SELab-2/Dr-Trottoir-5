<template>
  <v-card :flat="smallScreen" color="white" :class="`mx-auto my-16 h-75 ${smallScreen ? 'w-100' : 'w-75'}`">
    <v-col class="align-center py-8">
      <v-sheet :class="`mx-auto rounded-xl ${smallScreen ? ' w-100' : 'w-75'}`" color="black">
        <v-img src="../assets/logo.png" :class="`mx-auto ${smallScreen ? ' w-100' : 'w-75'}`"/>
      </v-sheet>
      <v-form @submit.prevent :class="`${smallScreen ? ' w-100' : 'w-50'} mx-auto my-5`">
        <v-text-field v-model="email" label="e-mail" />
        <v-text-field v-model="password" type="password" label="Wachtwoord" />
        <div class="text-red" v-if="error !== ''">{{error.message}}</div>
        <router-link to="/forgot">Wachtwoord vergeten?</router-link>
        <v-btn @click="login" block class="mt-2">Login</v-btn>
      </v-form>
      <v-row class="mx-auto justify-center">
        <div class="mx-2">Geen account?</div>
        <router-link to="/register">Maak nieuw account</router-link>
      </v-row>
    </v-col>
  </v-card>
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
    prevRoute: '/',
    smallScreen: false
  }),
  beforeRouteEnter (to, from, next) {
    // save the previous path so we can return after the login is done
    next(vm => {
      if (from !== undefined) {
        vm.prevRoute = from.path
      }
    })
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
    async login () {
      this.error = await loginUser(this.email, this.password, this.prevRoute)
    },
    onResize () {
      this.smallScreen = window.innerWidth < 500
    }
  }
})
</script>
