<template>
  <v-card color="white" class="mx-auto my-16 w-75">
    <v-row>
      <v-col md="12" lg="12" class="d-flex justify-lg-space-between pl-5 pr-5 pt-5">
        <v-btn @click="dialog = true" icon="mdi-delete"></v-btn>
        <v-btn icon="mdi-pencil"></v-btn>
      </v-col>
      <v-col lg="12" md="12" class="d-flex align-center justify-center">
        <h2>Gebouw: {{ name }}</h2>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center">
        <h2>Adres: {{ adres }}</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <normal-button text="Handleiding" :parent-function="getManual"></normal-button>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field readonly variant="solo" class="text_field" :model-value="manaul_status"></v-text-field>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center">
        <h2>Klanten nummer: {{ ivago_klantnr }}</h2>
      </v-col>
      <v-col md="12" lg="12" class="d-flex align-center justify-center">
        <h2>Vuilnis planning:</h2>
      </v-col>
      <!-- Add list of planning cards -->
      <v-col md="12" lg="12" class="d-flex align-center justify-center pb-10">
        <normal-button text="Nieuwe ophaling" :parent-function="addPlanning"></normal-button>
      </v-col>
    </v-row>
  </v-card>
  <v-dialog v-model="dialog" content-class="d-flex align-center justify-end">
    <v-card class="overflow-hidden h-50 w-50">
      <v-row>
        <v-col md="12" lg="12" class="d-flex align-center justify-center pt-10">
          <p>
            Bent u zeker dat u dit gebouw wilt verwijderen?
          </p>
        </v-col>
        <v-col md="6" lg="6" class="d-flex align-center justify-end pb-10">
          <normal-button text="Ja" @click="deleteBuilding"></normal-button>
        </v-col>
        <v-col md="6" lg="6" class="d-flex align-center justify-start pb-10">
          <normal-button text="Nee" @click="dialog = false"></normal-button>
        </v-col>
      </v-row>
    </v-card>
  </v-dialog>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import BuildingService from "@/api/services/BuildingService";
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";

export default {
  name: "AdminBuildingView",
  components: {NormalButton},
  props: ['id'],
  data: () => {
    return {
      name: '',
      adres: '',
      manual: null,
      manaul_status: '',
      ivago_klantnr: 0,
      planningen: [],
      dialog: false
    }
  },
  beforeCreate() {
    RequestHandler.handle(BuildingService.getBuildingById(this.$route.params.id), {
      id: 'getBuildingError',
      style: 'SNACKBAR'
    }).then(async result => {
      this.name = result.name
      this.adres = result.adres
      this.ivago_klantnr = result.ivago_klantnr
      await RequestHandler.handle(BuildingService.getManualById(result.manual), {
        id: 'getManualByBuildingError',
        style: 'SNACKBAR'
      }).then(manual => {
        this.manual = manual.file
        this.manaul_status = manual.manualStatus
      })
    }).catch(() => {
      // TODO Go to list of buildings page
      router.push({name: "home"})
    })
  },
  methods: {
    // TODO Add cookies
    getManual() {
      window.open(this.manual)
    },
    addPlanning() {
      // TODO Add planning for building
    },
    deleteBuilding() {
      RequestHandler.handle(BuildingService.deleteManualById(this.manual.id), {
        id: 'deleteManualError',
        style: "SNACKBAR"
      }).then(() => {
        RequestHandler.handle(BuildingService.deleteBuildingById(this.$route.params.id), {
          id: 'deleteBuildingError',
          style: "SNACKBAR"
        })
      })
      // TODO Go to list of buildings page
      router.push({name: 'home'})
    }
  }
}
</script>

<style>
.text_field {
  height: 40px;
  max-width: 150px;
  padding-left: 5px;
  padding-top: 5px;
}
</style>
