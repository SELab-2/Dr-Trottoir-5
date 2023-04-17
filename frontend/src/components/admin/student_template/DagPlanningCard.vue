<template>
<v-card
    class="mx-auto w-75 my-10"
    variant="outlined"
    :to="`/studenttemplates/${data.template_id}`"
  >
    <v-card-item>
      <div>
        <v-row class="px-3 my-1 justify-space-between">
           <div class="text-h6">
            {{ data.students === [] ? data.students.join(", ") : 'Er zijn geen studenten aangewezen'}}
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
            {{ data.end_hour}}
          </div>
        </v-row>
      </div>
    </v-card-item>

    <v-card-actions class="px-3 my-1 justify-space-between">
      <v-btn variant="outlined" to="/unauthorized">
        Dagplanning aanpassen
      </v-btn>
      <v-btn variant="outlined">
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
  name: "DagPlanningCard",
  props: {
    data: {
      type: Object,
      default: () => ({
        template_id: 0,
        ronde_id: 0,
        students: ['Tom', 'Bart'],
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
    }
  }
}
</script>

<style scoped>

</style>
