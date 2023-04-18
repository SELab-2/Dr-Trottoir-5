<template>
  <v-row class="justify-space-evenly align-center py-5">
    <div class="text-h4 text-md-h2 text-lg-h1">
      Studenten Templates
    </div>
    <v-btn :to="'/studenttemplates/add'" variant="outlined" >
        Nieuwe Aanmaken
    </v-btn>
  </v-row>
  <StudentTemplateCard @removed="remove_template" v-for="template in templates" :data="{
      template_id: template.id,
      name: template.name,
      location: template.location.name,
      even: template.even,
      status: state_mapping[template.status]
    }"></StudentTemplateCard>
</template>

<script>
import StudentTemplateCard from "@/components/admin/student_template/StudentTemplateCard.vue";
import StudentTemplateService from "@/api/services/StudentTemplateService";
import {RequestHandler} from "@/api/RequestHandler";

export default {
  name: "StudentTemplateView",
  components: {StudentTemplateCard},
  data: () => ({
    templates: [],
    state_mapping: {
      "A": "Actief",
      "E": "Eenmalig",
      "V": "Vervangen",
      "I": "Inactief"
    }
  }),
  async created() {
    this.templates = await RequestHandler.handle(StudentTemplateService.getStudentTemplates(), {
        id: "getStudentTemplatesError",
        style: "SNACKBAR"
      }).then(templates => templates).catch(() => []);
  },
  methods: {
    async remove_template() {
      this.templates = await RequestHandler.handle(StudentTemplateService.getStudentTemplates(), {
        id: "getStudentTemplatesError",
        style: "SNACKBAR"
      }).then(templates => templates).catch(() => []);
    }
  }

}
</script>

<style scoped>

</style>
