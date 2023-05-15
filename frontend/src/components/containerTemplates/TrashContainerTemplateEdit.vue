<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Pas de template aan.</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-text-field v-model='name' label='Naam' required></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-checkbox v-model="even" label="Even"></v-checkbox>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-checkbox v-model="permanent" label="Permanent"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="location"
            :items="locations"
            item-title="name"
            item-value="id"
            label="Locatie"
          />
        </v-col>
      </v-row>
      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="update()">Aanpassen</v-btn>
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

export default {
  name: "TrashContainerTemplateEditView",
  components: {},
  props: {},
  data: () => ({
    name: '',
    even: true,
    permanent: true,
    location: null,
    locations: [],
  }),
  async beforeMount() {
    // get all possible locations
    this.locations = await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

    const trashTemplate = await RequestHandler.handle(TrashTemplateService.getTrashTemplate(this.$route.params.id), {
      id: 'getTemplateEditError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => null)

    this.name = trashTemplate.name
    this.even = trashTemplate.even
    this.location = trashTemplate.location
  },
  methods: {
    async update() {
      const body = {
        name: this.name,
        even: this.even,
        location: this.location,
        permanent: this.permanent
      }
      await RequestHandler.handle(TrashTemplateService.updateTrashTemplate(this.$route.params.id, body), {
        id: 'CreateNewTrashTemplateError',
        style: 'SNACKBAR'
      }).then(result => {
        if (result['new_id'] !== null || result['new_id'] !== undefined) {
          return router.push({name: 'editTrashtemplates', params: {id: result['new_id']}})
        } else {
          return router.push({name: 'trashtemplates'})
        }
      })
    }
  }
}
</script>
