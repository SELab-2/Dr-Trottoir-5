<template>
  <v-row class="justify-space-around align-center pt-8">
    <div class="text-h4 text-md-h2">
      Alle Dagplanningen
    </div>
    <v-btn :to="{name: 'studenttemplate', params: {id: this.template_id}}" variant="outlined">
      Terug
    </v-btn>
  </v-row>
  <DagPlanningCard @remove="remove_dagplanning" v-for="dagplanning in dagplanningen" :data="{
    template_id: this.template_id,
    ronde_id: this.ronde_id,
    status: this.status,
    dag_id: dagplanning.id,
    students: dagplanning.students,
    day: dagplanning.time.day,
    start_hour: dagplanning.time.start_hour,
    end_hour: dagplanning.time.end_hour
  }" :key="dagplanning.id"></DagPlanningCard>
  <v-row class=" align-center justify-center pb-15">
    <v-col cols="12" sm="3" md="3">
      <NormalButton v-if="this.status !== 'Vervangen'" text="Nieuwe dagplanning aanmaken"
                    :to="{name: 'dagplanning_add', params: {template_id: this.template_id, ronde_id: this.ronde_id}}"
                    block></NormalButton>
    </v-col>
  </v-row>
</template>

<script>
import DagPlanningCard from "@/components/admin/student_template/DagPlanningCard.vue";
import {RequestHandler} from "@/api/RequestHandler";
import StudentTemplateService from "@/api/services/StudentTemplateService";
import NormalButton from "@/components/NormalButton.vue";
import router from "@/router";

export default {
  name: "RondeDagplanningenView",
  components: {
    DagPlanningCard,
    NormalButton
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
    }).then(result => result).catch(() => null);
    this.status = this.state_mapping[template.status]

    this.dagplanningen = await RequestHandler.handle(StudentTemplateService.getDagPlanningen(this.template_id, this.ronde_id), {
      id: 'getDagplanningenError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);
    this.sort_dagplanning()
  },
  methods: {
    async remove_dagplanning(new_template_id) {
      if (new_template_id === undefined) new_template_id = this.template_id

      this.template_id = new_template_id
      this.dagplanningen = await RequestHandler.handle(StudentTemplateService.getDagPlanningen(this.template_id, this.ronde_id), {
        id: 'getDagplanningenError',
        style: 'SNACKBAR'
      }).then(result => result).catch(() => []);
      this.sort_dagplanning()
      return await router.push({name: 'ronde_dagplanningen', params: {template_id: this.template_id, ronde_id: this.ronde_id}})
    },
    sort_dagplanning() {
      const sorted_dagplanningen = []
      for (const day of ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']) {
        for (const dagplanning of this.dagplanningen) {
          if (dagplanning.time.day === day) {
            sorted_dagplanningen.push(dagplanning)
          }
        }
      }
      this.dagplanningen = sorted_dagplanningen
    }
  }
}
</script>

<style scoped>

</style>
