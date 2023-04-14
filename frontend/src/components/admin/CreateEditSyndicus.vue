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
        item-value="id"
        v-model="syndicus.id"
      ></v-autocomplete>
      <label class="black-text">Locatie</label>
      <v-autocomplete
        clearable
        outlined
        :items="this.allLocations"
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
      ></v-autocomplete>
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
        id: null,
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
      console.log(this.allUsers)
    })
    this.allLocations = ['Gent', 'Brussel', 'Antwerpen']
    this.allBuildings = [
      {id: 1, name: 'Building 1'},
      {id: 2, name: 'Building 2'},
      {id: 3, name: 'Building 3'},
    ]
  }
}
</script>

<style scoped>

</style>
