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
      <label class="black-text">Gebouwen</label>
      <v-autocomplete
        clearable
        outlined
        :items="this.allBuildings.filter(building => building.location === this.syndicus.location)"
        item-title="name"
        item-value="id"
        v-model="syndicus.buildings"
        multiple
      >
        <template v-slot:no-data>
          <div class="px-4">Er zijn geen gebouwen voor gegeven locatie.</div>
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
import AuthService from "@/api/services/AuthService";

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
        id: '',
        location: '',
        buildings: []
      }
    }
  },
  methods: {
    async addSyndicus() {
      if (this.syndicus.id === '' || this.syndicus.location === '' || this.buildings.length === 0) {
        this.$store.dispatch("snackbar/open", {
          message: "Een van de verplichte velden is leeg.",
          color: "error"
        })
        return;
      }
      for (let building_id of this.syndicus.buildings) {
        let syndicus = this.allBuildings.filter(building => building.id === building_id)[0].syndicus
        syndicus.push(this.syndicus.id)
        await RequestHandler.handle(BuildingService.updateBuildingById(Number(building_id), {
          'syndicus': syndicus
        }), {
          id: 'addSyndicusToBuilding',
          style: 'SNACKBAR',
          customMessages: [
            {
              code: '500',
              message: 'Kon de syndicus niet toevoegen aan het gebouw.',
              description: 'Kon de syndicus niet toevoegen aan het gebouw.'
            }
          ]
        })
      }
      await RequestHandler.handle(AuthService.updateRoleOfUser({
        email: this.allUsers.filter(user => user.id === this.syndicus.id)[0].email,
        role: 'SY'
      }), {
        id: 'addSyndicusRole',
        style: 'SNACKBAR',
        customMessages: [
          {
            code: '500',
            message: 'Kon de role van de user niet aanpassen.',
            description: 'Kon de role van de user niet aanpassen.'
          }
        ]
      })
      console.log(this.$router.back())
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
      this.allUsers = users.filter(x => x.role === 'AA').map(user => {
        user['name'] = `${user.first_name} ${user.last_name}`
        return user
      })
      console.log(this.allUsers)
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
