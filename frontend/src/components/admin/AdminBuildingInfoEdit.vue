<template>
  <v-card color="white" class="mx-auto my-16 w-75">
    <v-row>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Naam</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start pt-5">
        <v-text-field data-test="name" class="text_field" v-model:model-value="name" variant="solo"></v-text-field>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Adres</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field data-test="adres" class="text_field" v-model:model-value="adres" variant="solo"></v-text-field>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
        <h2>Klanten nummer</h2>
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field data-test="client-nr" class="text_field" v-model:model-value="ivago_klantnr" variant="solo"></v-text-field>
      </v-col>
      <!---
        TODO For milestone 3
          <h2>Geschatte tijd in minuten</h2>
      <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
      </v-col>
      <v-col md="6" lg="6" class="d-flex align-center justify-start">
        <v-text-field class="text_field" v-model:model-value="time" variant="solo"></v-text-field>
      </v-col>
      --->
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
        <v-file-input data-test="manual" v-model="new_manual" prepend-icon="mdi-file-upload-outline" class="text_field"
                      variant="solo"></v-file-input>
      </v-col>
      <v-col class="d-flex justify-center align-center pt-5 pb-10" cols="12" sm="12" md="12" lg="12">
        <normal-button data-test="save-button" text='Aanpassingen opslaan' :parent-function="save"/>
        <normal-button data-test="cancel-button" text='Annuleer' :parent-function="cancel_save" class="ml-2"/>
      </v-col>
    </v-row>
  </v-card>
  <ConfirmDialog data-test="dialog" ref="confirm" text="Bent u zeker dat u dit gebouw wilt verwijderen?"
                 :confirm_function="deleteBuilding"></ConfirmDialog>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import BuildingService from "@/api/services/BuildingService";
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";
import ConfirmDialog from "@/components/util/ConfirmDialog"

export default {
  name: "AdminBuildingInfoEdit",
  components: {ConfirmDialog, NormalButton},
  data: () => {
    return {
      name: '',
      adres: '',
      manual: {file: '', fileType: '', manualStatus: ''},
      ivago_klantnr: 0,
      // time: 0,  TODO <- milestone 3
      planningen: [],
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
          this.manual = result.manual;
          this.manual.file = this.manual.file.substring(this.manual.file.indexOf('/api/'))
        } else {
          this.$store.dispatch("snackbar/open", {
            message: "Het gebouw heeft geen handleiding.",
            color: "error"
          })
        }
      }).catch(async () => {
        await router.push({name: 'buildings'})
      })
    },
    getManual() {
      window.open(this.manual.file)
    },
    async save() {
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
        }).then(manual => {
          this.manual = manual
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
      await router.push({name: 'admin_info_building', params: {id: this.$route.params.id}})
    },
    async cancel_save() {
      await router.push({name: 'admin_info_building', params: {id: this.$route.params.id}})
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
