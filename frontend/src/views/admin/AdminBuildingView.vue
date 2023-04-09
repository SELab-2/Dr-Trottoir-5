<template>
  <v-card color="white" class="mx-auto my-16 w-75">
    <v-row>
      <v-col md="12" lg="12" class="d-flex justify-lg-space-between pl-5 pr-5 pt-5">
        <v-btn icon="mdi-delete"></v-btn>
        <v-btn icon="mdi-pencil"></v-btn>
      </v-col>
      <v-col lg="12" md="12" class="d-flex align-center justify-center">
        <h2>Gebouw: {{ name }}</h2>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center">
        <h2>Adres: {{ adres }}</h2>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center">
        <p>{{manual}}</p>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center">
        <h2>Klanten nummer: {{ ivago_klantnr }}</h2>
      </v-col>
      <v-col  md="12" lg="12" class="d-flex align-center justify-center">
        <h1>Vuilnis planning: {{ name }}</h1>
      </v-col>
      <!-- Add list of planning cards -->
      <v-col  md="12" lg="12" class="d-flex align-center justify-center pb-5">
        <normal-button text="Nieuwe ophaling" :parent-function="addPlanning"></normal-button>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import BuildingService from "@/api/services/BuildingService";
import {RequestHandler} from "@/api/RequestHandler";

export default {
  name: "AdminBuildingView",
  components: {NormalButton},
  data: () => {
    return {
      name: '',
      adres: '',
      manual: null,
      ivago_klantnr: 0,
      planningen: [],
    }
  },
  beforeMount() {
    RequestHandler.handle(BuildingService.getBuildingById(this.$route.params.id), {
      id: 'getBuildingError',
      style: 'SNACKBAR'
    }).then(async result => {
      this.name = result.name
      this.adres = result.adres
      this.ivago_klantnr = result.ivago_klantnr
      this.manual = await RequestHandler.handle(BuildingService.getManualById(result.manual), {
        id: 'getManualByBuildingError',
        style: 'SNACKBAR'
      })
    })
  },
  methods: {
    addPlanning() {
      // TODO planning toevoegen voor gebouw
    }
  }
}
</script>

