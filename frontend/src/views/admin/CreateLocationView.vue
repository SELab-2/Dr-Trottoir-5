<template>
  <v-row>
    <v-col>
      <h1>Naam</h1>
    </v-col>
    <v-col>
      <v-text-field variant="outlined" v-model="name"></v-text-field>
    </v-col>
    <v-col>
      <normal-button text="Voeg Locatie toe" :parent-function="addLocation"></normal-button>
    </v-col>
  </v-row>
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
      name: ''
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
