<template>
 <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-5">
        <v-col cols="12" sm="6" md="6">
          <v-select
            label="Weekdag"
            :items="weekdagen"
            item-title="day"
            item-value="id"
            v-model="day"
          ></v-select>
        </v-col>
        <v-btn :to="{name: 'ronde_dagplanningen', params: {template_id: this.template_id, ronde_id: this.ronde_id}}" variant="outlined" >
            Terug
        </v-btn>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-select
            label="Studenten"
            :items="all_students"
            item-title="first_name"
            item-value="id"
            multiple
            chips
            v-model="students"
          ></v-select>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='start_hour' label='Startuur' required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='end_hour' label='Einduur' required></v-text-field>
        </v-col>
      </v-row>
      <v-row class="px-5 justify-center mx-auto">
        <v-col cols="12" sm="3" md="3">
          <v-btn class="mx-5 bg-primary text-secondary" @click="make_new_dagplanning">Aanmaken</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script>
import { RequestHandler } from '@/api/RequestHandler'
import StudentTemplateService from '@/api/services/StudentTemplateService'
import UserService from '@/api/services/UserService'
import router from '@/router'

export default {
  name: 'DagplanningAddView',
  data: () => ({
    template_id: 0,
    ronde_id: 0,
    day: 'MO',
    start_hour: '',
    end_hour: '',
    students: [],
    all_students: [],
    weekdagen: [
      { id: 'MO', day: 'Maandag' },
      { id: 'TU', day: 'Dinsdag' },
      { id: 'WE', day: 'Woensdag' },
      { id: 'TH', day: 'Donderdag' },
      { id: 'FR', day: 'Vrijdag' },
      { id: 'SA', day: 'Zaterdag' },
      { id: 'SU', day: 'Zondag' }
    ]
  }),
  async mounted () {
    this.template_id = this.$route.params.template_id
    this.ronde_id = this.$route.params.ronde_id

    // get the status of template
    const template = await RequestHandler.handle(StudentTemplateService.getStudentTemplate(this.template_id), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => {})

    this.start_hour = template.start_hour
    this.end_hour = template.end_hour

    // get all users
    this.all_students = await RequestHandler.handle(UserService.getUsers(), {
      id: 'getUsersError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => [])
  },
  methods: {
    async make_new_dagplanning () {
      const body = {
        day: this.day,
        students: this.students,
        start_hour: this.start_hour,
        end_hour: this.end_hour
      }
      const response = RequestHandler.handle(StudentTemplateService.addDagPlanningen(this.template_id, this.ronde_id, body), {
        id: 'addDagplanningError',
        style: 'SNACKBAR'
      }).then(res => res).catch(() => {})

      if (response.new_id !== undefined) {
        this.template_id = response.new_id
      }
      return await router.push({ name: 'ronde_dagplanningen', params: { template_id: this.template_id, ronde_id: this.ronde_id } })
    }
  }
}
</script>

<style scoped>

</style>
