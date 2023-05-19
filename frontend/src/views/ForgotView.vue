<template>
    <LoginTopBar :login="false"/>
  <!--
    Het eerste deel van de wachtwoord vergeten pagina waar het email adres ingevuld moet worden zodat de otp kan verstuurd
    worden.
  -->
  <v-card v-if="sendEmail" :flat="smallScreen" color="white" :class="`mx-auto mt-10 h-50 ${smallScreen ? 'w-100' : 'w-66'}`">
    <v-col class="align-center">
      <v-row class="justify-center my-5">
        <div class="text-h4 mx-auto">Wachtwoord vergeten?</div>
      </v-row>
      <v-form @submit.prevent :class="`${smallScreen ? 'w-75' : 'w-50'} mx-auto my-5`">
        <v-text-field v-model="email" label="e-mail" :error-messages="check_errors(this.errors, 'email')" clearable />
        <v-row class="justify-center my-2">
          <normal-button :parent-function="sendOtp" text="Wachtwoord opnieuw instellen"></normal-button>
        </v-row>
        <v-row class="justify-center my-2">
          <v-btn @click="goBack()" class="mx-auto" variant="flat" rounded >Terug</v-btn>
        </v-row>
      </v-form>
    </v-col>
  </v-card>
  <!--
    Tweede deel van de wachtwoord vergeten pagina waar de code en het nieuwe wachtwoord moeten ingegeven worden
  -->
  <v-card v-if="!sendEmail" :flat="smallScreen" color="white" :class="`mx-auto mt-10 ${smallScreen ? 'w-100' : 'w-66'}`">
    <v-col class="align-center">
      <v-row class="justify-center my-5">
        <div class="text-h4 mx-auto">Kies nieuw wachtwoord</div>
      </v-row>
      <v-form @submit.prevent :class="`${smallScreen ? 'w-75' : 'w-75'} mx-auto my-5`">
        <v-text-field
          v-model="email"
          :error-messages="check_errors(this.errors, 'email')"
          readonly
          :model-value="email"
          label="e-mail"
          variant="solo"
          append-icon="mdi-email"
          @click:append="sendOtp()"
        />
        <v-text-field v-model="otp" label="Code uit email"  :error-messages="check_errors(this.errors, 'otp')" clearable />
        <v-text-field
          v-model="password"
          :error-messages="check_errors(this.errors, 'password')"
          :append-inner-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append-inner="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          label="Nieuw wachtwoord"
        />
        <v-text-field
          v-model="password2"
          :error-messages="check_errors(this.errors, 'password2')"
          :append-inner-icon="value2 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append-inner="() => (value2 = !value2)"
          :type="value2 ? 'password' : 'text'"
          label="Bevestig wachtwoord"
        />
        <v-row class="justify-center my-2">
          <normal-button :parent-function="resetPassword" text="Nieuw wachtwoord opslaan"></normal-button>
        </v-row>
        <v-row class="justify-center my-5">
          <v-btn @click="goBack()" variant="flat" rounded >Terug</v-btn>
          <v-btn @click="sendOtp()">Verzend email opnieuw</v-btn>
        </v-row>
      </v-form>
    </v-col>
  </v-card>
</template>

<script>
import { defineComponent } from 'vue'
import router from '@/router'
import NormalButton from '@/components/NormalButton.vue'
import AuthService from "@/api/services/AuthService";
import {AuthForgotWrapper, AuthResetWrapper} from "@/api/wrappers/AuthWrappers";
import LoginTopBar from "@/components/LoginTopBar.vue";
import {check_errors, get_errors} from "@/error_handling";


export default defineComponent({
  name: 'ForgotView',
  components: {LoginTopBar, NormalButton },
  data: () => ({
    email: '',
    password: '',
    password2: '',
    value: 'password',
    value2: 'password',
    otp: '',
    prevRoute: '/',
    smallScreen: false,
    sendEmail: true,
    errors: null
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
      window.removeEventListener('resize', this.onResize)
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    check_errors,
    onResize () {
      this.smallScreen = window.innerWidth < 800
    },
    goBack () {
      this.errors = null
      if (this.sendEmail) {
        router.back()
      } else {
        this.sendEmail = true
      }
    },
    async sendOtp () {
      AuthService.forgot(new AuthForgotWrapper(this.email))
        .then(() => {
          this.sendEmail = false
          this.errors = null
        })
        .catch(async (error) => {
          this.errors = await get_errors(error)
        })
    },
    async resetPassword () {
      AuthService.reset(new AuthResetWrapper(
        this.email,
        this.password,
        this.password2,
        this.otp
      )).then(() => router.push({name : 'login' }))
        .catch(async (error) => {
          this.errors = await get_errors(error)
        })
    }
  }
})
</script>
