<template>
  <v-row class="justify-space-around align-center py-5">
    <div class="text-h4 text-md-h2 text-lg-h1">
      Template
    </div>
    <v-btn :to="'/studenttemplates/'" variant="outlined" >
        Terug
    </v-btn>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-text-field v-model='name' label='Naam' :readonly="!edit" required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='status' label='Status' readonly required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-checkbox label="Even" v-model="even" :readonly="!edit"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-select
            :readonly="!edit"
            label="Locatie"
            :items="locations"
            item-title="name"
            item-value="id"
            v-model="location"
          ></v-select>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='start_hour' label='Standaard Startuur' :readonly="!edit" required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='end_hour' label='Standaard Einduur' :readonly="!edit" required></v-text-field>
        </v-col>
      </v-row>
      <v-row v-if="this.status !== 'Vervangen'" class="px-5 justify-center mx-auto">
        <v-col v-if="!edit" class="d-flex justify-center ml-auto mx-auto" cols="12" sm="3" md="3">
          <NormalButton text="Pas aan" v-bind:parent-function="() => {edit = !edit}" block></NormalButton>
        </v-col>
        <v-col v-if="edit" class="d-flex justify-center ml-auto mx-auto" cols="12" sm="3" md="3">
          <NormalButton class="mx-5" text="Annuleer" v-bind:parent-function="() => {edit = !edit}" block></NormalButton>
          <NormalButton text="Sla op" v-bind:parent-function="save_edit" block></NormalButton>
        </v-col>
      </v-row>
      <div v-if="this.status === 'Vervangen'" class="px-3 text-caption">Om deze template aan te passen moeten eerst de eenmalige aanpassingen ongedaan worden.</div>
    </v-form>
  </v-card>
  <div  v-if="this.status !== 'Vervangen'" >
    <v-row class="justify-center">
      <div class="text-h3">
          Rondes
      </div>
    </v-row>
    <v-row class="px-5  justify-center align-end mx-auto">
      <v-col class="d-flex" cols='12' sm='6' md='6'>
        <v-autocomplete
          label="Rondes"
          :items="all_rondes"
          item-title="name"
          item-value="id"
          v-model="add_id"
        ></v-autocomplete>
        <v-btn @click="add_round()" class="mx-5">Voeg nieuwe ronde toe</v-btn>
      </v-col>
    </v-row>
  </div>
  <TemplateRondeCard @copy="(new_id) => copy_taken(new_id)" @round_removed="() => remove_ronde(ronde.id)" v-for="ronde in rondes" :data="{
      template_id: this.template_id,
      ronde_id: ronde.id,
      status: this.status,
      name: ronde.name,
      location: ronde.location.name
    }"></TemplateRondeCard>
</template>

<script>
import NormalButton from '@/components/NormalButton.vue';
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import StudentTemplateService from "@/api/services/StudentTemplateService";
import TemplateRondeCard from "@/components/admin/student_template/TemplateRondeCard.vue";
import RoundService from "@/api/services/RoundService";
import router from "@/router";

export default {
  name: "StudentTemplateEditView",
  components: {
    NormalButton,
    TemplateRondeCard
  },
  data: () => ({
    edit: false,
    template: null,
    template_id: 0,
    name: '',
    status: '',
    even: true,
    location: 0,
    start_hour: "",
    end_hour: "",
    locations: [],
    rondes: [],
    all_rondes: [],
    add_id: null,
    state_mapping: {
      "A": "Actief",
      "E": "Eenmalig",
      "V": "Vervangen",
      "I": "Inactief"
    }
  }),
  async mounted() {
    this.template_id = this.$route.params.id

    // get the template
    this.template = await RequestHandler.handle(StudentTemplateService.getStudentTemplate(this.template_id), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => null);

    // get all possible locations
    this.locations = await RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

    // get all rounds
    this.all_rondes = await RequestHandler.handle(RoundService.getRounds(), {
      id: 'getRondesError',
      style: 'SNACKBAR'
    }).then(result => result).catch(() => []);

    this.name = this.template.name
    this.status = this.state_mapping[this.template.status]
    this.even = this.template.even
    this.location = this.template.location
    this.start_hour = this.template.start_hour
    this.end_hour = this.template.end_hour
    this.rondes = this.template.rondes
  },
  methods: {
    async copy_taken(new_id) {
      this.template_id = new_id
      return await router.replace({path: `/studenttemplates/${new_id}`})
    },
    async save_edit() {
      this.edit = false
      const body = {
        name: this.name,
        even: this.even,
        start_hour: this.start_hour,
        end_hour: this.end_hour,
        location: this.location.id
      }

      const response = await RequestHandler.handle(StudentTemplateService.updateStudentTemplate(this.template_id, body), {
          id: 'updateStudentTemplate',
          style: 'SNACKBAR'
      }).then(res => res)
      if (response["new_id"] !== undefined) {
        await this.copy_taken(response["new_id"])
      }
    },
    async add_round() {
      const body = {ronde: this.add_id}
      const response = await RequestHandler.handle(StudentTemplateService.addRound(this.template_id, body), {
          id: 'studentTemplateAddRound',
          style: 'SNACKBAR'
      })
      for (let ronde of this.all_rondes) {
        if (ronde.id === this.add_id) {
          this.rondes.push(ronde)
        }
      }
      if (response["new_id"] !== undefined) {
        await this.copy_taken(response["new_id"])
      }
    },
    remove_ronde(ronde_id) {
      let index = -1;
      for (let i = 0; i < this.rondes.length; i++) {
        if (this.rondes[i].id === ronde_id) {
          index = i
        }
      }
      if (index > -1) {
        this.rondes.splice(index, 1);
      }

    }
  }
}
</script>

<style scoped>

</style>
