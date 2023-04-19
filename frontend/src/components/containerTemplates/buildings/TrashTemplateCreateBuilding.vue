<template>
  <v-row align="center" class="pt-10" justify="center">
    <h1>Nieuw gebouw aanmaken</h1>
  </v-row>
  <v-card :class="`mx-auto my-16 ${smallScreen ? 'w-100' : 'w-75'}`" color="white">
    <v-row align="center" class="xs-flex-column" justify="center">
      <v-col class="d-flex justify-lg-end align-center pt-10" col="12" lg="6">
        <h2>Naam</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <v-text-field v-model:model-value="name" class="text_field" variant="outlined"></v-text-field>
      </v-col>
      <v-col class="d-flex justify-lg-end align-center pt-10" col="12" lg="6">
        <h2>Adres</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <v-text-field v-model:model-value="adres" class="text_field" variant="outlined"></v-text-field>
      </v-col>
      <v-col class="d-flex justify-lg-end align-center pt-10" col="12" lg="6">
        <h2>Is dit een eenmalig gebouw?</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <input v-model="eenmalig" type="checkbox">
      </v-col>
      <v-col class="d-flex justify-lg-end align-center pt-10" col="12" lg="6">
        <h2>Locatie</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <v-select v-model="selectedLocation"
                  :items="locations"
                  class="text_field"
                  item-title="name"
                  item-value="id"
                  variant="solo"
        ></v-select>
      </v-col>
      <v-col class="d-flex justify-lg-end align-center pt-10" col="12" lg="6">
        <h2>Klanten nummer</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <v-text-field v-model:model-value="klant_nr" class="text_field" variant="outlined"></v-text-field>
      </v-col>
      <v-col class="d-flex justify-lg-end align-center pt-10" col="12" lg="6">
        <h2>Handleiding</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <v-file-input v-model="file" class="text_field" prepend-icon="mdi-file-upload-outline"
                      variant="outlined"></v-file-input>
      </v-col>
      <v-col class="d-flex justify-end align-center pt-10" col="12" lg="6">
        <h2>Geschatte tijd</h2>
      </v-col>
      <v-col class="d-flex justify-lg-start align-center" col="12" lg="6">
        <v-text-field v-model:model-value="time" class="text_field" placeholder="In minuten"
                      variant="outlined"></v-text-field>
      </v-col>
      <v-col class="d-flex justify-center align-center" col="12" lg="12">
        <normal-button :parent-function="createBuilding" text="Maak gebouw aan"></normal-button>
      </v-col>
      <v-col class="pt-5"></v-col>
    </v-row>
  </v-card>
</template>

<script>
import TrashTemplateService from '@/api/services/TrashTemplateService'
import NormalButton from '@/components/NormalButton'
import { RequestHandler } from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";
import { BuildingManualStatus } from "@/api/models/BuildingManualStatus";
import LocationService from "@/api/services/LocationService";

export default {
  name: 'TrashTemplateCreateBuilding',
  components: { NormalButton },
  props: {
    id: Number
  },
  data: () => {
    return {
      name: '',
      adres: '',
      klant_nr: null,
      file: null,
      time: null,
      smallScreen: false,
      locations: [],
      selectedLocation: '',
      eenmalig: false
    }
  },
  async beforeMount() {
    await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => {
        this.locations = result
      }
    )
  },
  methods: {
    addDropFile(e) {
      this.file = e.dataTransfer.files[0];
    },
    createBuilding() {

      // TODO Add geschatte tijd

      let body = {
        name: this.name,
        adres: this.adres,
        ivago_klantnr: this.klant_nr,
        manual: result['succes']['id'], //TODO just return in backend without succes
        location: this.selectedLocation
      }
      let error = {
        id: 'createBuildingError',
        style: 'SNACKBAR'
      }
      let then = () =>
        this.$store.dispatch("snackbar/open", {
          message: "Het gebouw is toegevoegd",
          color: "success"
        })

      if (this.eenmalig) {
        this.createManual().then(result =>
          RequestHandler.handle(
            TrashTemplateService.newBuildingToTemplateEenmalig(this.id, body), error
          ).then(then)
        )
      }else {
        this.createManual().then(result =>
          RequestHandler.handle(
            TrashTemplateService.newBuildingToTemplate(this.id, body), error
          ).then(then)
        )
      }
    },
    async createManual() {
      if (this.file === null) {
        return "Error"
      }
      return RequestHandler.handle(BuildingService.createManual(this.file[0], this.file[0].type,
        BuildingManualStatus.klaar
      ), {
        id: 'createManualError',
        style: "SNACKBAR"
      });
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

.drag_image {
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
</style>
