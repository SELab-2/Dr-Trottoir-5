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
        <v-col align="center" md="2" xs="6" class="ml-3">
          <v-list>
            <v-list-group value="Student(en)">
              <template v-slot:activator="{ props }">
                <v-list-item rounded
                             v-bind="props"
                ><p class="text-wrap">Student(en)</p></v-list-item>
              </template>
              <v-list-item v-for="(student, i) in data.round.students" :key="i"
              ><p class="text-wrap">{{student.first_name}} {{student.last_name}}</p></v-list-item>
            </v-list-group>
          </v-list>
        </v-col>
        <v-col align="right" md="1" xs="2" class="my-3 mx-2">
          <v-icon icon="mdi-information-outline" size="x-large" @click="info"></v-icon>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";

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
    info() {
      // TODO
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
