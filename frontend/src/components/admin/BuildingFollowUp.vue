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
          item-value="id"
          v-model="this.name"
          v-on:update:modelValue="(el) => this.buildingChange(el)"
        ></v-autocomplete>
        <h2>{{ this.name }}</h2>
      </v-col>
    </v-row>
    <v-row/>
    <br>
    <v-row justify="center">
      <v-col cols="4">
        <v-row justify="center" class="text-center">
          <v-col cols="12"><h1>Aankomst</h1></v-col>
          <br>
          <ul>
            <li v-for="(el) in this.arrivals" :key="el">
              <v-col cols="12">
                <FotoCardAdmin v-bind:data="el"/>
              </v-col>
            </li>
          </ul>
        </v-row>
      </v-col>

      <v-col cols="4">
        <v-row justify="center" class="text-center">
          <v-col cols="12"><h1>Berging</h1></v-col>
          <br>
          <ul>
            <li v-for="(el) in this.storages" :key="el">
              <v-col cols="12">
                <FotoCardAdmin v-bind:data="el"/>
              </v-col>
            </li>
          </ul>
        </v-row>
      </v-col>

      <v-col cols="4">
        <v-row justify="center" class="text-center">
          <v-col cols="12"><h1>Vertrek</h1></v-col>
          <br>
          <ul>
            <li v-for="(el) in this.departs" :key="el">
              <v-col cols="12">
                <FotoCardAdmin v-bind:data="el"/>
              </v-col>
            </li>
          </ul>
        </v-row>
      </v-col>


    </v-row>
  </v-col>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";
import router from "@/router";
import {DatePicker} from "v-calendar";
import PlanningService from "@/api/services/PlanningService";
import {getWeek} from "@/api/DateUtil";
import RoundBuildingCard from "@/components/admin/RoundBuildingCard.vue";
import FotoCardAdmin from "@/components/admin/FotoCardAdmin.vue";

export default {
  name: "BuildingFollowUp",
  components: {FotoCardAdmin, RoundBuildingCard, DatePicker},
  data: () => {
    return {
      id: 0,
      name: '',
      adres: '',
      location: {},
      manual: {file: '', fileType: '', manualStatus: ''},
      ivago_klantnr: 0,
      date: new Date().toISOString().split('T')[0],
      masks: { modelValue: 'YYYY-MM-DD' },
      buildings: [],
      arrivals: [],
      departs: [],
      storages: []
    }
  },

  beforeMount() {
    this.getBuildingInformation(this.$route.params.id).then(() => this.getStudentPosts())
    RequestHandler.handle(BuildingService.getBuildings(), {id: 'getBuildingsError', style: 'SNACKBAR'})
      .then(async result => this.buildings = result)
  },
  methods: {
    changed() {
      this.getStudentPosts()
    },
    async getBuildingInformation(buildingId) {
      await RequestHandler.handle(BuildingService.getBuildingById(buildingId), {
        id: 'getBuildingError',
        style: 'SNACKBAR'
      }).then(async result => {
        console.log(result)
        this.id = result.id
        this.name = result.name
        this.adres = result.adres
        this.location = result.location
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
      router.push({name: "admin_info_building", params: {id: building}})
      this.getBuildingInformation(building).then(() => this.getStudentPosts())
    },
    async getStudentPosts(){
      const date = new Date(this.date)
      let week = getWeek(date)
      if(date.getUTCDay() === 0){
        week -= 1
      }
      await RequestHandler.handle(PlanningService.getRounds(date.getFullYear(), week, date.getUTCDay(), this.location.id), {
        id: 'getRoundsError',
        style: 'NONE'
      }).then(async rounds => {
        for(const round of rounds){
          if(round.ronde.buildings.map(building => building.id).includes(this.id)){
            await RequestHandler.handle(PlanningService.getInfoOfBuilding(round.id, this.id), {
              id: 'getInfoOfBuildingError',
              style: 'NONE'
            }).then(async info => {
                await RequestHandler.handle(PlanningService.getPictures(info[0].id, date.getFullYear(), week), {
                  id: 'getPicturesError',
                  style: 'NONE'
                }).then(async pictures => {
                  console.log(pictures)
                  this.arrivals = []
                  this.departs = []
                  this.storages = []
                  for(const picture of pictures){
                    if(picture.pictureType === "AR"){
                      this.arrivals.push(picture)
                    } else if(picture.pictureType === "DE"){
                      this.departs.push(picture)
                    } else if(picture.pictureType === "ST"){
                      this.storages.push(picture)
                    }
                  }
                }).catch(() => {
                  this.arrivals = []
                  this.departs = []
                  this.storages = []
                })
              }).catch(() => {
                  this.arrivals = []
                  this.departs = []
                  this.storages = []
                })
          }
        }
      }).catch(() => {
        this.arrivals = []
        this.departs = []
        this.storages = []
      });
    }
  }
}
</script>

<style scoped>

.datepicker{
  width: 150px !important;
}

ul{
  list-style-type: None;
}

</style>
