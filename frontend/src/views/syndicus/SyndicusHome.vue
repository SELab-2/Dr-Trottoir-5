<template>
  <v-container align="center">
     <v-card>
       <v-card-title class="mt-2">
        <v-row>
          <v-col md="6" sm="6">
            <DatePicker v-model.string="date" color="white" :is-dark="true" :is-required="true" show-iso-weeknumbers
                        :first-day-of-week="1" :masks="masks" :attributes="attrs" view="weekly" />
          </v-col>
          <v-col sm="6" align="left" class="text-wrap">
            <h4 class="text-h4">
              Opmerkingen voor ?? op {{new Date(date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'})}}
            </h4>
            <v-autocomplete
              label="Gebouw" :items="buildings" class="mt-4" style="width: 50%;"
              v-model="building" item-title="name"  return-object
              variant="outlined"
            ></v-autocomplete>
          </v-col>
        </v-row>
      </v-card-title>
      <v-divider style="width: 90%;" class="mt-4"></v-divider>
     </v-card>
  </v-container>
</template>

<script>
import { DatePicker } from 'v-calendar';
import 'v-calendar/dist/style.css';
export default {
  name: "SyndicusHome",
  components: {DatePicker},
  data: () => ({
    date: new Date().toISOString().split('T')[0],
    buildings: [],
    building: null,
    masks: { modelValue: 'YYYY-MM-DD' },
    attrs: [
      {
        dates: new Date(),
        popover: {
          label: 'Glas'
        },
        dot: 'yellow'
      },
      {
        dates: new Date(),
        popover: {
          label: 'GFT'
        },
        dot: 'green'
      }
    ]
  }),
}
</script>
