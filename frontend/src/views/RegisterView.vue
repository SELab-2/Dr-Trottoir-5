<template>
  <LoginTopBar :login="false"/>
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
              <v-text-field v-model='firstname' :error-messages="check_errors(this.errors, 'firstname')" label='Voornaam' required></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="6">
              <v-text-field v-model="lastname" :error-messages="check_errors(this.errors, 'lastname')" label="Achternaam" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="email" :error-messages="check_errors(this.errors, 'email')" label="E-mail" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="password" :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" :error-messages="check_errors(this.errors, 'password')" :type="showPassword ? 'text' : 'password'" label="Wachtwoord" counter @click:append="showPassword = !showPassword"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="password2" :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" :error-messages="check_errors(this.errors, 'password2')" :type="showPassword ? 'text' : 'password'" label="Bevestig wachtwoord" counter @click:append="showPassword = !showPassword"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-autocomplete
                label="Locatie" :items="['Gent']" :error-messages="check_errors(this.errors, 'location')"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="phone_nr" :error-messages="check_errors(this.errors, 'phone_nr')" label="GSM-nummer" required></v-text-field>
            </v-col>
            <v-spacer></v-spacer>
            <v-col class="d-flex ml-auto" cols="12">
              <normal-button text="Registreer" v-bind:parent-function="apiRegister" block></normal-button>
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

<script lang="ts">
import {defineComponent} from 'vue';
import AuthService from '@/api/services/AuthService';
import {AuthRegisterWrapper} from '@/api/wrappers/AuthWrappers';
import NormalButton from '@/components/NormalButton.vue';
import LoginTopBar from "@/components/LoginTopBar.vue";
import router from '@/router';
import {check_errors, get_errors} from "@/error_handling";

export default defineComponent({
  name: 'RegisterView',
  components: {
    LoginTopBar,
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
    phone_nr: '',
    errors: null
  }),
  methods: {
    check_errors,
    async apiRegister () {
      const wrapper = new AuthRegisterWrapper(
        this.email,
        this.password,
        this.password2,
        this.firstname,
        this.lastname,
        this.phone_nr
      );

      AuthService.register(wrapper).then(async () => {
        // Send confirmation message.
        this.$store.dispatch("snackbar/open", {
          message: "Registreren gelukt",
          color: "success"
        });

        // Update the current user inside the store.
        await this.$store.dispatch("session/clear");
        await this.$store.dispatch("session/fetch");

        await router.push({ name: 'home' });
      }).catch(async (error) => {this.errors = await get_errors(error)});
    }
  }
})
</script>
