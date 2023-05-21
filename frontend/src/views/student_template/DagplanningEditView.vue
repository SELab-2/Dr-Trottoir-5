<template>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-5">
        <div class="text-h3 mx-5 mb-5">{{ format_day(this.day) }}</div>
        <v-btn :to="{name: 'ronde_dagplanningen', params: {template_id: this.template_id, ronde_id: this.ronde_id}}" variant="outlined" >
            Terug
        </v-btn>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-select
            :error-messages="check_errors(this.errors, 'students')"
            :readonly="this.status === 'Vervangen'"
            label="Studenten"
            :items="all_students.filter(student => student.role !== 'AA' && student.role !== 'SY' && student.locations.includes(this.location.id))"
            :item-title="getTitle"
            item-value="id"
            multiple
            chips
            v-model="students"
          ></v-select>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='start_hour' :error-messages="check_errors(this.errors, 'start_hour')" label='Startuur' :readonly="this.status === 'Vervangen'" required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='end_hour' :error-messages="check_errors(this.errors, 'end_hour')" label='Einduur' :readonly="this.status === 'Vervangen'" required></v-text-field>
        </v-col>
      </v-row>
      <v-row v-if="this.status === 'Actief'" class="px-5 justify-center mx-auto">
        <v-col cols="12" sm="3" md="3">
          <v-btn class="mx-5 bg-secondary text-primary" @click="save_edit_eenmalig">Eenmalig aanpassen</v-btn>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-btn class="mx-5 bg-primary text-secondary"  @click="save_edit_permanent" block>Permanent aanpassen</v-btn>
        </v-col>
      </v-row>
      <v-row v-if="this.status === 'Eenmalig'" class="px-5 justify-center mx-auto">
        <v-col cols="12" sm="3" md="3">
          <v-btn class="mx-5 bg-primary text-secondary" @click="save_edit_eenmalig">Aanpassing opslaan</v-btn>
        </v-col>
      </v-row>
      <div v-if="this.status === 'Vervangen'" class="px-3 text-caption">Om deze template aan te passen moeten eerst de eenmalige aanpassingen ongedaan worden.</div>
    </v-form>
  </v-card>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import StudentTemplateService from "@/api/services/StudentTemplateService";
import UserService from "@/api/services/UserService";
import router from "@/router";
import {check_errors, get_errors} from "@/error_handling";

export default {
  name: "DagplanningEditView",
  data: () => ({
    template_id: 0,
    dag_id: 0,
    ronde_id: 0,
    day: null,
    status: '',
    start_hour: "",
    end_hour: "",
    students: [],
    all_students: [],
    location: null,
    errors: null,
    state_mapping: {
      "A": "Actief",
      "E": "Eenmalig",
      "V": "Vervangen",
      "I": "Inactief"
    }
  }),
  async mounted() {
    this.template_id = this.$route.params.template_id
    this.dag_id = this.$route.params.dag_id
    this.ronde_id = this.$route.params.ronde_id

    // get the dagplanning
    const dagplanning = await RequestHandler.handle(StudentTemplateService.getDagPlanning(this.template_id, this.dag_id), {
        id: "getDagPlanningError",
        style: "SNACKBAR"
    }).then(res => res).catch(() => null);

    this.day = dagplanning.time.day
    this.start_hour = dagplanning.time.start_hour
    this.end_hour = dagplanning.time.end_hour
    this.students = dagplanning.students.map(student => student.id)

    // get the status of template
    const template = await RequestHandler.handle(StudentTemplateService.getStudentTemplate(this.template_id), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => null);
    this.status = this.state_mapping[template.status]
    this.location = template.location

    // get all users
    this.all_students = await RequestHandler.handle(UserService.getUsers(), {
      id: 'getUsersError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

  },
  methods: {
    check_errors,
    getTitle(item) {
      if(!Number.isInteger(item)) {
        return `${item.first_name} ${item.last_name}`
      }
    },
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
    async copy_taken(new_id) {
      this.template_id = new_id
      return await router.push({name: 'ronde_dagplanningen', params: {template_id: this.template_id, ronde_id: this.ronde_id}})
    },
    async save_edit_permanent() {

      const body = {
        students: this.students,
        start_hour: this.start_hour,
        end_hour: this.end_hour
      }

      StudentTemplateService.editDagPlanning(this.template_id, this.dag_id, body)
        .then(async response => {
          if (response["new_id"] !== undefined) {
            await this.copy_taken(response["new_id"], response["new_dag_id"])
          } else {
            await this.copy_taken(this.template_id, response["new_dag_id"])
          }
        }).catch(async (error) => {this.errors = await get_errors(error)});

    },
    async save_edit_eenmalig() {

      const body = {
        students: this.students,
        start_hour: this.start_hour,
        end_hour: this.end_hour
      }

      StudentTemplateService.editDagPlanningEenmalig(this.template_id, this.dag_id, body)
        .then(async response => {
          if (response["new_id"] !== undefined) {
            await this.copy_taken(response["new_id"])
          } else {
            await this.copy_taken(this.template_id)
          }
        }).catch(async (error) => {this.errors = await get_errors(error)});
    }
  }
}
</script>

<style scoped>

</style>
