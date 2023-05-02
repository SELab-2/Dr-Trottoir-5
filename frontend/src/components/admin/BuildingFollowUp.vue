<template>
  <v-col>
    <v-row justify="center">
      <v-col cols="6">
        <v-card flat>
          <DatePicker v-model.string="date" color="yellow" :is-dark="true" :is-required="true" show-iso-weeknumbers
                      :first-day-of-week="1" v-on:dayclick="changed" :masks="masks" class="datepicker"/>
        </v-card>
      </v-col>
      <v-col cols="4" align-self="center">
        <v-autocomplete
          clearable
          outlined
          rounded
          :menu-props:="{rounded: 'xl'}"
          :items="this.buildings"
          item-title="name"
          item-value="content"
          v-model="this.description"
          v-on:slotchange="this.changeBuilding"
        ></v-autocomplete>
        <h2>{{ this.name }}</h2>
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";
import router from "@/router";
import {DatePicker} from "v-calendar";

export default {
  name: "BuildingFollowUp",
  components: {DatePicker},
  data: () => {
    return {
      name: '',
      adres: '',
      manual: {file: '', fileType: '', manualStatus: ''},
      ivago_klantnr: 0,
      planningen: [],
      date: new Date().toISOString().split('T')[0],
      masks: { modelValue: 'YYYY-MM-DD' },
      buildings: []
    }
  },

  beforeMount() {
    this.getBuildingInformation()
    RequestHandler.handle(BuildingService.getBuildings(), {id: 'getBuildingsError', style: 'SNACKBAR'})
      .then(async result => this.buildings = result)
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
    buildingChange(building) {
      router.push({name: "admin_info_building", params: {id: building.id}})
    }
  }
}
</script>

<style scoped>

.datepicker{
  width: 150px !important;
}

</style>
