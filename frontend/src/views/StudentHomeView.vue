<template>
  <v-container align="center">
    <v-card height="auto" max-width="750px">
      <v-card-title class="mt-2">
        <h4 class="text-h4">Planning</h4>
      </v-card-title>
      <v-card-text class="mt-8 mb-6">
        <DatePicker v-model.string="date" :masks="masks" color="yellow" :is-dark="true" :is-required="true" view="weekly"
                    show-iso-weeknumbers :first-day-of-week="1" expanded />
      </v-card-text>
      <v-card-text>
        <normal-button text="Bekijk planning" v-bind:parent-function="selectDay" block class="mb-3"></normal-button>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { DatePicker } from 'v-calendar';
import NormalButton from "@/components/NormalButton.vue";
import 'v-calendar/dist/style.css';
import router from '@/router';

export default defineComponent({
  name: 'StudentHomeView',
  components: {
    DatePicker,
    NormalButton
  },
  methods: {
    selectDay() {
      router.push({ path: '/dagplanning', query: { date: this.date } });
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
