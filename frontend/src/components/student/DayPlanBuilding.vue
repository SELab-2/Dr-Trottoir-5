<!--
Component for a specific building in the dayplanning of a user
Example usage:
<DayPlanBuilding :data="{<building data>}" />
-->

<template>
  <v-container align="center">
    <v-col cols="12" sm="10">
      <v-card class='px-4 rounded-pill' elevation="5" @click="buildingClicked"
              :color="data.status === 'voltooid' ? 'green-lighten-1' : data.status === 'bezig' ? 'yellow-lighten-1' : 'red-lighten-1'">
        <v-card-title class="text-center">
          <v-row justify="center">
            <v-col cols="6" sm="5">
              <div class="text-wrap" v-if="data.location">{{ data.location.name }}</div>
              <div class="text-caption text-wrap">{{ data.adres }}</div>
            </v-col>
            <v-col cols="6" sm="5">
              <div>Status</div>
              <div class="text-caption">{{ data.status }}</div>
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
    </v-col>
  </v-container>
</template>

<script type="js">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'DayPlanBuilding',
  props: {
    data: {
      type: Object,
      default: () => ({ adres: 'Leeg', status: 'Onbekend' })
    }
  },
  methods: {
    buildingClicked () {
      // TODO: redirect to building page
    }
  }
})
</script>
