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
              PDF
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="3">
            <p :style="{ color: status === 'Update nodig' ? 'red' : status === 'Klaar' ? 'green' : '' }">{{
                this.status
              }}</p>
      </v-col>
      <v-col cols="2"/>
    </v-row>
  </v-container>
</template>

<script>
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
  props: {
    data: {
      type: Building
    }
  },
  data: () => ({
    status: ''
  }),
  methods: {
    downloadDocument: function () {
      window.open(this.data.manual.file)
    },
    goToBuildingPage: function () {
      router.push({name: 'admin_info_building', params : {id: this.data.id}})
    }
  },
  async mounted () {
    this.status = this.data.manual.manualStatus
    console.log(this.status)
  },
  async beforeMount () {
    await RequestHandler.handle(BuildingService.getManualById(this.data.id)).then(async result => { this.status = result.manualStatus })
    this.status = this.data.manual.manualStatus
    console.log(this.status)
  }
}
</script>

<style scoped>
.text-style-building{
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
