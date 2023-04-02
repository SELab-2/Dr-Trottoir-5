<template>
  <v-row >
    <v-col align="right">
        <v-avatar class="own-button-margin" >
          <v-icon v-on:click="goToFotoPage" dark size="30px" color="black">mdi-camera-outline</v-icon>
        </v-avatar>
    </v-col>
  </v-row>

  <h1 align="center"> {{ data.buildingName }} </h1>

  <v-col align="center">
    <h3> {{ data.type }} </h3>
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
</style>
