<template>
  <v-container>
    <v-card class='px-4'>
      <v-card-title align="center" class="bg-primary mt-2 rounded-xl">
        <v-img src="../assets/logo.png" height="75px" width="150px"></v-img>
      </v-card-title>
      <v-spacer></v-spacer>
      <v-card-text>
        <v-form ref='form' v-model='valid'>
          <v-row>
            <v-col cols='12' sm='6' md='6'>
              <v-text-field v-model='firstname' :rules='[rules.required]' label='Voornaam' required></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="6">
              <v-text-field v-model="lastname" :rules="[rules.required]" label="Achternaam" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="email" :rules="[rules.required]" label="E-mail" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="password" :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" :rules='[rules.required]' :type="showPassword ? 'text' : 'password'" label="Wachtwoord" counter @click:append="showPassword = !showPassword"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="password2" :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" :rules='[rules.required, passwordsMatch]' :type="showPassword ? 'text' : 'password'" label="Bevestig wachtwoord" counter @click:append="showPassword = !showPassword"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-autocomplete
                label="Locatie" :items="['Gent']" :rules="[rules.required]"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="gsm" :rules="[rules.required]" label="GSM-nummer" required></v-text-field>
            </v-col>
            <v-spacer></v-spacer>
            <v-col class="d-flex ml-auto" cols="12">
              <normal-button text="Registreer" v-bind:parent-function="validate" block></normal-button>
            </v-col>
          </v-row>
        </v-form>
        <v-row class="mx-auto justify-center mt-3 mb-1">
          <div class="mx-1">Reeds een account?</div>
          <router-link to="/login">Inloggen</router-link>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue'
import { requestWithBody } from '@/authorized'
import NormalButton from '@/components/NormalButton'

export default defineComponent({
  name: 'RegisterView',
  components: {
    NormalButton
  },
  data: () => ({
    valid: true,
    showPassword: false,
    firstname: '',
    lastname: '',
    email: '',
    password: '',
    password2: '',
    gsm: '',
    rules: {
      required: value => !!value || 'Dit veld is verplicht.'
    }
  }),
  methods: {
    passwordsMatch () { return this.password === this.password2 || 'Wachtwoorden komen niet overeen.' },
    async apiRegister () {
      const response = await requestWithBody('/api/register/', 'post', {
        email: this.email,
        first_name: this.firstname,
        last_name: this.lastname,
        password: this.password
      })
      console.log(response)
    },
    async validate () {
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        await this.apiRegister()
      }
    }
  }
})
</script>
