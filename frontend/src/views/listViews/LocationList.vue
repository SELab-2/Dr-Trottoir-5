<template>
  <ListPage :add-function="addLocation" :child-component="childComponent"
            :elements="elements" title="Locaties"
            :head-component="headComponent" :keys="keys" :map-keys="mapKeys"></ListPage>
</template>

<script>
import ListPage from "@/components/admin/ListPage";
import LocationCard from "@/components/admin/LocationCard";
import LocationHeader from "@/components/admin/LocationHeader";
import router from "@/router";
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";

export default {
  name: "LocationList",
  components: {ListPage},
  data() {
    return {
      childComponent: LocationCard,
      elements: [],
      headComponent: LocationHeader,
      keys: ['name'],
      mapKeys: {'name': 'naam'}
    }
  },
  methods: {
    addLocation() {
      router.push({name: 'create_location'})
    },
    async getLocations() {
      this.elements = await RequestHandler.handle(LocationService.getLocations(), {
        id: 'locationListGetLocations',
        style: 'SNACKBAR'
      })
    }
  },
  beforeMount() {
    this.getLocations()
  }
}
</script>
