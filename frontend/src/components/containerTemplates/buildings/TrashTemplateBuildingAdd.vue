<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Kies gebouwen voor deze template</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md="9" sm="9">
          <v-select
            v-model="building_chosen"
            :items="building_options"
            chips
            item-title="name"
            item-value="id"
            label="Gekozen gebouwen"
            multiple
          />
        </v-col>
        <v-col cols='12' md="3" sm="3">
          <v-checkbox v-model="permanent" label="Permanent"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="aanpassen()">Aanpassen</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import buildingService from "@/api/services/BuildingService";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import trashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";

export default {
  name: "TrashTemplateBuildingAdd",

  components: {},
  props: {},
  data() {
    return {
      building_options: [],
      building_chosen: [],
      building_originals: [],
      permanent: true
    }
  },

  async beforeMount() {
    this.building_options = await RequestHandler.handle(buildingService.getBuildings(), {
      id: 'getbuildingsError',
      style: 'SNACKBAR'
    }).then(result => result);

    this.building_originals = await RequestHandler.handle(trashTemplateService.getBuildingsOfTemplate(this.$route.params.id), {
      id: 'getBuildingsFromTemplateError',
      style: 'SNACKBAR'
    }).then((result) => {
      return result.map(buildingContainer => buildingContainer.building.id)
    })
    this.building_chosen = this.building_originals
  },

  methods: {
    async aanpassen() {
      console.log(this.building_originals)
      console.log(this.building_chosen)
      /* Al de gebouwen die niet in de originele lijst zaten en dus nieuw toegevoegd moeten worden. */
      this.building_chosen.forEach(building_id => {
        if (!this.building_originals.includes(building_id)) {
          if (this.permanent) {
            RequestHandler.handle(TrashTemplateService.newBuildingToTemplate(this.$route.params.id, {
              building: building_id,
              selection: []
            }), {
              id: 'addNewBuildingError',
              style: 'SNACKBAR'
            })
          } else {
            RequestHandler.handle(TrashTemplateService.newBuildingToTemplateEenmalig(this.$route.params.id, {
              building: building_id,
              selection: []
            }), {
              id: 'addNewBuildingError',
              style: 'SNACKBAR'
            })
          }
        }
      })
      /* Al de gebouwen die niet in de geselecteerde lijst zitten en dus verwijderd moeten worden. */
      this.building_originals.forEach((building) => {
        if (!this.building_chosen.includes(building)) {
          RequestHandler.handle(TrashTemplateService.deleteBuildingTemplate(this.$route.params.id, building), {
            id: 'deletebuildingError',
            style: 'SNACKBAR'
          })
        }
      })
      return await router.push({name: 'trashtemplateBuildings', params: {id: this.$route.params.id}})
    }
  }

}
</script>

<style scoped>

</style>
