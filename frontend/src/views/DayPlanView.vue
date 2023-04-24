<template>
  <v-container align="center">
    <v-card max-width="750px" class="py-3">
      <h1>{{ time }}</h1>
      <h2>{{ ronde }}</h2>
      <normal-button text="Terug" v-bind:parent-function="goBack" block class="mt-2" v-if="buildings.length === 0"></normal-button>
      <DayPlanBuilding v-for="building in buildings" :data="{building: building, planning: planning, year: year, week: week}" :date="date" />
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
    this.week = this.getWeek(date);

    RequestHandler.handle(PlanningService.get(this.year, this.week, date.getUTCDay()), {
      id: "getDayplanningError",
      style: "NONE"
    }).then(planning => {
      const buildings = Object(planning.ronde.buildings);
      const statusMap = {NS: 'Niet begonnen', ST: 'Bezig', FI: 'Voltooid'};
      for (let index in planning.status) buildings[index].status = statusMap[planning.status[index]];

      this.buildings = buildings;
      this.ronde = planning.ronde.name;
      this.planning = planning.id;
    }).catch(() => {});
  },
  methods: {
    capitalize(s: string) {
      return s.split(' ').map(s => s[0].toUpperCase() + s.slice(1)).join(' ');
    },
    goBack() {
      router.go(-1);
    },
    getWeek(d) {
      const date = new Date(d);
      date.setHours(0, 0, 0, 0);
      // Thursday in current week decides the year.
      date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
      // January 4 is always in week 1.
      const week1 = new Date(date.getFullYear(), 0, 4);
      // Adjust to Thursday in week 1 and count number of weeks from date to week1.
      return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000 - 3 + (week1.getDay() + 6) % 7) / 7);
    }
  },
  data: () => ({
    time: '',
    date: new Date().toISOString().split('T')[0],
    ronde: 'Er is nog geen ronde ingepland.',
    buildings: [],
    planning: null,
    year: null,
    week: null
  })
});
</script>
