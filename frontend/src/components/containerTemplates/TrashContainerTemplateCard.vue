<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p>{{ this.data.name }}</p>
      </v-col>
      <v-col cols="2">
        <p class="text-style-url" @click="goToTrashTemplateContainersPage">Zie Vuilnisbakken</p>
      </v-col>
      <v-col cols="2">
        <p class="text-style-url" @click="goToTrashTemplateBuildingsPage">Zie Gebouwen</p>
      </v-col>
      <v-col cols="1">
        {{ status_mapping[this.data.status] }}
      </v-col>
      <v-col cols="1">
        {{ this.locatie }}
      </v-col>
      <v-col cols="1">
        {{ this.data.even }}
      </v-col>
      <v-col class="text-right" cols="2">
        <v-btn class="button-style" icon v-on:click="deleteTemplate">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import TrashTemplate from '@/api/models/TrashTemplate'
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import EditIcon from '@/components/icons/EditIcon.vue'
import router from '@/router'
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import TrashTemplateService from "@/api/services/TrashTemplateService";

export default {
  name: 'TrashContainerTemplateCard',
  components: {DeleteIcon},
  props: {
    data: {
      type: TrashTemplate,
    }
  },
  data: () => ({
    locations: [],
    locatie: "",
    status_mapping: {
      "A": "Actief",
      "E": "Eenmalig",
      "V": "Vervangen"
    }
  }),
  methods: {
    editTemplate: function () {
      router.push({
        name: 'editTrashtemplates',
        params: {id: this.data.id}
      });
    },
    deleteTemplate: function () {
      RequestHandler.handle(TrashTemplateService.deleteTrashTemplate(this.data.id), {
        id: 'deleteTrashTemplateError',
        style: 'SNACKBAR'
      }).then(() => {
        router.go(0) // refresh the page
      })
    },
    goToTrashTemplateBuildingsPage: function () {
      router.push({
        name: 'trashtemplateBuildings',
        params: {id: this.data.id}
      });
    },
    goToTrashTemplateContainersPage: function () {
      router.push({
        name: 'trashtemplateContainers',
        params: {id: this.data.id}
      })
    }
  },
  async beforeMount() {
    await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => {
        this.locatie = result.filter(loc => loc.id === this.data.location)[0].name
      }
    )
  }
}
</script>

<style scoped>
.text-style-url {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
