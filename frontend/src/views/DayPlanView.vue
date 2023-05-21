<template>
  <v-container align="center">
    <v-expansion-panels v-model="panel" style="max-width: 750px;" v-if="rondes.length > 0">
      <h4 class="text-h4 mb-3">{{ time }}</h4>
      <v-expansion-panel v-for="ronde in rondes" :key="ronde.id">
        <v-expansion-panel-title>
          Ronde {{ ronde.ronde.name }}
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          <v-card max-width="750px" class="py-3" elevation="0">
            <DayPlanBuilding v-for="building in ronde.ronde.buildings" :key="building.id"
                             :data="{building: building, planning: ronde.id, year: year, week: week}" :date="date" />
          </v-card>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-card max-width="750px" class="py-3" v-if="rondes.length === 0">
      <h4 class="text-h4 mb-3">{{ time }}</h4>
      <h5 class="text-h5 mb-3">Er is nog geen ronde ingepland.</h5>
      <normal-button text="Terug" v-bind:parent-function="goBack" class="mt-2" style="width: 90%;"
                           v-if="rondes.length === 0"></normal-button>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DayPlanBuilding from '@/components/student/DayPlanBuilding.vue';
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import NormalButton from "@/components/NormalButton.vue";
import router from '@/router';
import {getWeek} from "@/api/DateUtil";
import TrashTemplateService from "@/api/services/TrashTemplateService";

export default defineComponent({
  name: "DayPlanView",
  components: {
    DayPlanBuilding,
    NormalButton
  },
  async created() {
    if ('date' in this.$route.query) this.date = this.$route.query.date;
    this.time = this.capitalize(new Date(this.date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'}));
    const date = new Date(this.date);
    this.year = date.getFullYear();
    this.week = getWeek(date);
    if(date.getUTCDay() === 0){
      this.week -= 1
    }
    const day = this.daymap[date.getUTCDay()];

    RequestHandler.handle(PlanningService.get(this.year, this.week, date.getUTCDay()), {
      id: "getDayplanningError",
      style: "NONE"
    }).then(plannings => {
      RequestHandler.handle(TrashTemplateService.getContainers(this.year, this.week), {
        id: "getContainersError",
        style: "NONE"
      }).then(containers => {
        plannings.forEach(planning => {
          RequestHandler.handle(PlanningService.getStatus(this.year, this.week, planning.id), {
            id: `getStatus${planning.id}Error`,
            style: "NONE"
          }).then(statuses => {
            const buildings = Object(planning.ronde.buildings);
            for (let building of buildings)
              building.status = statuses[building.id].AR === 0 ? 'Niet begonnen' : statuses[building.id].DE > 0 ? 'Voltooid' : 'Bezig';
            planning.ronde.buildings = buildings.filter(building => {
              if (building.id.toString() in containers) {
                return containers[building.id.toString()].some(container => {
                  return container.collection_day.day === day;
                });
              }
              return false;
            });
            if (planning.ronde.buildings.length > 0) this.rondes.push(planning);
          }).catch(() => null);
        });
      }).catch(() => null);
    }).catch(() => null);
  },
  methods: {
    capitalize(s: string) {
      return s.split(' ').map(s => s[0].toUpperCase() + s.slice(1)).join(' ');
    },
    goBack() {
      router.go(-1);
    }
  },
  data: () => ({
    time: '',
    date: new Date().toISOString().split('T')[0],
    ronde: 'Er is nog geen ronde ingepland.',
    rondes: [],
    year: null,
    week: null,
    panel: [0],
    daymap: {
      1: 'MO',
      2: 'TU',
      3: 'WE',
      4: 'TH',
      5: 'FR',
      6: 'SA',
      0: 'SU'
    }
  })
});
</script>
