<template>
  <v-container align="center">
    <v-card>
      <v-card-title class="mt-2">
        <v-row>
          <v-col cols="6">
            <v-card flat>
              <DatePicker v-model.string="date" color="yellow" :is-dark="true" :is-required="true" show-iso-weeknumbers
                          :first-day-of-week="1" v-on:dayclick="changed" :masks="masks"/>
            </v-card>
          </v-col>
          <v-col cols="6" align="left" class="text-wrap">
            <h4 class="text-h4">
              Planning in {{location}} op {{new Date(date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'})}}
            </h4>
            <v-autocomplete
              label="Locatie" :items="locations" class="mt-4" style="width: 50%;"
              v-model="location" item-title="name" v-on:update:modelValue="changed"
              variant="outlined"
            ></v-autocomplete>
            <v-text-field append-icon="mdi-magnify" v-model="search" label="Ronde" style="width: 50%;" variant="outlined"
                          @click:append="doSearch" @keydown.enter="doSearch"
            ></v-text-field>
              <v-btn-toggle
              v-model="toggle"
              color="green"
              multiple mandatory
            >
                  <v-btn value="0" variant="outlined" class="rounded-s-pill" style="width: 48%;">
                    <p class="text-wrap">Ingeplande rondes</p></v-btn>
                  <v-btn value="1" variant="outlined" class="rounded-e-pill" style="width: 48%;">
                    <p class="text-wrap">Niet ingeplande rondes</p></v-btn>
            </v-btn-toggle>
          </v-col>
        </v-row>
      </v-card-title>
      <v-divider style="width: 90%;" class="mt-4"></v-divider>
      <v-card-text class="mt-3">
        <RoundViewCard v-for="round in rounds" />
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
export default {
  name: "DashboardView",
  components: {RoundViewCard, DatePicker},
  async created() {
    RequestHandler.handle(RoundService.getLocations(), {
      id: 'getLocationsError',
      style: 'none'
    }).then(l => {
      this.locations = l;
      if (l.length > 0) this.location = l[0].name;
      this.changed();
    }).catch(() => null);
  },
  methods: {
    changed() {
      console.log(`Changed: ${this.location} ${this.date}`)
    },
    doSearch() {
      console.log(`Searching for ${this.search} in rounds..`)
    }
  },
  data: () => ({
    date: new Date().toISOString().split('T')[0],
    locations: [],
    location: '',
    search: '',
    toggle: ['0'],
    rounds: [1,2],
    masks: { modelValue: 'YYYY-MM-DD' }
  })
}
</script>
