<template>
  <v-row justify="center" align="center" class="pt-10">
    <h1>Nieuw gebouw aanmaken</h1>
  </v-row>
  <v-card color="white" :class="`mx-auto my-10 py-5 w-75`">
    <v-row class="justify-space-between mx-auto">
      <v-col cols='12' sm='6' md='6'>
        <v-text-field v-model='name' :error-messages="check_errors(this.errors, 'name')" label='Naam' required></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6">
        <v-text-field :error-messages="check_errors(this.errors, 'adres')" v-model="adres" label="Adres"></v-text-field>
      </v-col>
    </v-row>
    <v-row class="justify-space-between mx-auto">
      <v-col cols='12' sm='6' md='6'>
        <v-select label="Locatie"
                  :error-messages="check_errors(this.errors, 'location')"
                  variant="solo"
                  :items="locations"
                  item-title="name"
                  item-value="id"
                  v-model="selectedLocation"
        ></v-select>
      </v-col>
      <v-col cols="12" sm="3" md="3">
        <v-text-field label="Klanten nummer" :error-messages="check_errors(this.errors, 'ivago_klantnr')" v-model="klant_nr"></v-text-field>
      </v-col>
      <v-col cols="12" sm="3" md="3">
        <v-file-input label="Handleiding" v-model="file" :error-messages="check_errors(this.errors, 'manual')" prepend-icon="mdi-file-upload-outline" ></v-file-input>
      </v-col>
    </v-row>
    <v-row align="center" justify="center" class="xs-flex-column">
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
      }).catch(async (error) => {this.errors = await get_errors(error)});

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

</style>
