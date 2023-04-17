<template>
  <v-container>
    <h1 v-if="!edit">Maak nieuwe Syndicus aan</h1>
    <h1 v-else>Syndicus aanpassen</h1>
  </v-container>
  <v-container>
    <v-form>
      <label class="black-text">Syndicus</label>
      <v-autocomplete
        clearable
        :items="this.allUsers"
        :item-title="item => `${item.first_name}  ${item.last_name}`"
        :item-value="item => item"
        v-model="syndicus.syndicus"
      >
        <template v-slot:no-data>
          <div class="px-4">Er zijn geen nieuwe gebruikers.</div>
        </template>
      </v-autocomplete>
      <label class="black-text">Locatie</label>
      <v-autocomplete
        clearable
        outlined
        :items="this.allLocations"
        item-title="name"
        item-value="id"
        v-model="syndicus.location"
      ></v-autocomplete>
      <label class="black-text">Buildings</label>
      <v-autocomplete
        clearable
        outlined
        :items="this.allBuildings"
        item-title="name"
        item-value="id"
        v-model="syndicus.buildings"
        multiple
      >
        <template v-slot:no-data>
          <div class="px-4">Er zijn geen gebouwen.</div>
        </template>
      </v-autocomplete>
    </v-form>
    <normal-button v-if="!edit" text="Voeg syndicus toe" :parent-function="addSyndicus"/>
    <normal-button v-else text="Pas syndicus aan" :parent-function="editSyndicus"/>
  </v-container>

</template>

<script>

/**
 * CreateEditSyndicus component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * edit: Boolean als je een syndicus wilt bewerken of aanmaken
 */

import NormalButton from "@/components/NormalButton.vue";
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";
import BuildingService from "@/api/services/BuildingService";
import LocationService from "@/api/services/LocationService";

export default {
  name: 'CreateEditSyndicus',
  components: {NormalButton},
  props: {
    edit: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      allUsers: [],
      allLocations: [],
      allBuildings: [],
      syndicus: {
        syndicus: null,
        location: '',
        buildings: []
      }
    }
  },
  methods: {
    addSyndicus() {
      // TODO syndicus toevoegen aan de backend + error handling + terug naar de vorige pagina
      console.log(this.syndicus)
    },
    editSyndicus() {
      // TODO syndicus aanpassen in de backend + error handling + terug naar de vorige pagina
      console.log(this.syndicus)
    }
  },
  mounted() {
    // TODO als edit true is, dan de syndicus ophalen uit de backend en de data in de velden zetten
    if (this.edit) {
      console.log('edit') // TODO
    }
    RequestHandler.handle(UserService.getUsers(), {
      id: 'getAllUsersError',
      style: 'SNACKBAR',
      customMessages: [
        {
          code: '500',
          message: 'Kon alle gebruikers niet ophalen.',
          description: 'Kon gebruikers niet ophalen.'
        }
      ]
    }).then(users => {
      this.allUsers = users.filter(x => x.role === 'AA')
    })
    RequestHandler.handle(LocationService.getLocations(), {
      id: 'getLocationsError',
      style: 'SNACKBAR',
      customMessages: [
        {
          code: '500',
          message: 'Kon de locaties niet ophalen.',
          description: 'Kon de locaties niet ophalen.'
        }
      ]
    }).then(locations => {
      this.allLocations = locations
    })
    RequestHandler.handle(BuildingService.getAllBuildings(), {
      id: 'getBuildingsError',
      style: 'SNACKBAR',
      customMessages: [
        {
          code: '500',
          message: 'Kon de gebouwen niet ophalen.',
          description: 'Kon de gebouwen niet ophalen.'
        }
      ]
    }).then(buildings => {
      this.allBuildings = buildings
    })
  }
}
</script>

<style scoped>

</style>
