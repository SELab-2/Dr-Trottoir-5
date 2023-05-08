<template>
  <v-container align="center">
    <v-card max-width="750px">
      <h1 align="center"> {{ data.buildingName }} </h1>
      <h4> {{ data.type }} </h4>
      <v-avatar class="own-button-margin w-100" align="center">
        <v-icon v-on:click="goToPhotoPage" dark size="40px" color="black">mdi-camera-outline</v-icon>
      </v-avatar>
      <FotoCardStudent v-for="(fotoData, index) in data.images" :key="index" :data="fotoData"
        :buildingName="data.buildingName" :type="data.type" :info="data.info"/>
      <NormalButton text="Taak voltooien" :parent-function="completeTask" class="mb-3 w-75"/>
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

import FotoCardStudent from '@/components/student/FotoCardStudent.vue'
import NormalButton from '@/components/NormalButton.vue'
import router from '@/router'

export default {
  name: 'OverviewScreenStudentPosts',
  components: { NormalButton, FotoCardStudent },
  props: {
    data: {
      type: Object,
      default: () => ({ buildingName: '', type: '', images: [], info: '', planning: '', building_id: '' })
    }
  },
  methods: {
    goToPhotoPage () {
      router.push({
name: 'student_post',
query: {
        building: this.data.buildingName,
type: this.data.type,
info: this.data.info,
planning: this.data.planning,
        building_id: this.data.building_id
      }
})
    },
    completeTask () {
      router.go(-1)
    }
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
