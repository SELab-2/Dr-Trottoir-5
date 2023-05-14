<template>
  <v-container align="center">
    <v-card>
      <v-card-title class="mt-2">
        <v-row>
          <v-col md="6" sm="6">
            <v-card flat>
              <DatePicker v-model.string="date" color="yellow" :is-dark="true" :is-required="true" show-iso-weeknumbers
                          :first-day-of-week="1" v-on:dayclick="changed" :masks="masks"/>
            </v-card>
          </v-col>
          <v-col sm="6" align="left" class="text-wrap">
            <h4 class="text-h4">
              Planning in {{location.name}} op {{new Date(date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'})}}
            </h4>
            <v-autocomplete
              label="Locatie" :items="locations" class="mt-4" style="width: 50%;"
              v-model="location" item-title="name" v-on:update:modelValue="changed" return-object
              variant="outlined"
            ></v-autocomplete>
            <v-text-field append-icon="mdi-magnify" v-model="search" label="Ronde" style="width: 50%;" variant="outlined"
                          @click:append="filter" @keyup="filter"
            ></v-text-field>
              <v-btn-toggle
              v-model="toggle"
              color="green"
              multiple mandatory
            >
                  <v-btn value="0" variant="outlined" class="rounded-s-pill" style="width: 48%;" @click="filter">
                    <p class="text-wrap">Ingeplande rondes</p></v-btn>
                  <v-btn value="1" variant="outlined" class="rounded-e-pill" style="width: 48%;" @click="filter">
                    <p class="text-wrap">Niet ingeplande rondes</p></v-btn>
            </v-btn-toggle>
          </v-col>
        </v-row>
      </v-card-title>
      <v-divider style="width: 90%;" class="mt-4"></v-divider>
      <v-card-text class="mt-3">
        <RoundViewCard v-for="round in show" :data="{round: round, date: date}" />
        <NormalButton v-if="rounds.length === 0" text="Nieuwe planning" v-bind:parent-function="plan" />
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { DatePicker } from 'v-calendar';
import 'v-calendar/dist/style.css';
import {RequestHandler} from "@/api/RequestHandler";
import RoundService from "@/api/services/RoundService";
import RoundViewCard from "@/components/admin/RoundViewCard.vue";
import PlanningService from "@/api/services/PlanningService";
import NormalButton from "@/components/NormalButton.vue";
import router from "@/router";
import {getWeek} from "@/api/DateUtil";

export default {
  name: "DashboardView",
  components: {NormalButton, RoundViewCard, DatePicker},
  async created() {
    RequestHandler.handle(RoundService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(l => {
      this.locations = l;
      if (l.length > 0) this.location = l[0];
      this.changed();
    }).catch(() => null);
  },
  methods: {

    plan() {
      router.push({name: 'add_studenttemplate'});
    },
    async changed() {
      const date = new Date(this.date);
      const week = getWeek(this.date);

      const rounds = await RequestHandler.handle(PlanningService.getRounds(date.getFullYear(), week, date.getUTCDay(), this.location.id), {
        id: 'getRoundsError',
        style: 'NONE'
      }).then(rounds => rounds).catch(() => []);
      this.rounds = rounds;
      this.show = rounds;
      this.filter();
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
    filter() {
      this.show = this.rounds.filter(r => (
        ((this.toggle.includes('0') && r.students.length > 0) || (this.toggle.includes('1') && r.students.length === 0))
        &&
        r.ronde.name.toLowerCase().includes(this.search.toLowerCase())
      ));
    }
  },
  data: () => ({
    date: new Date().toISOString().split('T')[0],
    locations: [],
    location: {name: ''},
    search: '',
    toggle: ['0'],
    rounds: [],
    show: [],
    masks: { modelValue: 'YYYY-MM-DD' }
  })
}
</script>
