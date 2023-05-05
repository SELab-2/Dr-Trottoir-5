<template>
  <v-container>
    <V-card align="center">
      <v-card-title>
        <h4 class="text-h4">Nieuwe ronde aanmaken</h4>
      </v-card-title>
      <v-spacer />
      <v-card-text>
        <v-form ref='form' v-model='valid'>
          <v-col cols='12' sm='6' md='6'>
            <v-text-field v-model='name' :error-messages="check_errors(this.errors, 'name')" label='Naam' required variant="outlined"></v-text-field>
          </v-col>
          <v-col cols='12' sm='6' md='6'>
            <v-autocomplete
              label="Locatie" :items="locations" :error-messages="check_errors(this.errors, 'location')" item-title="name" v-model="location"
              item-value="id" variant="outlined"
            ></v-autocomplete>
          </v-col>
          <v-col cols='12' sm='6' md='6'>
            <v-autocomplete
              label="Gebouwen" :items="buildings" :error-messages="check_errors(this.errors, 'buildings')" multiple item-title="name" item-value="id"
              v-model="selected" variant="outlined"
            ></v-autocomplete>
          </v-col>
          <v-col cols="12" sm="6" md="6">
            <normal-button text="Aanmaken" v-bind:parent-function="createRound"></normal-button>
          </v-col>
        </v-form>
      </v-card-text>
    </V-card>
  </v-container>
</template>

<script>
import {defineComponent} from "vue";
import RoundService from "@/api/services/RoundService";
import {RequestHandler} from "@/api/RequestHandler";
import NormalButton from "@/components/NormalButton.vue";
import router from "@/router";
import {check_errors, get_errors} from "@/error_handling";

export default defineComponent({
  name: "CreateRoundView",
  components: {NormalButton},
  data: () => ({
    valid: true,
    locations: [],
    buildings: [],
    location: null,
    selected: null,
    name: '',
    errors: null
  }),
  async beforeCreate() {
    RequestHandler.handle(RoundService.getLocations(), {
      id: 'getLocationsError',
      style: 'none'
    }).then(l => {
      this.locations = l;
    }).catch(() => null);

    RequestHandler.handle(RoundService.getBuildings(), {
      id: 'getBuildingsError',
      style: 'none'
    }).then(b => {
      this.buildings = b;
    }).catch(() => null);
  },
  methods: {
    check_errors,
    async createRound() {
      RoundService.createRound({
        name: this.name,
        location: this.location,
        buildings: this.selected
      }).then(b => {
        this.$store.dispatch("snackbar/open", {
          message: `Ronde ${b.name} is aangemaakt.`,
          color: "success"
        });
        router.push({ name: 'rounds' });
      }).catch(async (error) => this.errors = await get_errors(error));
    }
  }
});
</script>
