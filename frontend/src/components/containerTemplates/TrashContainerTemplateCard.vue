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
        {{ this.data.year }}
      </v-col>
      <v-col cols="1">
        {{ this.data.week }}
      </v-col>
      <v-col cols="1">
        {{ this.locatie }}
      </v-col>
      <v-col cols="1">
        {{ this.data.even }}
      </v-col>
      <v-col class="text-right" cols="1">
        <v-btn class="button-style" icon v-on:click="editTemplate">
          <EditIcon/>
        </v-btn>
      </v-col>
      <v-col class="text-right" cols="1">
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
    }
  },
  data: () => ({
    locations: [],
    locatie: ""
  }),
  methods: {
    editTemplate: function () {
      router.push({
        path: '/trashtemplates/'+ this.data.id +'/edit'
      });
    },
    deleteTemplate: function () {
      //todo
    },
    goToTrashTemplateBuildingsPage: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/buildings'
      });
    },
    goToTrashTemplateContainersPage: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/containers'
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
