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
      </v-row>
      <StateButtons :status="status" :eenmalig="() => aanpassen(true)" :permanent="() => aanpassen(false)"/>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import buildingService from "@/api/services/BuildingService";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import StateButtons from "@/components/StateButtons.vue";

export default {
  name: "TrashTemplateBuildingAdd",

  components: {StateButtons},
  props: {},
  data() {
    return {
      building_options: [],
      building_chosen: [],
      building_originals: [],
      status: "I"
    }
  },

  async beforeMount() {
    this.building_options = await RequestHandler.handle(buildingService.getBuildings(), {
      id: 'getbuildingsError',
      style: 'SNACKBAR'
    }).then(result => result);

    this.building_originals = await RequestHandler.handle(TrashTemplateService.getBuildingsOfTemplate(this.$route.params.id), {
      id: 'getBuildingsFromTemplateError',
      style: 'SNACKBAR'
    }).then((result) => {
      return result.map(buildingContainer => buildingContainer.building.id)
    })
    this.building_chosen = this.building_originals

    RequestHandler.handle(
      TrashTemplateService.getTrashTemplate(this.$route.params.id),
      {
        id: 'getTrashtemplateError',
        style: 'SNACKBAR'
      }
    ).then(result => {
      this.status = result.status
    })
  },

  methods: {
    async aanpassen(eenmalig) {

      /* Al de gebouwen die niet in de originele lijst zaten en dus nieuw toegevoegd moeten worden. */
      this.building_chosen.forEach(building_id => {
        if (!this.building_originals.includes(building_id)) {
          if (!eenmalig) {
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
