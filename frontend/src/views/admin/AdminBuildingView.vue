<template>
  <v-row>
    <v-btn icon="mdi-delete"></v-btn>
    <v-btn icon="mdi-pencil"></v-btn>
    <v-col lg="12">
      <h1>{{ name }}</h1>
    </v-col>
    <v-col lg="12">
      <h1>Adres</h1>
    </v-col>
    <v-col lg="12">
      <h1>{{ adres }}</h1>
    </v-col>
    <v-col lg="12">
      <h1>Klanten nummer</h1>
    </v-col>
    <v-col lg="12">
      <h1>
        {{ ivago_klantnr }}
      </h1>
    </v-col>
    <v-col lg="12">
      <h1>Vuilnis planning {{ name }}</h1>
    </v-col>
    <!-- Add list of planning cards -->
    <v-col lg="12">
      <normal-button text="Nieuwe ophaling" :parent-function="() => {}"></normal-button>
    </v-col>
  </v-row>
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
      name: 'Empty',
      adres: 'Empty',
      manual: null,
      ivago_klantnr: 0,
      planningen: []
    }
  },
  beforeMount() {
    RequestHandler.handle(BuildingService.getBuildingById(this.$route.params.id), {
      id: 'getBuildingError',
      style: 'SNACKBAR'
    }).then(result => {
      this.name = result.name
      this.adres = result.adres
      this.manual = result.manual
      this.ivago_klantnr = result.ivago_klantnr
    })
  }
}
</script>

