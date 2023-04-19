<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p class="text-style-title">{{ this.data.name }}</p>
      </v-col>
      <v-col cols="1">
        <p @click="goToTrashTemplateContainersPage">Zie Vuilnisbakken</p>
      </v-col>
      <v-col cols="1">
        <p @click="goToTrashTemplateBuildingsPage">Zie Gebouwen</p>
      </v-col>
      <v-col cols="1">
        {{ this.data.year }}
      </v-col>
      <v-col cols="1">
        {{ this.data.week }}
      </v-col>
      <v-col cols="1">
        {{ this.locations.filter(loc => loc.id === this.data.location_id)[0].name }}
      </v-col>
      <v-col cols="1"/>
      <v-col class="text-right" cols="2">
        <v-btn class="button-style" icon v-on:click="editTemplate">
          <EditIcon/>
        </v-btn>
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

export default {
  name: 'TrashContainerTemplateCard',
  components: {EditIcon, DeleteIcon},
  props: {
    data: {
      type: TrashTemplate,
      default: () => (new TrashTemplate())
    }
  },
  data: () => ({
    locations: []
  }),
  methods: {
    editTemplate: function () {
      router.push({
        path: '/trashtemplates/edit', params: {
          toEdit: this.data // TODO deze pagina maken
        }
      });
    },
    deleteTemplate: function () {
      //todo
    },
    goToTrashTemplateBuildingsPage: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/buildings', params: {
          trashTemplate: this.data // TODO deze pagina maken
        }
      });
    },
    goToTrashTemplateContainersPage: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/containers', params: {
          trashTemplate: this.data // TODO deze pagina maken
        }
      })
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
  }
}
</script>

<style scoped>
.text-style-title {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
