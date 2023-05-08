<template>
<v-card
    class="mx-auto w-75 my-10"
    variant="outlined"
    :to="{name: 'studenttemplate', params: {id: data.template_id}}"
  >
    <v-card-item>
      <div>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-overline">
            {{ data.location }}
          </div>
          <div class="text-overline">
            {{ data.even ? "even" : "oneven" }}
          </div>
        </v-row>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-h6">
            {{ data.name }}
          </div>
          <div class="text-caption">{{ data.status }}</div>
        </v-row>
      </div>
    </v-card-item>

    <v-card-actions v-if="this.data.status !== 'Vervangen'" class="px-3 my-1 justify-space-between">
      <v-btn variant="outlined" :to="{name: 'studenttemplate', params: {id: data.template_id}}">
        Aanpassen
      </v-btn>
      <v-btn variant="outlined" @click.prevent="delete_template()">
        Verwijderen
      </v-btn>
    </v-card-actions>
    <div v-if="this.data.status === 'Vervangen'" class="px-3 text-caption">Om deze template aan te passen moeten eerst de eenmalige aanpassingen ongedaan worden.</div>
  </v-card>

</template>

<script>
import { RequestHandler } from '@/api/RequestHandler'
import StudentTemplateService from '@/api/services/StudentTemplateService'

export default {
  name: 'StudentTemplateCard',
  props: {
    data: {
      type: Object,
      default: () => ({
        template_id: 0,
        name: 'Template Rondes Gent',
        location: 'Gent',
        even: true,
        status: 'Actief'
      })
    }
  },
  methods: {
    async delete_template () {
      await RequestHandler.handle(StudentTemplateService.deleteStudentTemplate(this.data.template_id), {
          id: 'deleteStudentTemplate',
          style: 'SNACKBAR'
      })
      this.$emit('removed')
    }
  }
}
</script>

<style scoped>

</style>
