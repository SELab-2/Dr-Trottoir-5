<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Maak een nieuwe template aan</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-text-field v-model='name' label='Naam' :error-messages="check_errors(this.errors, 'name')" required></v-text-field>
        </v-col>
        <v-col cols="12" md="6" sm="6">
          <v-checkbox v-model="even" :error-messages="check_errors(this.errors, 'even')" label="Even"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="location"
            :error-messages="check_errors(this.errors, 'location')"
            :items="locations"
            item-title="name"
            item-value="id"
            label="Locatie"
          ></v-select>
        </v-col>
      </v-row>
      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn data-test="create" class="overflow-hidden" @click="create()">Aanmaken</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import {check_errors, get_errors} from "@/error_handling";

export default {
  name: "TrashContainerTemplateCreateView",
  data: () => ({
    name: '',
    even: true,
    location: null,
    errors: null,
    locations: []
  }),

  async beforeMount() {
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
        location: this.location
      }
      TrashTemplateService.newTrashTemplate(body)
        .then(async () => {await router.push({name: 'trashtemplates'})})
        .catch(async (error) => {this.errors = await get_errors(error)})
    }
  }
}
</script>
