<template>
  <v-container align="center">
    <v-card v-if="building !== null">
      <v-card-title class="mt-2">
        <v-row>
          <v-col md="6" sm="6">
            <DatePicker v-model.string="date" color="white" :is-dark="true" :is-required="true" show-iso-weeknumbers
                        :first-day-of-week="1" :masks="masks" :attributes="attrs" view="weekly" v-on:dayclick="changed" />
          </v-col>
          <v-col sm="6" align="left" class="text-wrap">
            <h4 class="text-h4">
              Opmerkingen voor {{building.name}} op
              {{new Date(date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'})}}
            </h4>
          </v-col>
        </v-row>
      </v-card-title>
      <v-divider style="width: 90%;" class="mt-4"></v-divider>
    </v-card>

    <v-card v-else>
      <v-card-title class="text-center">
        <v-icon
          color="warning"
          icon="mdi-cancel"
          size="x-large"
        ></v-icon>
      </v-card-title>
      <v-spacer></v-spacer>
      <v-card-text>
        <v-row class="mx-auto justify-center">
          <div class="mx-1">Gebouw niet gevonden!</div>
        </v-row>
        <v-row class="my-4 justify-center">
          <div class="mx-1">Vraag uw syndicus om een nieuwe QR-Code door te geven.</div>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import NormalButton from "@/components/NormalButton.vue";
import QRCodeVue3 from "qrcode-vue3";

export default {
  name: "BuildingView",
  components: {QRCodeVue3, NormalButton},
  props: {id: String},
  data: () => ({
    building: null,
    masks: { modelValue: 'YYYY-MM-DD' },
    date: new Date().toISOString().split('T')[0],
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
  beforeMount() {

  },
  methods: {
    changed() {

    }
  }
}
</script>
