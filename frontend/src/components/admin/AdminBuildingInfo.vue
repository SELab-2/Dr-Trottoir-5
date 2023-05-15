<template>
  <v-card color="white" :class="`mx-auto my-10 py-5 w-75`">
    <v-row class="justify-space-between mx-auto">
      <v-col cols='12' sm='6' md='6'>
        <v-text-field v-model='name' :readonly="!edit" :error-messages="check_errors(this.errors, 'name')" label='Naam' required></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6">
        <v-text-field :readonly="!edit" :error-messages="check_errors(this.errors, 'adres')" v-model="adres" label="Adres"></v-text-field>
      </v-col>
    </v-row>
    <v-row class="justify-space-between mx-auto">
      <v-col cols='12' sm='6' md='6'>
        <v-select label="Locatie"
                  :readonly="!edit"
                  :error-messages="check_errors(this.errors, 'location')"
                  variant="solo"
                  :items="locations"
                  item-title="name"
                  item-value="id"
                  v-model="selectedLocation"
        ></v-select>
      </v-col>
      <v-col cols="12" sm="6" md="6">
        <v-text-field :readonly="!edit" label="Klanten nummer" :error-messages="check_errors(this.errors, 'ivago_klantnr')" v-model="ivago_klantnr"></v-text-field>
      </v-col>
    </v-row>
    <v-row class="justify-space-between mx-auto">
      <v-col cols="12" sm="3" md="3">
        <v-select variant="solo"
                  :readonly="!edit"
                  :items="['Klaar', 'Update nodig', 'Bezig', 'Geüpdatet']"
                  v-model="manual.manualStatus"
        ></v-select>
      </v-col>
      <v-col cols="12" sm="6" md="6">
        <v-file-input label="Handleiding" :readonly="!edit" v-model="manual" :error-messages="check_errors(this.errors, 'manual')" prepend-icon="mdi-file-upload-outline" ></v-file-input>
      </v-col>
    </v-row>
    <v-col v-if="edit" class="d-flex justify-center align-center py-5">
      <normal-button text='Aanpassingen opslaan' :parent-function="save"/>
      <normal-button text='Annuleer' :parent-function="cancel_save" class="ml-2"/>
    </v-col>
    <v-col v-if="!edit" class="d-flex justify-center align-center py-5">
      <normal-button text="Afvalcontainer toevoegen" :parent-function="addPlanning"></normal-button>
      <normal-button text="Aanpassen" :parent-function="goEditPage" class="ml-2"></normal-button>
    </v-col>
  </v-card>
  <ConfirmDialog ref="confirm" text="Bent u zeker dat u dit gebouw wilt verwijderen?"
                 :confirm_function="deleteBuilding"></ConfirmDialog>
</template>

<script>
import NormalButton from "@/components/NormalButton";
import BuildingService from "@/api/services/BuildingService";
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";
import ConfirmDialog from "@/components/util/ConfirmDialog"
import {check_errors, get_errors} from "@/error_handling";
import LocationService from "@/api/services/LocationService";

export default {
  name: "AdminBuildingView",
  components: {ConfirmDialog, NormalButton},
  props: {edit: Boolean},
  data: () => {
    return {
      name: '',
      adres: '',
      manual: {file: '', fileType: '', manualStatus: ''},
      ivago_klantnr: 0,
      // time: 0,  TODO <- milestone 3
      planningen: [],
      new_manual: null,
      selectedLocation: null,
      locations: [],
      errors: null
    }
  },
  beforeMount() {
    this.getBuildingInformation()
  },
  methods: {
    check_errors,
    goEditPage() {
      router.push({name: 'admin_edit_building', params: {id: this.$route.params.id}})
    },
    async getBuildingInformation() {

        // get all possible locations
      this.locations = await RequestHandler.handle(LocationService.getLocations(), {
        id: 'getLocationsError',
        style: 'SNACKBAR'
      }).then(result => result).catch(() => []);

      RequestHandler.handle(BuildingService.getBuildingById(this.$route.params.id), {
        id: 'getBuildingError',
        style: 'SNACKBAR'
      }).then(async result => {
        this.name = result.name
        this.adres = result.adres
        this.ivago_klantnr = result.ivago_klantnr
        this.selectedLocation = result.location

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
    addPlanning() {
      router.push({'name': 'trashtemplates'})
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
      await router.push({name: 'buildings'})
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
        }).then(manual => { this.manual = manual })
      } else {
        await RequestHandler.handle(BuildingService.updateManualStatusById(this.manual.id, {
          manualStatus: this.manual.manualStatus
        }), {
          id: 'updateManualStatusError',
          style: 'SNACKBAR'
        })
      }

      BuildingService.updateBuildingById(this.$route.params.id, body_building)
        .then(async () => {
          this.errors = null;
          await router.push({name: 'buildings'})
        })
        .catch(async (error) => this.errors = await get_errors(error));

    },
    async cancel_save() {
      await router.back()
    }
  }
}
</script>

<style>
</style>
