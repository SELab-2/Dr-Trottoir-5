<template>
  <v-container>
    <V-card align="center">
      <v-card-title>
        <h4 class="text-h4" v-if="id === undefined">Nieuwe ronde aanmaken</h4>
        <h4 class="text-h4" v-if="id !== undefined">Ronde bewerken</h4>
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
              label="Gebouwen" :items="buildings.filter(building => building.location === this.location)" :error-messages="check_errors(this.errors, 'buildings')" multiple item-title="name" item-value="id"
              v-model="selected" variant="outlined"
            ></v-autocomplete>
          </v-col>
          <v-col cols="12" sm="6" md="6">
            <normal-button v-if="id === undefined" text="Aanmaken" :parent-function="createRound"></normal-button>
            <normal-button v-if="id !== undefined" text="Opslaan" :parent-function="createRound"></normal-button>
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
  props: {id: String},
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
    await RequestHandler.handle(RoundService.getLocations(), {
      id: 'getLocationsError',
      style: 'none'
    }).then(l => {
      this.locations = l;
    }).catch(() => null);

    await RequestHandler.handle(RoundService.getBuildings(), {
      id: 'getBuildingsError',
      style: 'none'
    }).then(async b => {
      this.buildings = b;
    }).catch(() => null);

    if (this.id !== undefined) {
      RequestHandler.handle(RoundService.getRoundById(Number(this.id)), {
        id: 'getRoundError',
        style: 'SNACKBAR'
      }).then(r => {
        this.name = r.name;
        this.location = r.location;
        this.selected = r.buildings;
      }).catch(() => null);
    }
  },
  methods: {
    check_errors,
    async createRound() {
      if (this.id === undefined) {
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
        }).catch(async (error) => {this.errors = await get_errors(error)});
      } else {
        RoundService.updateRoundById(Number(this.id), {
          name: this.name,
          location: this.location,
          buildings: this.selected
        }).then(() => {
          this.$store.dispatch("snackbar/open", {
            message: `Ronde ${this.name} is aangepast.`,
            color: "success"
          });
          router.push({ name: 'rounds' });
        }).catch(async (error) => {this.errors = await get_errors(error)});
      }
    }
  }
});
</script>
