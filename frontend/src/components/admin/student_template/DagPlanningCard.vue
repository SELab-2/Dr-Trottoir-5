<template>
  <v-card
    class="mx-auto w-75 my-10"
    variant="outlined"
    :to="{name: 'dagplanning_edit', params: {template_id: data.template_id, ronde_id: data.ronde_id, dag_id: data.dag_id}}"
  >
    <v-card-item>
      <div>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-h6">
            {{
              data.students.length > 0 ? data.students.map(student => student.first_name).join(", ") : 'Er zijn geen studenten aangewezen'
            }}
          </div>
          <div class="text-overline">
            {{ format_day(data.day) }}
          </div>
        </v-row>
        <v-row class="px-3 my-1 justify-start">
          <div class="text-overline">
            {{ data.start_hour + '    -   ' }}
          </div>
          <div class="text-overline">
            {{ data.end_hour }}
          </div>
        </v-row>
      </div>
    </v-card-item>

    <v-card-actions v-if="this.data.status !== 'Vervangen'" class="px-3 my-1 justify-space-between">
      <v-btn variant="outlined"
             :to="{name: 'dagplanning_edit', params: {template_id: data.template_id, ronde_id: data.ronde_id, dag_id: data.dag_id}}">
        Dagplanning aanpassen
      </v-btn>
      <v-btn @click.prevent="remove_dagplanning" variant="outlined">
        Verwijderen
      </v-btn>
    </v-card-actions>
    <div v-if="this.data.status === 'Vervangen'" class="px-3 text-caption">Om deze template aan te passen moeten eerst
      de eenmalige aanpassingen ongedaan worden.
    </div>
  </v-card>

</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import StudentTemplateService from "@/api/services/StudentTemplateService";
import router from "@/router";

export default {
  name: "DagPlanningCard",
  props: {
    data: {
      type: Object,
      default: () => ({
        template_id: 0,
        ronde_id: 0,
        status: "Actief",
        dag_id: 0,
        students: [],
        day: 'MO',
        start_hour: '17:00',
        end_hour: '20:00'
      })
    }
  },
  methods: {
    format_day(day) {
      const day_mapping = {
        "MO": "Maandag",
        "TU": "Dinsdag",
        "WE": "Woensdag",
        "TH": "Donderdag",
        "FR": "Vrijdag",
        "SA": "Zaterdag",
        "SU": "Zondag",
      }
      return day_mapping[day]
    },
    async remove_dagplanning() {
      const response = await RequestHandler.handle(StudentTemplateService.deleteDagPlanning(this.data.template_id, this.data.dag_id), {
        id: "deleteDagplanningError",
        style: "SNACKBAR"
      }).then(res => res).catch(() => {})
      this.$emit('remove', response["new_id"])
    }
  }
}
</script>

<style scoped>

</style>
