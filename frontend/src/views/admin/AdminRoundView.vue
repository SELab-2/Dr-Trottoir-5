<template>
  <v-container align="center">
    <v-card v-if="planning !== null" elevation="0" class="py-3">
      <v-row>
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <h1>Ronde {{ planning.ronde.name }} op {{ dateString }}{{ planning.students.length > 0 ? ' door' : '' }}</h1>
        </v-col>
        <v-col cols="2">
          <v-btn v-if="template !== null"
                 :to="`/studenttemplates/${template}/rondes/${planning.ronde.id}/dagplanningen/${planning.id}`"
                 class="my-2" color="primary"><v-icon color="secondary" icon="mdi-pencil"></v-icon></v-btn>
        </v-col>
      </v-row>
      <h2 v-for="student in planning.students"><a :href="'/admin/gebruiker/'+student.id" style="text-decoration: none;">
        {{student.first_name}} {{student.last_name}}</a></h2>
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
      <v-card class="mt-8 py-4" style="max-width: 95%;">
        <v-row>
          <v-col cols="2"><h5 class="text-h5 font-weight-bold">Totaal</h5></v-col>
          <v-col cols="2"><h5 class="text-h5">{{status}}</h5></v-col>
          <v-col cols="2"><h5 class="text-h5" v-if="pictures !== null">
            {{Object.keys(pictures).filter(p => pictures[p].remark !== '').length}} opmerkingen</h5></v-col>
          <v-col cols="1"><h5 class="text-h5" v-if="duration !== null">{{duration}}</h5></v-col>
        </v-row>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import NormalButton from "@/components/NormalButton.vue";
import FollowUpRoundBuildingCard from "@/components/admin/FollowUpRoundBuildingCard.vue";
import {getWeek} from "@/api/DateUtil";

export default {
  name: "AdminRoundView",
  components: {FollowUpRoundBuildingCard, NormalButton},
  data: () =>({
    date: null,
    dateString: "",
    planning: null,
    pictures: null,
    duration: null,
    template: null,
    status: "Niet voltooid"
  }),
  created() {
    if ('date' in this.$route.query) this.date = new Date(this.$route.query.date);
    this.dateString = this.date.toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'});
    if ('planning' in this.$route.query) {
      RequestHandler.handle(PlanningService.getPlanning(this.$route.query.planning), {
        id: `getPlanningError`,
        style: "SNACKBAR"
      }).then(planning => this.planning = planning).catch(() => null);

      RequestHandler.handle(PlanningService.findTemplate(this.$route.query.planning), {
        id: 'findTemplateError',
        style: "NONE"
      }).then(t => this.template = t.template_id).catch(() => null);

      RequestHandler.handle(PlanningService.getStatusPictures(this.date.getFullYear(),
        getWeek(this.date), this.$route.query.planning), {
        id: `getPicturesError`,
        style: "SNACKBAR"
      }).then(pictures => {
        this.pictures = pictures;
        const times = Object.keys(pictures).map(p => pictures[p].map(t => new Date(t.time)))
                .flat().sort((p1, p2) => p1 < p2 ? -1 : 1);
        if (times.length > 0) {
          const secs = (times[times.length - 1].getTime() - times[0].getTime()) / 1000;
          const minutes = Math.floor(secs / 60);
          const seconds = Math.round(secs - minutes * 60);
          this.duration = `${minutes}min ${seconds}s`;
        } else this.duration = '-';

        if (Object.keys(pictures).every(p => pictures[p].some(pic => pic.pictureType === 'DE'))) this.status = 'Voltooid';
        else if (Object.keys(pictures).some(p => pictures[p].length > 0)) this.status = 'bezig';
      }).catch(() => null);
    }
  }
}
</script>
