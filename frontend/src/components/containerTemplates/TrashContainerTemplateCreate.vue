<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Maak een nieuwe template aan</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-text-field v-model='name' label='Naam' required></v-text-field>
        </v-col>
        <v-col cols="12" md="6" sm="6">
          <v-checkbox v-model="even" label="Even"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="location"
            :items="locations"
            item-title="name"
            item-value="id"
            label="Locatie"
          ></v-select>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="buildings"
            :items="building_choices"
            item-title="name"
            item-value="id"
            label="Kies gebowen"
            multiple="true"
            chips="true"
          ></v-select>
        </v-col>
      </v-row>

      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="create()">Aanmaken</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import buildingService from "@/api/services/BuildingService";

export default {
  name: "TrashContainerTemplateCreateView",
  data: () => ({
    name: '',
    even: true,
    location: null,
    locations: [],
    buildings: null,
    building_choices: []
  }),
  async beforeMount() {
    // get all possible locations
    this.locations = await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

    // get all possible buildings
    this.building_choices = await RequestHandler.handle(buildingService.getBuildings(), {
      id: 'getbuildingsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);
  },
  methods: {
    async create() {
      const body = {
        name: this.name,
        even: this.even,
        location: this.location
      }
      const response = await RequestHandler.handle(TrashTemplateService.newTrashTemplate(body), {
        id: 'CreateNewTrashTemplateError',
        style: 'SNACKBAR'
      }).then(result => {
        this.building_choices.forEach((building) => {
          RequestHandler.handle(TrashTemplateService.newBuildingToTemplate(result.id, {
            building: building.id,
            selection: [] //TODO ADD THE SELECTED TRASHCANS
          }), {
            id: 'addBuildingError',
            style: 'SNACKBAR'
          }).then((result) => {
            console.log("done")
          })
        })
        return result
      });
      return await router.push({name: 'trashtemplates'})
    }
  }
}
</script>
