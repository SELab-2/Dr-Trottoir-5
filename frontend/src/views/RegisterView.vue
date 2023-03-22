<template>
  <v-container>
    <v-card class='px-4'>
      <v-card-title align="center" class="bg-primary mt-2">
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
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue'
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
    gsm: '',
    rules: {
      required: value => !!value || 'Dit veld is verplicht.'
    }
  }),
  methods: {
    async apiRegister () {
      const response = await fetch('https://sel2-5.ugent.be/api/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
      }).catch(error => error)
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
