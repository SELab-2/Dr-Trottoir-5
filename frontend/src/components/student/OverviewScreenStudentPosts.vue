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
    <FotoCardStudent/>
    <FotoCardStudent/>
    <FotoCardStudent/>
    <FotoCardStudent/>
    <FotoCardStudent/>
  </div>

</template>

<script>
import FotoCardStudent from "@/components/student/FotoCardStudent.vue";

export default {
  name: 'OverviewScreenStudentPosts',
  components: {FotoCardStudent},
  props: {
    data: {
      type: Object,
      default: () => ({buildingName: 'Gebouw test', type: "Aankomst"})
    }
  },
  methods: {
    goToFotoPage: function () {
      // TODO
    }
  },
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
