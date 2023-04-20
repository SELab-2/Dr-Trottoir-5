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


export default {
  name: 'TrashTemplateBuildingCard',
  components: {},
  props: {
    data: {
      type: Building
    }
  },
  data: () => ({
    status: '',
  }),
  methods: {
    downloadDocument: function () {
      // TODO
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
