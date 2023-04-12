<template>
  <v-container align="center">
    <v-card max-width="750px">
      <h1 align="center"> {{ data.buildingName }} </h1>
      <h4> {{ data.type }} </h4>
      <v-avatar class="own-button-margin" align="center">
        <v-icon v-on:click="goToFotoPage" dark size="40px" color="black">mdi-camera-outline</v-icon>
      </v-avatar>
      <FotoCardStudent v-for="(fotoData, index) in fotoDataList" :key="index" :data="fotoData" />
      <NormalButton text="Taak voltooien" :parent-function="completeTask" class="mb-3"/>
    </v-card>
  </v-container>
</template>

<script>

/**
 * OverviewScreenStudentPosts component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * buildingName: String
 * type: String (Aankomst of Vertrek of Berging)
 *
 * Data halen van backend voor de FotoCardStudent componenten zie ´mounted()´
 */

import FotoCardStudent from "@/components/student/FotoCardStudent.vue";
import NormalButton from "@/components/NormalButton.vue";

export default {
  name: 'OverviewScreenStudentPosts',
  components: {NormalButton, FotoCardStudent},
  data() {
    return {
      fotoDataList: []
    }
  },
  props: {
    data: {
      type: Object,
      default: () => ({buildingName: 'Gebouw test', type: "Aankomst"})
    }
  },
  methods: {
    goToFotoPage: function () {
      // TODO
    },
    completeTask: function () {
      // TODO
    }
  },
  async mounted() {
    // TODO data halen van backend
    this.fotoDataList = [
        { timeStamp: 'Empty', description: 'Empty', imageURL: 'empty' },
        { timeStamp: 'Empty', description: 'Empty', imageURL: 'empty' },
        { timeStamp: 'Empty', description: 'Empty', imageURL: 'empty' },
        { timeStamp: 'Empty', description: 'Empty', imageURL: 'empty' },
        { timeStamp: 'Empty', description: 'Empty', imageURL: 'empty' }
      ]
  }
}
</script>

<style scoped>
.own-button-margin {
  margin-right: 5px;
  margin-top: 5px;
}
h1 {
  max-width: 100%;
  word-wrap: break-word;
  white-space: normal;
  line-height: 1.5;
  hyphens: auto;
}
</style>
