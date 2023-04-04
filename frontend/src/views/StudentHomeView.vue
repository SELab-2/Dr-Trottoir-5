<template>
  <v-container align="center">
    <v-card>
      <v-card-title class="mt-1">
        <h1>Planning</h1>
      </v-card-title>
      <v-card-text class="mt-3">
        <DatePicker v-model.string="date" :masks="masks" color="yellow" :is-dark="true" :is-required="true" view="weekly" show-iso-weeknumbers />
      </v-card-text>
      <v-card-text>
        <normal-button text="Bekijk planning" v-bind:parent-function="selectDay" block></normal-button>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { DatePicker } from 'v-calendar';
import NormalButton from "@/components/NormalButton.vue";
import 'v-calendar/dist/style.css';

export default defineComponent({
  name: 'StudentHomeView',
  components: {
    DatePicker,
    NormalButton
  },
  methods: {
    selectDay() {

    }
  },
  data: () => {
    return {
      date: new Date().toISOString().split('T')[0],
      masks: { modelValue: 'YYYY-MM-DD' }
    }
  }
});

</script>
