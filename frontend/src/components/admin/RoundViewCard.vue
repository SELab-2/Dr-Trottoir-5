<!--
This component is used in the admin and superstudent dashboard view,
it displays the information of one round so that a list of round views can easily be made
-->
<template>
  <v-container align="center" style="width: 80%;">
    <v-card>
      <v-row>
        <v-col align="left" class="ml-4 my-2" md="2" xs="12">
          <h5 class="text-h5 text-wrap font-weight-bold">Ronde {{data.round.ronde.name}}</h5>
        </v-col>
        <v-col align="left" md="2" class="my-3" xs="12">
          <p class="text-subtitle-1 font-weight-bold">{{data.date}}</p>
        </v-col>
        <v-col align="left" md="3" xs="10">
          <v-progress-linear color="green" :model-value="this.percentage"
                             :height="20" class="my-4 mx-2" rounded="xl"
          style="width: 35vw; max-width: 100%;">
          </v-progress-linear>
        </v-col>
        <v-col align="left" md="1" xs="1" class="my-3 ml-4">
          <v-icon v-if="this.percentage === 100"
                  icon="mdi-check" color="green" size="x-large"></v-icon>
        </v-col>
        <v-col align="center" md="2" xs="6" class="ml-3 my-1">
          <v-expansion-panels style="width: 90%;">
            <v-expansion-panel :title="data.round.students.length + ` student${data.round.students.length === 1 ? '' : 'en'}`"
                               :disabled="data.round.students.length === 0">
              <v-expansion-panel-text v-if="data.round.students.length > 0">
                <p style="word-wrap: break-word;" v-for="s in data.round.students" class="mt-2">
                  <a :href="'/admin/gebruiker/'+s.id" style="text-decoration: none;">
                  {{ s.first_name }} {{ s.last_name }}</a></p>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
        <v-col align="right" md="1" xs="2" class="my-3 mx-2">
          <v-icon icon="mdi-information-outline" size="x-large" @click="info" v-if="data.round.students.length > 0"></v-icon>
          <v-icon v-else icon="mdi-plus-circle" size="x-large" @click="plan"></v-icon>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import router from "@/router";

export default {
  name: "RoundViewCard",
  data: () => ({
    percentage: 0,
    users: [],
    count: 0
  }),
  created() {
    this.getStatus();
  },
  props: {
    data: {
      type: Object,
      default: () => ({
        round: {ronde: {name: ''}, id: -1},
        date: ''
      })
    }
  },
  watch: {
    data: function() {
      this.count++;
      if (this.count % 2 === 0) this.getStatus();
    }
  },
  methods: {
    router() {
      return router
    },
    info() {
      router.push({name: 'adminRoundView', query: {planning: this.data.round.id, date: this.data.date}});
    },
    plan() {
      router.push({name: 'studenttemplates'});
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
    },
    getStatus() {
      const date = new Date(this.data.date);
      this.percentage = 0;

      RequestHandler.handle(PlanningService.getStatus(date.getFullYear(), this.getWeek(date), this.data.round.id), {
        id: `getStatus${this.data.round.id}Error`,
        style: "NONE"
      }).then(statuses => {
        let progress = 0;
        for (let id in statuses) {
          const status = statuses[id];
          progress += status.DE > 0 ? 3 : status.ST > 0 ? 2 : status.AR > 0 ? 1 : 0;
        }
        this.percentage = progress / (this.data.round.ronde.buildings.length * 3) * 100;
      }).catch(() => null);
    }
  }
}
</script>
