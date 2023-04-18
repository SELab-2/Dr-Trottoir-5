<template>
  <ListPage :add-function="addBuilding" :child-component="childComponent" :elements="elements" title="Gebouwen" :head-component="headComponent" key-value="name"/>
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
      headComponent: BuildingHeader
    }
  },
  methods: {
    addBuilding : function () {
      router.push({ path: '/building/create'});
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
