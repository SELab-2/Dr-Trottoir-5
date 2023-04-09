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
        item-title="name"
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
      allLocations :[],
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
    }
  },
  mounted() {

    // TODO als edit true is, dan de syndicus ophalen uit de backend en de data in de velden zetten
    if (this.props.edit) {
      console.log('edit') // TODO
    }
    // TODO dummy data aanpassen door backend data te gebruiken
    this.allUsers = [
        {id: 1, name: 'John Doe'},
        {id: 2, name: 'Jane Smith'},
        {id: 3, name: 'Bob Johnson'},
      ]
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
