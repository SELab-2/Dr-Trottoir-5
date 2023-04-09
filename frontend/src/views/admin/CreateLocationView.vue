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
        <v-text-field class="text_field" variant="outlined" v-model="name"></v-text-field>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center pt-10 pb-10">
        <normal-button text="Voeg Locatie toe" :parent-function="addLocation"></normal-button>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";

export default {
  name: "CreateLocationView.vue",
  components: {NormalButton},
  data: () => {
    return {
      name: '',
    }
  },
  methods: {
    addLocation() {
      RequestHandler.handle(LocationService.createLocation({
          name: this.name
        }
      ), {
        id: 'createLocationError',
        style: 'SNACKBAR'
      }).then(() =>

        this.$store.dispatch("snackbar/open", {
          message: "De locatie is toegevoegd",
          color: "success"
        })
      );
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
