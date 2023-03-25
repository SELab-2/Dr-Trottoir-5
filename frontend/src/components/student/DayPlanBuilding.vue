<!--
Component for a specific building in the dayplanning of a user
Example usage:
<DayPlanBuilding building-name="Sterre S8" building-info="Krijgslaan 281-S8, 9000 Gent" status="niet voltooid" />
-->

<template>
  <v-container align="center">
    <v-col cols="12" sm="10">
      <v-card class='px-4 rounded-pill' elevation="5" @click="buildingClicked"
              :color="status === 'voltooid' ? 'green-lighten-1' : status === 'bezig' ? 'yellow-lighten-1' : 'red-lighten-1'">
        <v-card-title class="text-center">
          <v-row justify="center">
            <v-col cols="6" sm="5">
              <div class="text-wrap">{{ buildingName }}</div>
              <div class="text-caption text-wrap">{{ buildingInfo }}</div>
            </v-col>
            <v-col cols="6" sm="5">
              <div>Status</div>
              <div class="text-caption">{{ status }}</div>
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'DayPlanBuilding',
  props: {
    buildingName: { type: String, default: 'Resto S5' },
    buildingInfo: { type: String, default: 'Krijgslaan 281, 9000 Gent' },
    status: { type: String, default: 'bezig' }
  },
  data: () => ({}),
  methods: {
    buildingClicked () {
      // TODO: redirect to building page
    }
  }
})
</script>
