<template>
  <v-container align="center">
    <h1>{{ time }}</h1>
    <h2>{{ ronde }}</h2>
    <DayPlanBuilding v-for="building in buildings" :data="building" />
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DayPlanBuilding from '@/components/student/DayPlanBuilding.vue';
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";

export default defineComponent({
  name: "DayPlanView",
  components: {
    DayPlanBuilding
  },
  created() {
    this.time = this.capitalize(new Date().toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'}));
    const student = this.$store.getters['session/currentUser'];
    if (!student) return;
    const id = student.id;
    const date = new Date().toISOString().split('T')[0];

    RequestHandler.handle(PlanningService.get(id, date), {
      id: "getDayplanningError",
      style: "SNACKBAR"
    }).catch(() => {}).then(planning => {
      this.buildings = planning.ronde.buildings;
      this.ronde = planning.ronde.name;
    });
  },
  methods: {
    capitalize(s: string) {
      return s.split(' ').map(s => s[0].toUpperCase() + s.slice(1)).join(' ');
    }
  },
  data: () => ({
    time: '',
    ronde: 'Er is nog geen ronde ingepland.',
    buildings: [{}]
  })
});
</script>
