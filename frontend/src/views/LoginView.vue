<template>
  <LoginTopBar :login="true"/>
  <v-card :class="`mx-auto my-16 h-75 ${smallScreen ? 'w-100' : 'w-75'}`" :flat="smallScreen" color="white">
    <v-col class="align-center py-8">
      <v-card-title align="center" class="bg-primary mt-2 rounded-xl">
        <v-img src="../assets/logo.png" height="75px" width="150px"></v-img>
      </v-card-title>
      <v-form :class="`${smallScreen ? ' w-100' : 'w-50'} mx-auto my-5`" @submit.prevent>
        <v-text-field
          v-model="email"
          label="e-mail"
          :error-messages="check_errors('email')"
        ></v-text-field>
        <v-text-field
          v-model="password"
          :error-messages="check_errors('password')"
          :append-inner-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append-inner="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          label="Wachtwoord"
        ></v-text-field>
        <router-link to="/forgot">Wachtwoord vergeten?</router-link>
        <normal-button text="Login" v-bind:parent-function="login" block class="mt-2"></normal-button>
      </v-form>
      <v-row class="mx-auto justify-center">
        <div class="mx-2">Geen account?</div>
        <router-link :to="{name: 'register'}">Maak nieuw account</router-link>
      </v-row>
    </v-col>
  </v-card>
</template>

<script>
import AuthService from '@/api/services/AuthService'
import router from '@/router'
import { defineComponent } from 'vue'
import NormalButton from '@/components/NormalButton'
import LoginTopBar from "@/components/LoginTopBar.vue";


export default defineComponent({
  name: 'LoginView',
  data: () => ({
    email: '',
    value: 'password',
    password: '',
    prevRoute: '/',
    smallScreen: false,
    errors: null
  }),
  components: {
    NormalButton,
    LoginTopBar
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
      window.removeEventListener('resize', this.onResize)
    }
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    check_errors(fieldname) {
      if (this.errors === null) return "";
      for (const error of this.errors) {
        if (error.field === fieldname) {
          return error.message;
        }
      }
      return "";
    },
    login() {
      AuthService.login({ email: this.email, password: this.password })
       .then(
         async () => {

           // Send confirmation message.
           this.$store.dispatch("snackbar/open", {
             message: "U bent ingelogd",
             color: "success"
           });

           // Update the current user inside the store.
           await this.$store.dispatch("session/clear");
           await this.$store.dispatch("session/fetch");

           await router.push({ name: 'home' });
         }
       ).catch(async (error) => {
        this.errors = error.json ? await error.json().then(res => res.errors).catch(() => null) : null;
     })
   },
   onResize() {
     this.smallScreen = window.innerWidth < 600
   }
 }
})
</script>
