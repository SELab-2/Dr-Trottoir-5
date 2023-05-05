<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Maak een nieuwe template aan</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-text-field v-model='name' :error-messages="check_errors(this.errors, 'name')" label='Naam' required></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-checkbox label="Even" :error-messages="check_errors(this.errors, 'even')" v-model="even"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-select
            label="Locatie"
            :items="locations"
            item-title="name"
            item-value="id"
            v-model="location"
            :error-messages="check_errors(this.errors, 'location')"
          ></v-select>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='start_hour' :error-messages="check_errors(this.errors, 'start_hour')" label='Standaard Startuur' required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='end_hour' :error-messages="check_errors(this.errors, 'end_hour')" label='Standaard Einduur' required></v-text-field>
        </v-col>
      </v-row>
      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" sm="3" md="3">
          <v-btn @click="create()" class="overflow-hidden">Aanmaken</v-btn>
        </v-col>

      </v-row>
    </v-form>
  </v-card>
</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import NormalButton from '@/components/NormalButton.vue';
import StudentTemplateService from "@/api/services/StudentTemplateService";
import router from "@/router";
import {check_errors, get_errors} from "@/error_handling";

export default {
  name: "StudentTemplateAddView",
  components: {
    NormalButton
  },
  data: () => ({
    name: '',
    even: true,
    location: null,
    start_hour: "",
    end_hour: "",
    locations: [],
    errors: null
  }),
  async mounted() {
    // get all possible locations
    this.locations = await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);
  },
  methods: {
    check_errors,
    async create() {
      const body = {
        name: this.name,
        even: this.even,
        start_hour: this.start_hour,
        end_hour: this.end_hour,
        location: this.location
      }

      StudentTemplateService.addStudentTemplate(body)
        .then(response => router.push({name: 'studenttemplates', params: {id: response["new_id"]}}))
        .catch(async (error) => this.errors = await get_errors(error));
    }
  }
}
</script>

<style scoped>

</style>
