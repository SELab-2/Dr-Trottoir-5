<template>
  <v-card :class="`mx-auto my-16 h-75 ${smallScreen ? 'w-100' : 'w-75'}`" :flat="smallScreen" color="white">
    <v-col class="align-center py-8">
      <v-card-title align="center" class="bg-primary mt-2 rounded-xl">
        <v-img src="../assets/logo.png" height="75px" width="150px"></v-img>
      </v-card-title>
      <v-form :class="`${smallScreen ? ' w-100' : 'w-50'} mx-auto my-5`" @submit.prevent>
        <v-text-field
          v-model="email"
          label="e-mail"
        ></v-text-field>
        <v-text-field
          v-model="password"
          label="Wachtwoord"
          type="password"
        ></v-text-field>
        <div v-if="error !== ''" class="text-red">{{ error.message }}</div>
        <router-link to="/forgot">Wachtwoord vergeten?</router-link> <!-- TODO /FORGOT page -->
        <normal-button text="Login" v-bind:parent-function="login" block class="mt-2"></normal-button>
      </v-form>
      <v-row class="mx-auto justify-center">
        <div class="mx-2">Geen account?</div>
        <router-link to="/register">Maak nieuw account</router-link>
      </v-row>
    </v-col>
  </v-card>
</template>

<script>
import { ErrorHandler } from '@/api/error/ErrorHandler'
import AuthService from '@/api/services/AuthService'
import router from '@/router'
import { defineComponent } from 'vue'
import NormalButton from '@/components/NormalButton'

export default defineComponent({
  name: 'LoginView',
  data: () => ({
    email: '',
    password: '',
    error: '',
    prevRoute: '/',
    smallScreen: false
  }),
  components: {
    NormalButton
  },
  beforeRouteEnter(to, from, next) {
    // save the previous path so we can return after the login is done
    next(vm => {
      if (from !== undefined) {
        vm.prevRoute = from.path
      }
    })
  },
  beforeUnmount() {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.onResize, { passive: true })
    }
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    login() {
      AuthService.login({ email: this.email, password: this.password })
        .then(
          (data) => {

            // Send confirmation message.
            this.$store.dispatch("snackbar/open", {
              message: "Successfully logged in",
              color: "success"
            });

            // Clear locally stored user
            this.$store.dispatch("session/clearStorage");

            // Update the current user inside the store.
            this.$store.dispatch("session/fetch");

            router.push({ path: '/' })
          }
        ).catch((error) => {

        ErrorHandler.handle(
          error,
          {
            id: "login",
            style: "SNACKBAR"
          },
          this.fields
        );
      })
    },
    onResize() {
      this.smallScreen = window.innerWidth < 500
    }
  }
})
</script>
