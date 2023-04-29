<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col class="d-flex align-center" cols="2">
        <p class="text-style-building" @click="goToBuildingPage">{{ this.building.name }}</p>
      </v-col>
      <v-col class="d-flex align-center" cols="2">
        <p>{{ this.building.adres }}</p>
      </v-col>
      <v-col class="d-flex align-center" cols="1">
        <p :style="{
    color:
      this.building.efficiency < 50 ? '#FF1F00' :
      this.building.efficiency < 75 ? '#E88E4D' :
      '#39AE68'
  }">{{ this.building.efficiency }}%</p>
      </v-col>
      <v-col class="d-flex align-center" cols="1">
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
      <v-col class="d-flex align-center" cols="2">
        <v-menu>
          <template v-slot:activator="{ props }">
            <span :style="{ color: status === 'Update nodig' ? 'red' : status === 'Klaar' ? 'green' : '' }">{{
                status
              }}</span>
          </template>
        </v-menu>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Building from "@/api/models/Building";
import BuildingService from "@/api/services/BuildingService";
import { RequestHandler } from "@/api/RequestHandler";
import router from "@/router";


export default {
  name: 'TrashTemplateBuildingCard',
  components: {},
  props: {
    data: {
      /**
       * Object of type:
       * {
       *   building: Building,
       *   trash_ids: Number[]
       * }
       * **/
      type: Object //TODO MAKE OBJECT FOR THIS
    }
  },
  data: () => ({
    status: '',
    building: null
  }),
  methods: {
    downloadDocument: function () {
      // TODO
    },
    goToBuildingPage: function () {
      // TODO Check if correct id with data because now it's with this.building
      router.push({name: 'admin_info_building', params: {id: this.building.id}});
    }
  },
  mounted() {
    this.status = this.building.status
  },
  async beforeMount() {
    this.building = this.data.building
    await RequestHandler.handle(BuildingService.getManualById(this.data.id)).then(
      async result => this.status = result.manualStatus)
  }
}
</script>

<style scoped>
.text-style-building {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
