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
              color="primary"
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
                       v-bind:append-icon="this.statuses.AR > 0 ? 'mdi-check' : ''">
        </normal-button>
        <normal-button text="Berging" v-bind:parent-function="clickStorage" block class="mb-3"
                       v-bind:append-icon="this.statuses.ST ? 'mdi-check' : ''">
        </normal-button>
        <normal-button text="Vertrek" v-bind:parent-function="clickDeparture" block class="mb-3"
                       v-bind:append-icon="this.statuses.DE ? 'mdi-check' : ''">
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
import TrashTemplateService from "@/api/services/TrashTemplateService";

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

      RequestHandler.handle(PlanningService.getStatus(this.year, this.week, planning.id), {
        id: `getStatus${planning.id}Error`,
        style: "NONE"
      }).then(statuses => {
        this.statuses = statuses[this.$route.query.building];
      }).catch(() => null);

      const building_index = planning.ronde.buildings.findIndex(b => String(b.id) === this.$route.query.building);
      this.building = planning.ronde.buildings[building_index];
      RequestHandler.handle(PlanningService.getInfo(planning.id), {
        id: "getBuildingInfoError",
        style: "NONE"
      }).then(infos => { this.info = infos.find(i => i.building === this.building.id).id }).catch(() => null);

      const containers = await RequestHandler.handle(TrashTemplateService.getContainers(this.year, this.week), {
        id: "getContainersError",
        style: "NONE"
      }).then(containers => {
        if (this.building.id.toString() in containers) return containers[this.building.id.toString()];
        return [];
      }).catch(() => null);
      if (!containers) return;
      this.containers = containers.filter(c => c.collection_day.day === planning.time.day);
    }
  },
  data: () => ({
    building: {location: {name: ''}, adres: '', id: ''},
    trashMap: {PM: 'PMD', GL: 'GLAS', RE: 'REST', GF: 'GFT', PK: 'PK'},
    containers: [],
    statuses: {ST: 0, DE: 0, AR: 0},
    info: '',
    planning: '',
    year: null,
    week: null
  }),
  methods: {
    clickArrival() {
      router.push({name: 'student_post_view', query: {info: this.info, building: this.building.id, type: 'Aankomst', planning: this.planning, year: this.year, week: this.week}});
    },
    clickStorage() {
      router.push({name: 'student_post_view', query: {info: this.info, building: this.building.id, type: 'Berging', planning: this.planning, year: this.year, week: this.week}});
    },
    clickDeparture() {
      router.push({name: 'student_post_view', query: {info: this.info, building: this.building.id, type: 'Vertrek', planning: this.planning, year: this.year, week: this.week}});
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
