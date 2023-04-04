<template>
  <v-row >
    <v-col/>
    <v-col align="center" cols="8">
        <h1 align="center"> {{ data.buildingName }} </h1>
    </v-col>
    <v-col align="right" cols="2">
        <v-avatar class="own-button-margin" >
          <v-icon v-on:click="goToFotoPage" dark size="30px" color="black">mdi-camera-outline</v-icon>
        </v-avatar>
    </v-col>
</v-row>
  <v-col align="center">
    <h4> {{ data.type }} </h4>
  </v-col>
  <div align="center">
      <v-col v-for="(fotoData, index) in fotoDataList" :key="index">
        <FotoCardStudent :data="fotoData"/>
      </v-col>
  </div>

  <v-row justify="end" v-if="fotoDataList.length > 0">
    <v-col cols="12" align="center">
      <NormalButton text="Taak voltooien" :parent-function="completeTask"/>
    </v-col>
  </v-row>

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
