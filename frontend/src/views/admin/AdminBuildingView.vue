<template>
  <v-card v-if="!edit" color="white" class="mx-auto my-16 w-75">
    <v-row>
      <v-col md="12" lg="12" class="d-flex justify-lg-space-between pl-5 pr-5 pt-5">
        <v-btn @click="$refs.confirm.open()" icon="mdi-delete"></v-btn>
        <v-btn @click="edit = true" icon="mdi-pencil"></v-btn>
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
        <v-text-field readonly variant="solo" class="text_field_manaul"
                      :model-value="manual.manualStatus"></v-text-field>
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
  <v-card v-else color="white" class="mx-auto my-16 w-75">
    <v-row>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Naam</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start pt-5">
        <v-text-field class="text_field" v-model:model-value="name" variant="solo"></v-text-field>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Adres</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field class="text_field" v-model:model-value="adres" variant="solo"></v-text-field>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Klanten nummer</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field class="text_field" v-model:model-value="ivago_klantnr" variant="solo"></v-text-field>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Geschatte tijd in minuten</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field class="text_field" v-model:model-value="time" variant="solo"></v-text-field>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Handleiding status</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-select class="text_field"
                  variant="solo"
                  :items="['Klaar', 'Update nodig', 'Bezig', 'Geüpdatet']"
                  v-model="manual.manualStatus"
        ></v-select>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Nieuwe handleiding</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex justify-start align-center">
        <v-file-input v-model="new_manual" prepend-icon="mdi-file-upload-outline" class="text_field"
                      variant="solo"></v-file-input>
      </v-col>
      <v-col class="d-flex justify-center align-center pt-5 pb-10" cols="12" sm="12" md="12" lg="12">
        <normal-button text='Aanpassingen opslaan' :parent-function="save"/>
        <normal-button text='Annuleer' :parent-function="cancel_save" class="ml-2"/>
      </v-col>
    </v-row>
  </v-card>
  <ConfirmDialog ref="confirm" text="Bent u zeker dat u dit gebouw wilt verwijderen?" :confirm_function="deleteBuilding"></ConfirmDialog>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import BuildingService from "@/api/services/BuildingService";
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";
import ConfirmDialog from "@/components/util/ConfirmDialog"

export default {
  name: "AdminBuildingView",
  components: {ConfirmDialog, NormalButton},
  props: ['id'],
  data: () => {
    return {
      name: '',
      adres: '',
      manual: {file: '', fileType: '', manualStatus: ''},
      ivago_klantnr: 0,
      time: 0,
      planningen: [],
      dialog: false,
      edit: false,
      new_manual: null
    }
  },
  beforeMount() {
    this.getBuildingInformation()
  },
  methods: {
    getBuildingInformation() {
      RequestHandler.handle(BuildingService.getBuildingById(this.$route.params.id), {
        id: 'getBuildingError',
        style: 'SNACKBAR'
      }).then(async result => {
        this.name = result.name
        this.adres = result.adres
        this.ivago_klantnr = result.ivago_klantnr
        if (result.manual != null) {
          await RequestHandler.handle(BuildingService.getManualById(result.manual), {
            id: 'getManualByBuildingError',
            style: 'SNACKBAR'
          }).then(manual => {
            this.manual = manual
          })
        } else {
          this.$store.dispatch("snackbar/open", {
            message: "Het gebouw heeft geen handleiding.",
            color: "error"
          })
        }
      }).catch(() => {
        // TODO Go to list of buildings page
        //router.push({name: 'home'})
      })
    },
    getManual() {
      window.open(this.manual.file)
    },
    addPlanning() {
      // TODO Add planning for building
    },
    async deleteBuilding() {
      if (this.manual.file !== '') {
        await RequestHandler.handle(BuildingService.deleteManualById(this.manual.id), {
          id: 'deleteManualError',
          style: "SNACKBAR"
        })
      }
      RequestHandler.handle(BuildingService.deleteBuildingById(this.$route.params.id), {
        id: 'deleteBuildingError',
        style: "SNACKBAR"
      })
      // TODO Go to list of buildings page
      await router.push({name: 'home'})
    },
    async save() {
      this.edit = false
      let body_building = {
        name: this.name,
        adres: this.adres,
        ivago_klantnr: this.ivago_klantnr,
      }
      if (this.new_manual !== null) {
        await RequestHandler.handle(BuildingService.updateManualFileById(
          this.manual.id,
          this.new_manual[0], this.new_manual[0].type,
          this.manual.manualStatus), {
          id: 'updateManualFileError',
          style: 'SNACKBAR'
        })
      } else {
        await RequestHandler.handle(BuildingService.updateManualStatusById(this.manual.id, {
          manualStatus: this.manual.manualStatus
        }), {
          id: 'updateManualStatusError',
          style: 'SNACKBAR'
        })
      }
      await RequestHandler.handle(BuildingService.updateBuildingById(this.$route.params.id, body_building), {
        id: 'updateBuildingError',
        style: 'SNACKBAR'
      })
    },
    cancel_save() {
      this.edit = false
      this.getBuildingInformation()
    }
  }
}
</script>

<style>
.text_field_manaul {
  height: 40px;
  max-width: 150px;
  padding-left: 5px;
  padding-top: 5px;
}

.text_field {
  height: 40px;
  max-width: 350px;
  padding-left: 5px;
  padding-top: 5px;
}
</style>
