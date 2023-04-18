<template>
  <v-row class="justify-space-around align-center pt-8">
    <div class="text-h4 text-md-h2">
      Alle Dagplanningen
    </div>
    <v-btn :to="`/studenttemplates/${this.template_id}`" variant="outlined" >
        Terug
    </v-btn>
  </v-row>

  <DagPlanningCard v-for="dagplanning in dagplanningen" :data="{
    template_id: this.template_id,
    ronde_id: this.ronde_id,
    status: this.status,
    dag_id: dagplanning.id,
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
    status: "Actief",
    ronde_id: 0,
    name: 'Testnaam',
    location: null,
    dagplanningen: [],
    state_mapping: {
      "A": "Actief",
      "E": "Eenmalig",
      "V": "Vervangen",
      "I": "Inactief"
    }
  }),
  async mounted() {
    this.template_id = this.$route.params.template_id
    this.ronde_id = this.$route.params.ronde_id

    // get the status of template
    const template = await RequestHandler.handle(StudentTemplateService.getStudentTemplate(this.template_id), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => {});
    this.status = this.state_mapping[template.status]

    this.dagplanningen = await RequestHandler.handle(StudentTemplateService.getDagPlanningen(this.template_id, this.ronde_id), {
      id: 'getDagplanningenError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);
  }
}
</script>

<style scoped>

</style>
