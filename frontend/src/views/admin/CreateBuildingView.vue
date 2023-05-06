<template>
  <v-row justify="center" align="center" class="pt-10">
    <h1>Nieuw gebouw aanmaken</h1>
  </v-row>
  <v-card color="white" :class="`mx-auto my-16 ${smallScreen ? 'w-100' : 'w-75'}`">
    <v-row align="center" justify="center" class="xs-flex-column">
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Naam</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field class="text_field" :error-messages="check_errors(this.errors, 'name')" variant="outlined" v-model:model-value="name"></v-text-field>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Adres</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field class="text_field" variant="outlined" :error-messages="check_errors(this.errors, 'adres')" v-model:model-value="adres"></v-text-field>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Locatie</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-select class="text_field"
                  :error-messages="check_errors(this.errors, 'location')"
                  variant="solo"
                  :items="locations"
                  item-title="name"
                  item-value="id"
                  v-model="selectedLocation"
        ></v-select>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Klanten nummer</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field class="text_field" variant="outlined" :error-messages="check_errors(this.errors, 'ivago_klantnr')" v-model:model-value="klant_nr"></v-text-field>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Handleiding</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-file-input v-model="file" :error-messages="check_errors(this.errors, 'manual')" prepend-icon="mdi-file-upload-outline" class="text_field"
                      variant="outlined"></v-file-input>
      </v-col>
      <!---
      TODO Milestone 3
      <v-col col="12" lg="6" class="d-flex justify-end align-center pt-10">
        <h2>Geschatte tijd</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field placeholder="In minuten" class="text_field" variant="outlined"
                      v-model:model-value="time"></v-text-field>
      </v-col>
      ---->
      <v-col col="12" lg="12" class="d-flex justify-center align-center">
        <normal-button text="Maak gebouw aan" :parent-function="createBuilding"></normal-button>
      </v-col>
      <v-col class="pt-5"></v-col>
    </v-row>
  </v-card>
</template>

<script>
import NormalButton from '@/components/NormalButton'
import {RequestHandler} from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";
import {BuildingManualStatus} from "@/api/models/BuildingManualStatus";
import LocationService from "@/api/services/LocationService";
import router from "@/router";
import {check_errors, get_errors} from "@/error_handling";

export default {
  name: 'CreateBuildingView',
  components: {NormalButton},
  data: () => {
    return {
      name: '',
      adres: '',
      klant_nr: null,
      file: null,
      // time: null, TODO Milestone 3
      smallScreen: false,
      locations: [],
      selectedLocation: null,
      errors: null
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
    check_errors,
    async createBuilding() {
      // TODO Milestone 3 Add geschatte tijd
      const manual = await this.createManual()

      BuildingService.createBuilding({
        name: this.name,
        adres: this.adres,
        ivago_klantnr: this.klant_nr,
        manual: manual['id'],
        location: this.selectedLocation
      })
      .then(() => {
        this.errors = null;
        this.$store.dispatch("snackbar/open", {
          message: "Het gebouw is toegevoegd",
          color: "success"
        })
        router.push({name: 'buildings'})
      }).catch(async (error) => this.errors = await get_errors(error));

    },
    async createManual() {
      if (this.file === null || this.file.length === 0) {
        return "Error"
      }
      return RequestHandler.handle(BuildingService.createManual(this.file[0], this.file[0].type,
        BuildingManualStatus.klaar
      ), {
        id: 'createManualError',
        style: "SNACKBAR",
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
