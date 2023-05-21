<template>
  <v-container align="center">
    <v-card v-if="building !== null">
      <v-card-title class="mt-2">
        <DatePicker v-model.string="date" color="white" :is-dark="true" :is-required="true" show-iso-weeknumbers
                    :first-day-of-week="1" :masks="masks" :attributes="attrs" view="weekly" v-on:dayclick="changed"
                    v-on:did-move="(e) => {setWeek(e); getContainers()}"
        />
        <h4 class="text-h4 my-2 text-wrap">
          Opmerkingen voor {{building.name}} op
          {{new Date(date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'})}}
        </h4>
      </v-card-title>
      <v-divider style="width: 90%;" class="mt-4"></v-divider>
      <v-card-text class="mt-3">
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
              <p class="text-subtitle-1" v-if="this.arrivals.length === 0">Geen berichten beschikbaar.</p>
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
              <p class="text-subtitle-1" v-if="this.storages.length === 0">Geen berichten beschikbaar.</p>
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
              <p class="text-subtitle-1" v-if="this.departs.length === 0">Geen berichten beschikbaar.</p>
            </v-row>
          </v-col>
        </v-row>
       </v-card-text>
    </v-card>

    <v-card v-else>
      <v-card-title class="text-center">
        <v-icon
          color="warning"
          icon="mdi-cancel"
          size="x-large"
        ></v-icon>
      </v-card-title>
      <v-spacer></v-spacer>
      <v-card-text>
        <v-row class="mx-auto justify-center">
          <div class="mx-1">Gebouw niet gevonden!</div>
        </v-row>
        <v-row class="my-4 justify-center">
          <div class="mx-1">Vraag uw syndicus om een nieuwe QR-Code door te geven.</div>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import RoundService from "@/api/services/RoundService";
import {DatePicker} from "v-calendar";
import FotoCardAdmin from "@/components/admin/FotoCardAdmin.vue";
import {getWeek} from "@/api/DateUtil";
import PlanningService from "@/api/services/PlanningService";
import TrashTemplateService from "@/api/services/TrashTemplateService";

export default {
  name: "BuildingView",
  components: {FotoCardAdmin, DatePicker},
  props: {id: String},
  data: () => ({
    building: null,
    masks: { modelValue: 'YYYY-MM-DD' },
    date: new Date().toISOString().split('T')[0],
    week: new Date(),
    arrivals: [],
    departs: [],
    storages: [],
    attrs: [],
    mapping: {
      GL: {type: 'GLAS', color: 'yellow'},
      GF: {type: 'GFT', color: 'green'},
      PM: {type: 'PMD', color: 'orange'},
      PK: {type: 'PK', color: 'blue'},
      RE: {type: 'REST', color: 'gray'}
    },
    day_map: {
      MO: 1,
      TU: 2,
      WE: 3,
      TH: 4,
      FR: 5,
      SA: 6,
      SU: 0,
    }
  }),
  beforeMount() {
    RequestHandler.handle(RoundService.getBuildingByUUID(this.id), {
      id: 'getBuildingByUUIDError',
      style: 'NONE'
    }).then(building => {
      this.building = building;
      this.changed();
      this.getContainers();
    }).catch(() => null)
  },
  methods: {
    changed() {
      this.getStudentPosts();
    },
    setWeek(e) {
      this.week = new Date(e[0].viewDays[1].id);
    },
    getContainers() {
      let week = getWeek(this.week);
      if (this.week.getUTCDay() === 0) week -= 1;
      RequestHandler.handle(TrashTemplateService.getContainers(this.week.getFullYear(), week), {
        id: "getContainersError",
        style: "NONE"
      }).then(containers => {
        if (this.building !== null && this.building.id.toString() in containers) {
          const cs = containers[this.building.id.toString()];
          this.attrs = cs.map(container => {
            const container_date = new Date(this.week);
            const dist = this.day_map[container.collection_day.day] - container_date.getDay();
            container_date.setDate(container_date.getDate() + dist);
            return {
              dates: container_date,
              popover: {
                label: this.mapping[container.type].type
              },
              dot: this.mapping[container.type].color
          }});
        }
      }).catch(() => null);
    },
    async getStudentPosts(){
      const date = new Date(this.date)
      let week = getWeek(date)
      if (date.getUTCDay() === 0) week -= 1;
      await RequestHandler.handle(PlanningService.getRounds(date.getFullYear(), week, date.getUTCDay(), this.building.location.id), {
        id: 'getRoundsError',
        style: 'NONE'
      }).then(async rounds => {
        for(const round of rounds){
          if(round.ronde.buildings.map(building => building.id).includes(this.building.id)){
            await RequestHandler.handle(PlanningService.getInfoOfBuilding(round.id, this.building.id), {
              id: 'getInfoOfBuildingError',
              style: 'NONE'
            }).then(async info => {
              await RequestHandler.handle(PlanningService.getPictures(info[0].id, date.getFullYear(), week), {
                id: 'getPicturesError',
                style: 'NONE'
              }).then(async pictures => {
                this.arrivals = []
                this.departs = []
                this.storages = []
                for(const picture of pictures){
                  picture.admin = false;
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
