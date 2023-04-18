<!--
This component is used in the admin and superstudent dashboard view,
it displays the information of one round so that a list of round views can easily be made
-->
<template>
  <v-container align="center" style="width: 80%;">
    <v-card>
      <v-row>
        <v-col align="left" class="ml-4 my-2" cols="2" xs="3">
          <h5 class="text-h5 text-wrap font-weight-bold">Ronde Sterre</h5>
        </v-col>
        <v-col align="left" cols="2" class="my-3" xs="2">
          <p class="text-subtitle-1 font-weight-bold">2023-04-18</p>
        </v-col>
        <v-col align="left" cols="3" xs="4">
          <v-progress-linear color="green" :model-value="percentage" :height="20" class="my-4" rounded="xl">
          </v-progress-linear>
        </v-col>
        <v-col align="left" cols="1" class="my-3 ml-4">
          <v-icon v-if="percentage === 100" icon="mdi-check" color="green" size="x-large"></v-icon>
        </v-col>
        <v-col align="center" cols="2" class="my-3 ml-4">
          <p class="text-subtitle-1 font-weight-bold">Pieter</p>
        </v-col>
        <v-col align="right" cols="1" class="my-3 ml-2">
          <v-icon icon="mdi-information-outline" size="x-large" @click="info"></v-icon>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "RoundViewCard",
  data: () => ({
    percentage: 100
  }),
  methods: {
    info() {

    }
  }
}
</script>

