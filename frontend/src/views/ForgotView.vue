<template>
  <v-card v-if="sendEmail" :flat="smallScreen" color="white" :class="`mx-auto mt-10 h-50 ${smallScreen ? 'w-100' : 'w-66'}`">
    <v-col class="align-center">
      <v-row class="justify-center my-5">
        <div class="text-h4 mx-auto">Wachtwoord vergeten?</div>
      </v-row>
      <v-form @submit.prevent :class="`${smallScreen ? 'w-75' : 'w-50'} mx-auto my-5`">
        <v-text-field v-model="email" label="e-mail" clearable />
        <v-row class="justify-center my-2">
          <normal-button :parent-function="sendOtp" text="Wachtwoord opnieuw instellen"></normal-button>
        </v-row>
        <v-row class="justify-center my-2">
          <v-btn @click="goBack()" class="mx-auto" variant="flat" rounded >Terug</v-btn>
        </v-row>
      </v-form>
    </v-col>
  </v-card>
  <v-card v-if="!sendEmail" :flat="smallScreen" color="white" :class="`mx-auto mt-10 ${smallScreen ? 'w-100' : 'w-66'}`">
    <v-col class="align-center">
      <v-row class="justify-center my-5">
        <div class="text-h4 mx-auto">Kies nieuw wachtwoord</div>
      </v-row>
      <v-form @submit.prevent :class="`${smallScreen ? 'w-75' : 'w-75'} mx-auto my-5`">
        <v-text-field
          v-model="email"
          readonly
          :model-value="email"
          label="e-mail"
          variant="solo"
          suffix="Verzend opnieuw"
          append-icon="mdi-email"
          @click:append="sendOtp()"
        />
        <v-text-field v-model="otp" label="Code uit email" clearable />
        <v-text-field
          v-model="password"
          :append-inner-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append-inner="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          label="Nieuw wachtwoord"
        />
        <v-text-field
          v-model="password2"
          :append-inner-icon="value2 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append-inner="() => (value2 = !value2)"
          :type="value2 ? 'password' : 'text'"
          label="Tweede keer nieuw wachtwoord"
        />
        <v-row class="justify-center my-2">
          <normal-button text="Nieuw wachtwoord opslaan"></normal-button>
        </v-row>
        <v-row class="justify-center my-5">
          <v-btn @click="goBack()" variant="flat" rounded >Terug</v-btn>
          <v-btn>Verzend email opnieuw</v-btn>
        </v-row>
      </v-form>
    </v-col>
  </v-card>
</template>

<script>
import { defineComponent } from 'vue'
import router from '@/router'
import NormalButton from '@/components/NormalButton.vue'

export default defineComponent({
  name: 'ForgotView',
  components: { NormalButton },
  data: () => ({
    email: '',
    password: '',
    value: 'password',
    value2: 'password',
    password2: '',
    otp: '',
    prevRoute: '/',
    smallScreen: false,
    sendEmail: true
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
    onResize () {
      this.smallScreen = window.innerWidth < 800
    },
    goBack () {
      if (this.sendEmail) {
        router.back()
      } else {
        this.sendEmail = true
      }
    },
    sendOtp () {
      this.sendEmail = false
    }
  }
})
</script>
