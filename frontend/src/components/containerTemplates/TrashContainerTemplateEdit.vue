<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Pas de template aan.</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-text-field v-model='name' label='Naam' required></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-checkbox v-model="even" label="Even"></v-checkbox>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-checkbox v-model="permanent" label="Permanent"></v-checkbox>
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
      </v-row>

      <v-row
        v-for="gebouw in this.buildings"
        class="justify-space-between mx-auto"
      >
        <v-col cols='6' md='3' sm='3'>
          <p>{{ gebouw.building.name }}</p>
        </v-col>
        <v-col cols='6' md='3' sm='3'>
          <p>{{ gebouw.building.adres }}</p>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="gebouw.trash_ids"
            :items="container_choices"
            chips
            item-title="trash_container.type"
            item-value="extra_id"
            label="Kies containers voor dit gebouw"
            multiple
          ></v-select>
        </v-col>
      </v-row>

      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="create()">Aanpassen</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import NormalButton from "@/components/NormalButton.vue";
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import trashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import buildingService from "@/api/services/BuildingService";

export default {
  name: "TrashContainerTemplateEditView",
  components: {
    NormalButton
  },
  props: {},
  data: () => ({
    name: '',
    even: true,
    permanent: true,
    location: null,
    locations: [],
    buildings: [],
    original_buildings: [],
    building_choices: [],
    container_choices: [],
  }),
  async mounted() {
  },
  async beforeMount() {
    // get all possible locations
    this.locations = await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

    const trashTemplate = await RequestHandler.handle(trashTemplateService.getTrashTemplate(this.$route.params.id), {
      id: 'getTemplateEditError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => null)

    this.name = trashTemplate.name
    this.even = trashTemplate.even
    this.location = trashTemplate.location
    this.original_buildings = trashTemplate.buildings
    this.buildings = trashTemplate.buildings
    console.log(this.buildings)

    // get all possible buildings
    this.building_choices = await RequestHandler.handle(buildingService.getBuildings(), {
      id: 'getbuildingsError',
      style: 'SNACKBAR'
    }).then(result => {
      return result.map(res => {
        return {
          building: res,
          trash_ids: []
        }
      })
    }).catch(() => []);

    this.container_choices = await RequestHandler.handle(
      trashTemplateService.getTrashContainersOfTemplate(this.$route.params.id), {
        id: 'getContainersForTemplateError',
        style: 'SNACKBAR'
      }).then(result => result.map(con => con.extra_id)).catch(() => []);

  },
  methods: {
    async create() {
      const body = {
        name: this.name,
        even: this.even,
        location: this.location,
        permanent: this.permanent
      }
      const response = await RequestHandler.handle(TrashTemplateService.updateTrashTemplate(this.$route.params.id, body), {
        id: 'CreateNewTrashTemplateError',
        style: 'SNACKBAR'
      }).then(result => {
        this.buildings.forEach((building) => {
          console.log(building)
          if (building.building.id in this.original_buildings.map(b => b.building.id)){
            RequestHandler.handle(TrashTemplateService.updateBuildingTemplate(this.$route.params.id, {
              building: building.building.id,
              selection: building.trash_ids
            }), {
              id: 'updateSelectionToBuildingError',
              style: 'SNACKBAR'
            })
          } else {
            RequestHandler.handle(TrashTemplateService.newBuildingToTemplate(this.$route.params.id, {
              building: building.building.id,
              selection: building.trash_ids
            }), {
              id: 'addSelectionToBuildingError',
              style: 'SNACKBAR'
            })
          }

        })
        return result
      });
      return await router.push({name: 'trashtemplates'})
    }
  }
}
</script>
