<template>
  <ListPage :add-function="addBuilding" :child-component="childComponent" :elements="elements" title="Gebouwen" :head-component="headComponent" :keys="keys" :map-keys="mapKeys"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import BuildingCard from '@/components/admin/BuildingCard'
import BuildingHeader from '@/components/admin/BuildingHeader'
import {RequestHandler} from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";
import router from "@/router";
export default {
  name: 'BuildingList',
  components: { ListPage },
  data () {
    return {
      childComponent: BuildingCard,
      elements: [],
      headComponent: BuildingHeader,
      keys: ['name', 'adres', 'manual'],
      mapKeys: {
        'name': 'naam',
        'adres': 'adres',
        'manual': 'handleiding'
      }
    }
  },
  methods: {
    addBuilding : function () {
      router.push({name: 'create_building'})
    }
  },
  async beforeMount() {
    await RequestHandler.handle(BuildingService.getBuildings(), {id: 'getBuildingsError', style: 'SNACKBAR'}).then(async result => {
      this.elements = result
    })
  }
}
</script>

<style scoped>

</style>
