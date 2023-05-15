<!--
Component for a specific building in the dayplanning of a user
Example usage:
<DayPlanBuilding :data="{<building data>}" />
-->

<template>
  <v-container align="center">
    <v-col cols="12" sm="10">
      <v-card data-test="building" class='px-2' elevation="5" @click="buildingClicked"
              :color="data.building.status === 'Voltooid' ? 'green-lighten-1' : data.building.status === 'Bezig' ? 'yellow-lighten-1' : 'red-lighten-1'">
        <v-card-title class="text-center">
          <v-row justify="center">
            <v-col cols="6" sm="5">
              <div data-test="name-building" class="text-wrap" v-if="data.building.name">{{ data.building.name }}</div>
              <div data-test="adres-building" class="text-caption text-wrap">{{ data.building.adres }}</div>
            </v-col>
            <v-col cols="6" sm="5">
              <div data-test="status">Status</div>
              <div data-test="status-building" class="text-caption">{{ data.building.status }}</div>
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
    </v-col>
  </v-container>
</template>

<script type="js">
import { defineComponent } from 'vue';
import router from "@/router";

export default defineComponent({
  name: 'DayPlanBuilding',
  props: {
    data: {
      type: Object,
      default: () => ({building: {adres: 'Leeg', status: 'Onbekend'}, planning: null})
    },
    date: {
      type: String,
      default: () => new Date().toISOString().split('T')[0]
    }
  },
  methods: {
    buildingClicked () {
      router.push({name: 'building_student', query: {
        building: this.data.building.id, planning: this.data.planning, year: this.data.year, week: this.data.week
      }});
    }
  }
})
</script>
