<template>
  <v-row justify="center" align="center" class="pt-10">
    <h1>Nieuwe locatie aanmaken</h1>
  </v-row>
  <v-card color="white" class="mx-auto my-16 w-75">
    <v-row>
      <v-col lg="6" md="6" class="d-flex align-center justify-end pt-10">
        <h1>Naam</h1>
      </v-col>
      <v-col lg="6" md="6" class="d-flex align-center justify-start">
        <v-text-field class="text_field" variant="outlined" :error-messages="check_errors(this.errors, 'name')" v-model="name"></v-text-field>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center pt-10 pb-10">
        <normal-button text="Voeg locatie toe" :parent-function="addLocation"></normal-button>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import LocationService from "@/api/services/LocationService";
import {check_errors, get_errors} from "@/error_handling";

export default {
  name: "CreateLocationView.vue",
  components: {NormalButton},
  data: () => {
    return {
      name: '',
      errors: null
    }
  },
  methods: {
    check_errors,
    addLocation() {
      LocationService.createLocation({
          name: this.name
        }
      ).then(() => {
        this.errors = null;
        this.$store.dispatch("snackbar/open", {
          message: "De locatie is toegevoegd",
          color: "success"
        })
      }
      ).catch(async (error) => this.errors = await get_errors(error));
    }
  }
}
</script>
<style>
.text_field {
  height: 40px;
  max-width: 350px;
  padding-left: 5px;
  padding-top: 5px;
}
</style>
