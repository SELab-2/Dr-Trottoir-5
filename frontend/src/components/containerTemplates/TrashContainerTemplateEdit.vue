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
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="chosen_buildings"
            :items="building_choices"
            chips
            item-title="name"
            item-value="id"
            label="Gekozen gebouwen"
            multiple
          ></v-select>
        </v-col>
      </v-row>

      <div v-if="chosen_buildings.length > 0">
        <v-row
          v-for="gebouw in to_show()"
          :key="gebouw.building.id"
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
      </div>

      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="update()">Aanpassen</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import trashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import buildingService from "@/api/services/BuildingService";

import BuildingContainer from "@/api/models/BuildingContainer";
import Container from "@/api/models/Container";

export default {
  name: "TrashContainerTemplateEditView",
  components: {},
  props: {},
  data: () => ({
    name: '',
    even: true,
    permanent: true,
    location: null,
    locations: [],
    buildings: <BuildingContainer[]>[],
    chosen_buildings: [],
    original_buildings: [],
    building_choices: <BuildingContainer[]>[],
    container_choices: <Container[]>[],
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
    this.buildings = trashTemplate.buildings
    this.chosen_buildings = this.buildings.map(b => b.building.id)

    // get all possible buildings
    this.building_choices = await RequestHandler.handle(buildingService.getBuildings(), {
      id: 'getbuildingsError',
      style: 'SNACKBAR'
    }).then(result => {
      return result.map(res => res)
    }).catch(() => []);

    this.container_choices = await RequestHandler.handle(
      trashTemplateService.getTrashContainersOfTemplate(this.$route.params.id), {
        id: 'getContainersForTemplateError',
        style: 'SNACKBAR'
      }).then(result => result).catch(() => []);

    for (const building of this.buildings) {
      building.trash_ids.map(id => this.container_choices.filter(con => con.extra_id === id)[0])
    }
  },
  methods: {

    to_show(): BuildingContainer[] {
      return this.buildings.filter(b => this.chosen_buildings.includes(b.building.id))
    },

    async update() {
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
        /* Update or make the chosen buildings */
        this.chosen_buildings.forEach((building_id) => {
          if (this.buildings.map(b => b.building.id).includes(building_id)) {
            const building = this.buildings.filter(b => b.building.id === building_id)[0]
            RequestHandler.handle(TrashTemplateService.updateBuildingTemplate(this.$route.params.id, building_id, {
              selection: building.trash_ids
            }), {
              id: 'updateSelectionToBuildingError',
              style: 'SNACKBAR'
            })
          }
        })

        /* Delete buildings that were removed from the list */
        this.buildings.forEach((building) => {
          if (!this.chosen_buildings.includes(building.building.id)){
            RequestHandler.handle(TrashTemplateService.deleteBuildingTemplate(this.$route.params.id, building.building.id), {
              id: 'deletebuildingError',
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
