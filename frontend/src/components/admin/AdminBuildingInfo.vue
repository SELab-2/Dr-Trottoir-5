<template>
  <v-col>
    <v-row justify="end" class="button-row">
      <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goEditPage">
          <EditIcon/>
        </v-btn>
        <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deleteBuilding">
          <DeleteIcon/>
        </v-btn>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card flat class="datecard">
          <DatePicker v-model.string="date" color="yellow" :is-dark="true" :is-required="true" show-iso-weeknumbers
                      :first-day-of-week="1" v-on:dayclick="changed" :masks="masks" class="datepicker"/>
        </v-card>
      </v-col>
      <v-col cols="3">
        <v-row>
          <v-col lg="12" md="12" class="d-flex align-center justify-center">
            <h2>Gebouw: {{ name }}</h2>
          </v-col>
          <v-col lg="12" md="12" class="d-flex align-center justify-center">
            <button @click="() => {this.search = !this.search}" class="text-decoration-underline">Change building</button>
          </v-col>
          <v-col lg="12" md="12" class="d-flex align-center justify-center" v-if="this.search">
            <v-autocomplete
              outlined
              rounded
              :menu-props:="{rounded: 'xl'}"
              :items="this.buildings"
              item-title="name"
              item-value="id"
              v-model="this.name"
              v-on:update:modelValue="(el) => this.buildingChange(el)"
            ></v-autocomplete>
          </v-col>
          <v-col md="12" lg="12" class="d-flex align-center justify-center">
            <h2>Adres: {{ adres }}</h2>
          </v-col>
          <v-col md="6" lg="6" class="d-flex align-center justify-end pt-10">
            <normal-button text="Handleiding" :parent-function="getManual"></normal-button>
          </v-col>
          <v-col md="6" lg="6" class="d-flex align-center justify-start">
            <v-text-field readonly variant="solo" class="text_field_manual"
                          :model-value="manual.manualStatus"></v-text-field>
          </v-col>
          <v-col md="12" lg="12" class="d-flex align-center justify-center">
            <h2>Klanten nummer: {{ ivago_klantnr }}</h2>
          </v-col>
          <v-col md="12" lg="12" class="d-flex align-center justify-center">
            <h2>Vuilnis planning:</h2>
          </v-col>
          <!-- TODO Add list of planning cards -->
          <v-col md="12" lg="12" class="d-flex align-center justify-center pb-10">
            <normal-button text="Nieuwe ophaling" :parent-function="addPlanning"></normal-button>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="6">
        <v-row justify="center" class="text-center">
          <ul>
            <li v-for="(el) in this.garbageCollections" :key="el">
              <v-col cols="12">
                <TrashPickupCard v-bind:data="el"/>
              </v-col>
            </li>
          </ul>
        </v-row>
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
                <FotoCardAdmin v-bind:data="el" :syndici="0" building="1"/>
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
import FotoCardAdmin from "@/components/admin/FotoCardAdmin.vue";
import NormalButton from "@/components/NormalButton.vue";
import DeleteIcon from "@/components/icons/DeleteIcon.vue";
import EditIcon from "@/components/icons/EditIcon.vue";
import TrashPickupCard from "@/components/admin/TrashPickupCard.vue";


export default {
  name: "AdminBuildingInfo",
  components: {TrashPickupCard, EditIcon, DeleteIcon, NormalButton, FotoCardAdmin, DatePicker},
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
      storages: [],
      garbageCollections: [],
      search: false,
      // time: 0,  TODO <- milestone 3
      planningen: [],
      new_manual: null,
      selectedLocation: null,
      locations: [],
      errors: null,
      // syndici: 0
    }
  },

  async beforeMount() {
    await this.getBuildingInformation(this.$route.params.id).then(() => this.getStudentPosts())
    await this.getTrashPickUps()
    await RequestHandler.handle(BuildingService.getBuildings(), {id: 'getBuildingsError', style: 'SNACKBAR'})
      .then(async result => {
        this.buildings = result
      })
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
        this.selectedLocation = result.location
        // this.syndici = result.syndicus.length()

        if (result.manual != null) {
          this.manual = result.manual;
          this.manual.file = this.manual.file.substring(this.manual.file.indexOf('/api/'))
        } else {
          this.$store.dispatch("snackbar/open", {
            message: "Het gebouw heeft geen handleiding.",
            color: "error"
          })
        }
        console.log(this.id)
      }).catch(async () => {
        await router.push({name: 'buildings'})
      })
    },
    getManual() {
      window.open(this.manual.file)
    },
    buildingChange(building) {
      this.search = false
      router.push({name: "admin_info_building", params: {id: building}})
      this.getBuildingInformation(building).then(() => this.getStudentPosts())
    },
    goEditPage() {
      router.push({name: 'admin_edit_building', params: {id: this.$route.params.id}})
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
    async getTrashPickUps(){
      // TODO: get all trash pick ups from one building at a certain time
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

.datecard{
  margin-left: 100px;
}

.text_field_manual {
  height: 40px;
  max-width: 150px;
  padding-left: 5px;
  padding-top: 5px;
}

ul{
  list-style-type: None;
}

.button-row{
  margin-right: 50px;
  margin-top: 50px;
}

</style>
