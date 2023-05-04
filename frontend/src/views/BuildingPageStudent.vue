<template>
  <v-container align="center">
    <v-card max-width="750px">
      <v-card-title class="mt-2">
        <h1 class="text-wrap">{{building.name}}</h1>
        <v-row align="center" class="my-4">
          <v-btn prepend-icon="mdi-map-marker" class="mx-auto my-2" color="secondary"
                 :href="'https://www.google.com/maps/search/?api=1&query='+ encodeURIComponent(building.adres)" target="_blank">
            {{building.adres}}
          </v-btn>
          <v-btn class="mx-auto" color="secondary" :onclick="buildingInfo">
            Info
          </v-btn>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-card
          class="mx-auto"
          max-width="300"
        >
          <v-list density="compact">
            <v-list-subheader>Containers</v-list-subheader>

            <v-list-item
              v-for="(item, i) in containers"
              :key="i"
              :title="trashMap[item.type]"
              :subtitle="item.special_actions"
              align="left"
              active-color="primary"
            >
              <template v-slot:prepend>
                <v-icon icon="mdi-trash-can" color="green"></v-icon>
              </template>
            </v-list-item>
          </v-list>
        </v-card>
      </v-card-text>
      <v-card-text>
        <normal-button text="Aankomst" v-bind:parent-function="clickArrival" block class="mb-3"
                       v-bind:append-icon="this.pictures.includes('AR') ? 'mdi-check' : ''">
        </normal-button>
        <normal-button text="Berging" v-bind:parent-function="clickStorage" block class="mb-3"
                       v-bind:append-icon="this.pictures.includes('ST') ? 'mdi-check' : ''">
        </normal-button>
        <normal-button text="Vertrek" v-bind:parent-function="clickDeparture" block class="mb-3"
                       v-bind:append-icon="this.pictures.includes('DE') ? 'mdi-check' : ''">
        </normal-button>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import NormalButton from "@/components/NormalButton";
import ContainerService from "@/api/services/ContainerService";
import router from "@/router";

export default defineComponent({
  name: "BuildingPageStudent",
  components: {
    NormalButton
  },
  async created() {
    if ('planning' in this.$route.query) this.planning = this.$route.query.planning;
    if ('year' in this.$route.query) this.year = this.$route.query.year;
    if ('week' in this.$route.query) this.week = this.$route.query.week;
    if ('building' in this.$route.query) {
      const planning = await RequestHandler.handle(PlanningService.getPlanning(this.planning), {
        id: "getDayplanningError",
        style: "NONE"
      }).then(planning => planning).catch(() => null);
      if (!planning) return;

      const building_index = planning.ronde.buildings.findIndex(b => String(b.id) === this.$route.query.building);
      this.building = planning.ronde.buildings[building_index];
      const infos = await RequestHandler.handle(PlanningService.getInfo(planning.id), {
        id: "getBuildingInfoError",
        style: "NONE"
      }).then(info => info).catch(() => null);
      if (!infos) return;
      this.info = infos[building_index].id;

      RequestHandler.handle(PlanningService.getPictures(this.info), {
        id: "getPicturesError",
        style: "NONE"
      }).then(picture => this.pictures = picture.map(p => p.pictureType)).catch(() => null);

      const containers = await RequestHandler.handle(ContainerService.get(this.building.id, this.year, this.week), {
        id: "getContainersError",
        style: "NONE"
      }).then(c => c).catch(() => null);
      if (!containers) return;

      const weekDays = ['SU','MO','TU','WE','TH','FR','SA'];
      const day = weekDays[new Date(this.date).getDay()];
      this.containers = containers.filter(c => c.collection_day.day === day);
    }
  },
  data: () => ({
    date: new Date().toISOString().split('T')[0],
    building: {location: {name: ''}, adres: '', id: ''},
    trashMap: {PM: 'PMD', GL: 'GLAS', RE: 'REST', GF: 'GFT', PK: 'PK'},
    containers: [],
    pictures: [],
    info: '',
    planning: '',
    year: null,
    week: null
  }),
  methods: {
    clickArrival() {
      router.push({name: 'student_post_view', query: {info: this.info, building: this.building.id, type: 'Aankomst', planning: this.planning}});
    },
    clickStorage() {
      router.push({name: 'student_post_view', query: {info: this.info, building: this.building.id, type: 'Berging', planning: this.planning}});
    },
    clickDeparture() {
      router.push({name: 'student_post_view', query: {info: this.info, building: this.building.id, type: 'Vertrek', planning: this.planning}});
    },
    buildingInfo() {
      router.push({name: 'building_info', query: {building: this.building.id}});
    }
  }
});
</script>

<style>
  .v-btn__append .v-icon {
    color: limegreen;
  }
</style>
