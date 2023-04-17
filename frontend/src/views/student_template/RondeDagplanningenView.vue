<template>
  <v-row class="mx-auto justify-center align-center mt-10">
    <div class="text-h2">Alle Dagplanningen van</div>
  </v-row>
  <v-row class="mx-auto justify-center align-center my-5">
    <div class="text-h2">{{name}}</div>
  </v-row>
  <DagPlanningCard v-for="dagplanning in dagplanningen" :data="{
    students: dagplanning.students,
    day: dagplanning.time.day,
    start_hour: dagplanning.time.start_hour,
    end_hour: dagplanning.time.end_hour
  }"></DagPlanningCard>
</template>

<script>
import DagPlanningCard from "@/components/admin/student_template/DagPlanningCard.vue";
import {RequestHandler} from "@/api/RequestHandler";
import StudentTemplateService from "@/api/services/StudentTemplateService";

export default {
  name: "RondeDagplanningenView",
  components: {
    DagPlanningCard
  },
  data: () => ({
    template_id: 0,
    ronde_id: 0,
    name: 'edddddddddddddd',
    location: null,
    dagplanningen: []
  }),
  async mounted() {
    this.template_id = this.$route.params.template_id
    this.ronde_id = this.$route.params.ronde_id
    this.dagplanningen = await RequestHandler.handle(StudentTemplateService.getDagPlanningen(this.template_id, this.ronde_id), {
      id: 'getDagplanningenError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

  }
}
</script>

<style scoped>

</style>
