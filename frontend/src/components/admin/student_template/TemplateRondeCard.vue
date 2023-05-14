<template>
<v-card
    class="mx-auto w-75 my-10"
    variant="outlined"
    :to="{name: 'ronde_dagplanningen', params: {template_id: data.template_id, ronde_id: data.ronde_id}}"
  >
    <v-card-item>
      <div>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-overline">
            {{ data.location }}
          </div>
        </v-row>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-h6">
            {{ data.name }}
          </div>
        </v-row>
      </div>
    </v-card-item>

    <v-card-actions class="px-3 my-1 justify-space-between">
      <v-btn variant="outlined" :to="{name: 'ronde_dagplanningen', params: {template_id: data.template_id, ronde_id: data.ronde_id}}">
        Dagplanningen
      </v-btn>
      <v-btn v-if="this.data.status !== 'Vervangen'" @click.prevent="on_delete" variant="outlined">
        Verwijderen
      </v-btn>
    </v-card-actions>
  </v-card>

</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import StudentTemplateService from "@/api/services/StudentTemplateService";
import router from "@/router";

export default {
  name: "TemplateRondeCard",
  props: {
    data: {
      type: Object,
      default: () => ({
        template_id: 0,
        ronde_id: 0,
        status: "Actief",
        name: 'Template Rondes Gent',
        location: 'Gent'
      })
    }
  },
  methods: {
    async on_delete() {
      const response = await RequestHandler.handle(StudentTemplateService.removeRound(this.data.template_id, this.data.ronde_id), {
          id: 'deleteRound',
          style: 'SNACKBAR'
      })
      if (response["new_id"] !== undefined) {
        const new_id = response["new_id"]
        this.$emit('copy', new_id)
      }
      this.$emit('round_removed')
    }
  }
}
</script>

<style scoped>

</style>
