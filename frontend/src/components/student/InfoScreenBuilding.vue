<template>
  <v-container align="center">
    <v-card max-width="750px">
      <div align="center">
        <h1 data-test="buildingName">{{ building.name }}</h1>
        <v-container>
          <v-img style="max-height: 30vh;" src=""></v-img>
        </v-container>
      </div>
      <v-container >
        <v-btn data-test="download-button" rounded="xl" @click="downloadFile">
          <v-icon color="#FFE600" dark>mdi-file</v-icon>
          <p style="color: #FFE600">Handleiding</p>
        </v-btn>
      </v-container>
      <v-card class="container-border ma-2">
        <h2 class="mt-2">Opmerkingen:</h2>
        <v-list>
          <v-list-item v-for="remark in building.remarks">{{ remark }}</v-list-item>
        </v-list>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import RoundService from "@/api/services/RoundService";

/**
 * InfoScreenBuilding component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * nameBuilding: String naam van het gebouw
 * imageURL: String foto van het gebouw
 * remarks: Array de opmerkingen van het gebouw (code poort, locatie, etc.)
 */

export default {
  name: 'InfoScreenBuilding',
  props: {
    data: {
      type: Object,
      default: () => ({
        nameBuilding: "Empty",
        imageURL: 'empty',
        remarks: []
      })
    }
  },
  data: () => ({
    building: {location: {name: 'Empty'}, manual: {file: ''}, remarks: []},
  }),
  async created() {
    if ('building' in this.$route.query) {
      const building = await RequestHandler.handle(RoundService.getBuilding(this.$route.query.building), {
        id: "getBuildingError",
        style: "NONE"
      }).then(b => b).catch(() => null);
      if (!building) return;

      this.building = building;
    }
  },
  methods: {
    downloadFile() {
      window.open(this.building.manual.file);
    }
  }
}
</script>
