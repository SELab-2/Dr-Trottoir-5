<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p data-test="name"  @click="goToBuildingPage" class="text-style-building">{{ this.data.name }}</p>
      </v-col>
      <v-col cols="2">
        <p data-test="adres">{{ this.data.adres }}</p>
      </v-col>
      <v-col cols="1">
        <p :style="{
    color:
      this.data.efficiency < 50 ? '#FF1F00' :
      this.data.efficiency < 75 ? '#E88E4D' :
      '#39AE68'
  }">{{ this.data.efficiency }}%</p>
      </v-col>
      <v-col cols="2">
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
            >
              <v-icon color="#FFE600" icon="mdi-file"></v-icon>
              <v-icon color="#FFE600" right>mdi-menu-down</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item data-test="manual" value="download" @click="downloadDocument">
              <v-icon color="red" icon="mdi-file-pdf-box"></v-icon>
              Handleiding
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="3">
        <p :style="{ color: status === 'Update nodig' ? 'red' : status === 'Klaar' ? 'green' : '' }">{{
            this.status
          }}</p>
      </v-col>
      <v-col cols="2" class="d-flex align-center justify-end">
        <v-btn data-test="edit" icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditBuilding">
          <EditIcon/>
        </v-btn>
        <v-btn data-test="delete" icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import EditIcon from '@/components/icons/EditIcon.vue'
import Building from "@/api/models/Building";
import BuildingService from "@/api/services/BuildingService";
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";
import DeleteIcon from "@/components/icons/DeleteIcon.vue";

/**
 * BuildingCard component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * gebouw: String
 * adres: String
 * status: String
 * efficiency: Number
 */

export default {
  name: 'BuildingCard',
  components: {DeleteIcon, EditIcon},
  props: {
    data: {
      type: Building
    }
  },
  data: () => ({
    manual: '',
    status: '',
  }),
  methods: {
    downloadDocument: function () {
      window.open(this.manual)
    },
    goToEditBuilding: function () {
      router.push({name: 'admin_edit_building', params: {id: this.data.id}})
    },
    deletePost: async function () {
      await RequestHandler.handle(BuildingService.deleteBuildingById(this.data.id), {
        id: 'BuildingCardDeleteBuilding',
        style: 'SNACKBAR',
        customMessages: [
          {
            code: '500',
            message: 'Kon gebouw niet verwijderen.',
            description: 'Kon gebouw niet verwijderen.'
          }
        ]
      }).then(() => location.reload())
        .catch(() => location.reload())
    },
    goToBuildingPage: function () {
      router.push({name: 'admin_info_building', params: {id: this.data.id}});
    },
  },
  async beforeMount() {
    await RequestHandler.handle(BuildingService.getManualById(this.data.id), {
      id: 'BuildingCardGetManual',
      style: 'SNACKBAR'
    }).then(async result => {
      this.status = result.manualStatus
      this.manual = result.file.substring(result.file.indexOf('/api/'))
    })
  }
}
</script>

<style scoped>
.text-style-building {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
