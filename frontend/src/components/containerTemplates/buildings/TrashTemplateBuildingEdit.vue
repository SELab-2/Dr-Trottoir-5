<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Pas de containers van dit gebouw aan.</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row
        v-if="building !== null"
        class="justify-space-between mx-auto"
      >
        <v-col cols='6' md='3' sm='3'>
          <p>{{ building.building.name }}</p>
        </v-col>
        <v-col cols='6' md='3' sm='3'>
          <p>{{ building.building.adres }}</p>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="trash_ids"
            :items="container_choices"
            chips
            :item-title="getLabel"
            item-value="extra_id"
            label="Kies containers voor dit gebouw"
            multiple
          />
        </v-col>
      </v-row>
      <StateButtons :status="status" :eenmalig="() => update(true)" :permanent="() => update(false)"/>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import BuildingContainer from "@/api/models/BuildingContainer";
import StateButtons from "@/components/StateButtons.vue";

export default {
  name: "TrashTemplateEditView",
  components: {StateButtons},
  data() {
    return {
      building: BuildingContainer,
      trash_ids: [],
      container_choices: [],
      status: "I"
    }
  },
  async beforeMount() {
    this.building = await RequestHandler.handle(
      TrashTemplateService.getBuildingOfTemplate(this.$route.params.id, this.$route.params.gebouwId), {
        id: 'getBuildingError',
        style: 'SNACKBAR'
      })
    this.trash_ids = this.building.trash_ids

    this.container_choices = await RequestHandler.handle(
      TrashTemplateService.getTrashContainersOfTemplate(this.$route.params.id), {
        id: 'getContainersForTemplateError',
        style: 'SNACKBAR'
      }).then(result => result).catch(() => []);

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
    getLabel(container) {
      const format_day = {
        "MO": "Maandag",
        "TU": "Dinsdag",
        "WE": "Woensdag",
        "TH": "Donderdag",
        "FR": "Vrijdag",
        "SA": "Zaterdag",
        "SU": "Zondag"
      }
      const format_type = {
        "PM": "PMD",
        "GL": "GLAS",
        "GF": "GFT",
        "RE": "REST",
        "PK": "PK"
      }
      if(!Number.isInteger(container)) {
        return `${format_type[container.trash_container.type]} ${format_day[container.trash_container.collection_day.day]}`
      }
    },
    async update(eenmalig) {
      if (!eenmalig) {
        RequestHandler.handle(TrashTemplateService.updateBuildingTemplate(this.$route.params.id, this.$route.params.gebouwId, {
          selection: this.trash_ids
        }), {
          id: 'updateSelectionToBuildingError',
          style: 'SNACKBAR'
        })
      } else {
        RequestHandler.handle(TrashTemplateService.updateBuildingTemplateEenmalig(this.$route.params.id, this.$route.params.gebouwId, {
          selection: this.trash_ids
        }), {
          id: 'updateSelectionToBuildingError',
          style: 'SNACKBAR'
        })
      }
      return await router.push({name: 'trashtemplates'})
    }
  }
}
</script>
