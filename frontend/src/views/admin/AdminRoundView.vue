<template>
  <v-container align="center">
    <v-card v-if="planning !== null" elevation="0" class="py-3">
      <v-row>
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <h1>Ronde {{ planning.ronde.name }} op {{ dateString }} door</h1>
        </v-col>
        <v-col cols="2">
          <v-btn class="my-2" color="primary"><v-icon color="secondary" icon="mdi-pencil"></v-icon></v-btn>
        </v-col>
      </v-row>
      <h2 v-for="student in planning.students">{{student.first_name}} {{student.last_name}}</h2>
      <v-card class="mt-4 py-4" style="max-width: 95%;">
        <v-row>
          <v-col cols="2"><h5 class="text-h5">Gebouw</h5></v-col>
          <v-col cols="2"><h5 class="text-h5">Status</h5></v-col>
          <v-col cols="2"><h5 class="text-h5">Opmerkingen</h5></v-col>
          <v-col cols="1"><h5 class="text-h5">Tijd</h5></v-col>
          <v-col cols="5"><h5 class="text-h5">Locatie</h5></v-col>
        </v-row>
      </v-card>
      <FollowUpRoundBuildingCard v-for="building in planning.ronde.buildings" class="my-4" style="max-width: 95%;"
                                 v-if="pictures !== null"
                                 :data="{building: building, pictures: pictures[building.id], optimalDuration: 15 * 60}">
      </FollowUpRoundBuildingCard>
    </v-card>
  </v-container>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import NormalButton from "@/components/NormalButton.vue";
import FollowUpRoundBuildingCard from "@/components/admin/FollowUpRoundBuildingCard.vue";

export default {
  name: "AdminRoundView",
  components: {FollowUpRoundBuildingCard, NormalButton},
  data: () =>({
    date: null,
    dateString: "",
    planning: null,
    pictures: null
  }),
  methods: {
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
  created() {
    if ('date' in this.$route.query) this.date = new Date(this.$route.query.date);
    this.dateString = this.date.toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'});
    if ('planning' in this.$route.query) {
      RequestHandler.handle(PlanningService.getPlanning(this.$route.query.planning), {
        id: `getPlanningError`,
        style: "SNACKBAR"
      }).then(planning => this.planning = planning).catch(() => null);

      RequestHandler.handle(PlanningService.getStatusPictures(this.date.getFullYear(),
        this.getWeek(this.date), this.$route.query.planning), {
        id: `getPicturesError`,
        style: "SNACKBAR"
      }).then(pictures => this.pictures = pictures).catch(() => null);
    }
  }
}
</script>
