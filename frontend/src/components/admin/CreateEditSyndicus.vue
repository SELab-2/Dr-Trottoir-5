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
          <div class="px-4">Er zijn geen gebruikers.</div>
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
        @update:modelValue="updateBuilding"
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
    <normal-button data-test="add" v-if="!edit" text="Voeg syndicus toe" :parent-function="addSyndicus"/>
    <normal-button data-test="edit" v-else text="Pas syndicus aan" :parent-function="editSyndicus"/>
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
import router from "@/router";

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
        location: null,
        buildings: [],
        old_buildings: []
      }
    }
  },
  methods: {
    async update(building_id, syndicus) {
      /**
       * This method is the request we send to the backend. The body exists of an updated list
       * of syndicussen for a specific building.
       */
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
    },
    async addSyndicus() {
      /**
       * For adding a syndicus do we need to check if all fields are not empty. After this can
       * we send a request with an updated list. We do this for every selected building. We than change
       * the role of the user to syndicus.
       */
      if (this.syndicus.id === null || this.syndicus.location === null || this.syndicus.buildings.length === 0) {
        this.$store.dispatch("snackbar/open", {
          message: "Een of meerdere van de verplichte velden zijn leeg.",
          color: "error"
        })
        return;
      }
      for (let building_id of this.syndicus.buildings) {
        let syndicus = this.allBuildings.find(building => building.id === building_id).syndicus
        syndicus.push(this.syndicus.id)
        await this.update(building_id, syndicus)
      }
      await RequestHandler.handle(AuthService.updateRoleOfUser({
        email: this.allUsers.find(user => user.id === this.syndicus.id).email,
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
      await router.push({name: 'syndici'})
    },
    async editSyndicus() {
      /**
       * If we want to edit the buildings of a syndicus we have two options. There are buildings removed
       * or buildings been added to the syndicus. For every option do we need to update the list of syndicates of a building.
       */
      for (let building_id of this.syndicus.old_buildings) {
        if (!this.syndicus.buildings.includes(building_id)) {
          let syndicus = this.allBuildings.find(building => building.id === building_id).syndicus
          const index = syndicus.indexOf(this.syndicus.id)
          syndicus.splice(index, 1)
          await this.update(building_id, syndicus)
        }
      }
      for (let building_id of this.syndicus.buildings) {
        if (!this.syndicus.old_buildings.includes(building_id)) {
          const syndicus = this.allBuildings.find(building => building.id === building_id).syndicus
          syndicus.push(this.syndicus.id)
          await this.update(building_id, syndicus)
        }
      }
      await router.push({name: 'syndici'})
    },
    updateBuilding() {
      /**
       * Every time the location of a syndicus is changed we update the selected buildings
       * for the given syndicus.
       */
      if (this.edit) {
        const buildings = this.allBuildings.filter(building =>
          building.syndicus.includes(this.syndicus.id)).map(building => building.id)
        this.syndicus.old_buildings = buildings
        this.syndicus.buildings = buildings
      }
    }
  },
  mounted() {
    /**
     * We collect the needed data to adjust or add a syndicus.
     * We need a list of locations, a list of users that are not registered or have the role syndicus.
     * A list of all the buildings that are registered with us.
     */
    if (this.edit) {
      RequestHandler.handle(UserService.getUsers(), {
        id: 'getAllSyndicusUsersError',
        style: 'SNACKBAR',
        customMessages: [
          {
            code: '500',
            message: 'Kon alle syndicussen niet ophalen.',
            description: 'Kon syndicussen niet ophalen.'
          }
        ]
      }).then(users => {
        this.allUsers = users.filter(x => x.role === 'SY').map(user => {
          user['name'] = `${user.first_name} ${user.last_name}`
          return user
        })
      })
    } else {
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
      })
    }
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
