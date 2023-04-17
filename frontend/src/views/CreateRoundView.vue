<template>
  <v-container>
    <V-card align="center">
      <v-card-title>
        <h2>Nieuwe ronde aanmaken</h2>
      </v-card-title>
      <v-spacer />
      <v-card-text>
        <v-form ref='form' v-model='valid'>
          <v-col cols='12' sm='6' md='6'>
            <v-text-field v-model='name' :rules='[rules.required]' label='Naam' required></v-text-field>
          </v-col>
          <v-col cols='12' sm='6' md='6'>
            <v-autocomplete
              label="Locatie" :items="locations" :rules="[rules.required]" item-title="name" v-model="location"
              item-value="id"
            ></v-autocomplete>
          </v-col>
          <v-col cols='12' sm='6' md='6'>
            <v-autocomplete
              label="Gebouwen" :items="buildings" :rules="[rules.required]" multiple item-title="name" item-value="id"
              v-model="selected"
            ></v-autocomplete>
          </v-col>
          <v-col cols="12" sm="6" md="6">
            <normal-button text="Aanmaken" v-bind:parent-function="validate"></normal-button>
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
    rules: {
      required: value => !!value || 'Dit veld is verplicht.'
    }
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
    async createRound() {
      RequestHandler.handle(RoundService.createRound({
        name: this.name,
        location: this.location,
        buildings: this.selected
      }), {
        id: 'createRoundError',
        style: 'none'
      }).then(b => {
        this.$store.dispatch("snackbar/open", {
          message: `Ronde ${b.name} is aangemaakt.`,
          color: "success"
        });
        router.push({ path: '/' }); // TODO: change to list of rounds
      }).catch(() => null);
    },
    async validate () {
      const { valid } = await this.$refs.form.validate();

      if (valid) {
        await this.createRound();
      }
    }
  }
});
</script>
