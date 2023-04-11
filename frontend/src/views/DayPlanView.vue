<template>
  <v-container align="center">
    <h1>{{ time }}</h1>
    <h2>{{ ronde }}</h2>
    <normal-button text="Terug" v-bind:parent-function="goBack" block class="mt-2" v-if="buildings.length === 0"></normal-button>
    <DayPlanBuilding v-for="building in buildings" :data="building" :date="date" />
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
    const user = this.$store.getters['session/currentUser'];
    const id = await user.then(user => user.id).catch(() => null);
    if (!id) return;

    RequestHandler.handle(PlanningService.get(id, this.date), {
      id: "getDayplanningError",
      style: "NONE"
    }).then(planning => {
      const buildings = Object(planning.ronde.buildings);
      const statusMap = {NS: 'Niet begonnen', ST: 'Bezig', FI: 'Voltooid'};
      for (let index in planning.status) buildings[index].status = statusMap[planning.status[index]];

      this.buildings = buildings;
      this.ronde = planning.ronde.name;
    }).catch(() => {});
  },
  methods: {
    capitalize(s: string) {
      return s.split(' ').map(s => s[0].toUpperCase() + s.slice(1)).join(' ');
    },
    goBack() {
      router.go(-1);
    },
  },
  data: () => ({
    time: '',
    date: new Date().toISOString().split('T')[0],
    ronde: 'Er is nog geen ronde ingepland.',
    buildings: []
  })
});
</script>
