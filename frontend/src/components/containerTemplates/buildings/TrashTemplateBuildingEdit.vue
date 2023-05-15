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
        <v-col cols="12" md="3" sm="3">
          <v-checkbox v-model="permanent" label="Permanent"/>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="trash_ids"
            :items="container_choices"
            chips
            item-title="trash_container.type"
            item-value="extra_id"
            label="Kies containers voor dit gebouw"
            multiple
          />
        </v-col>
      </v-row>

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
import TrashTemplateService from "@/api/services/TrashTemplateService";
import trashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import Container from "@/api/models/Container";
import BuildingContainer from "@/api/models/BuildingContainer";

export default {
  name: "TrashTemplateEditView",
  components: {},
  props: {},
  data: () => ({
    permanent: true,
    building: <BuildingContainer>null,
    trash_ids: [],
    container_choices: <Container[]>[]
  }),
  async mounted() {
  },
  async beforeMount() {
    this.building = await RequestHandler.handle(
      trashTemplateService.getBuildingOfTemplate(this.$route.params.id, this.$route.params.gebouwId), {
        id: 'getBuildingError',
        style: 'SNACKBAR'
      })

    this.container_choices = await RequestHandler.handle(
      trashTemplateService.getTrashContainersOfTemplate(this.$route.params.id), {
        id: 'getContainersForTemplateError',
        style: 'SNACKBAR'
      }).then(result => result).catch(() => []);
  },
  methods: {
    async update() {
      if (this.permanent) {
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
