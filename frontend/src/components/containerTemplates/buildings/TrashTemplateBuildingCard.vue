<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2" class="d-flex align-center">
        <p @click="goToBuildingPage" class="text-style-building">{{ this.data.name }}</p>
      </v-col>
      <v-col cols="2" class="d-flex align-center">
        <p>{{ this.data.adres }}</p>
      </v-col>
      <v-col cols="1" class="d-flex align-center">
        <p :style="{
    color:
      this.data.efficiency < 50 ? '#FF1F00' :
      this.data.efficiency < 75 ? '#E88E4D' :
      '#39AE68'
  }">{{ this.data.efficiency }}%</p>
      </v-col>
      <v-col cols="1" class="d-flex align-center">
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
            <v-list-item value="download" @click="downloadDocument">
              <v-icon color="red" icon="mdi-file-pdf-box"></v-icon>
              PDF
            </v-list-item>
            <v-list-item value="upload" @click="uploadDocument">
              <v-icon color="#FFE600" icon="mdi-file-upload-outline"></v-icon>
              Upload
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2" class="d-flex align-center">
        <v-menu>
          <template v-slot:activator="{ props }">
            <span :style="{ color: status === 'Update nodig' ? 'red' : status === 'Klaar' ? 'green' : '' }">{{
                status
              }}</span>
          </template>
        </v-menu>
      </v-col>
      <v-col cols="3" class="d-flex align-center justify-end">
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
          <EditIcon/>
        </v-btn>
        <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
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
  name: 'TrashTemplateBuildingCard',
  components: {DeleteIcon, EditIcon },
  props: {
    data: {
      type: Building
    }
  },
  data: () => ({
    status: '',
    documentStatus: ['Klaar'] // TODO + updaten in database
  }),
  methods: {
    editPost: function () {
      // TODO
    },
    deletePost: function () {
      RequestHandler.handle(BuildingService.deleteBuildingById(this.data.id))
        .then(async result => router.go(0))
    },
    uploadDocument: function () {
      // TODO
    },
    downloadDocument: function () {
      // TODO
    },
    updateStatus: function (newStatus) {
      this.status = newStatus
      // TODO opslaan in database
    },
    goToBuildingPage: function () {
      router.push({ path: '/building/' + this.data.id});
    }
  },
  async mounted () {
    this.status = this.data.status
  },
  async beforeMount () {
    await RequestHandler.handle(BuildingService.getManualById(this.data.id)).then(async result => this.status = result.manualStatus)
  }
}
</script>

<style scoped>
.text-style-building {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
