<template>
  <v-col align="center">
    <h1>Resto s5</h1>
    <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
    </v-btn>
    <h3>Aankomst</h3>
  </v-col>

  <FotoCardStudent/>
  <FotoCardStudent/>
</template>



<script>
import FotoCardStudent from "@/components/student/FotoCardStudent.vue";

export default {
  name: 'OverviewScreenStudentPosts',
  components: {FotoCardStudent},
  props: {
    data: {
      type: Object,
      default: () => ({name: 'Empty', argsCount: 0})
    }
  }
}
</script>

<style scoped>

</style>
