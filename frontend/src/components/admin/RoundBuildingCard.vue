<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p @click="goToBuildingPage" class="text-style-building">{{ this.data.name }}</p>
      </v-col>
      <v-col cols="3">
        <p>{{ this.data.adres }}</p>
      </v-col>
      <v-col cols="1">
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
              PFD
            </v-list-item>
            <v-list-item value="upload" @click="uploadDocument">
              <v-icon color="#FFE600" icon="mdi-file-upload-outline"></v-icon>
              Upload
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2">
        <v-menu>
          <template v-slot:activator="{ props }">
            <span :style="{ color: status === 'Update nodig' ? 'red' : status === 'Klaar' ? 'green' : '' }">{{
                status
              }}</span>
          </template>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2" class="text-right">
        <v-btn icon class="button-style" v-on:click="deletePost">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import {RequestHandler} from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";
import Building from "@/api/models/Building";
import router from "@/router";
/**
 * RoundBuildingCard component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * gebouw: String
 * adres: String
 * status: String
 */

export default {
  name: 'RoundBuildingCard',
  components: { DeleteIcon },
  props: {
    data: {
      type: Building
    }
  },
  data: () => ({
    status: ''
  }),
  methods: {
    deletePost: function () {
      // TODO
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
      router.push({ path: 'building/' + this.data.id })
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
.text-style-building{
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
