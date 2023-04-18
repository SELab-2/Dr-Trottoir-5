<template>
  <RoundListPage :add-function="addMethod" :child-component="childComponent" :elements="elements" title="Rondes" :keys="keys" />
</template>

<script>
import RoundListPage from '@/components/admin/RoundListPage'
import ListPage from '@/components/admin/ListPage'
import ListBuildings from '@/components/admin/ListBuildings'
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";
import RoundService from "@/api/services/RoundService";
import BuildingService from "@/api/services/BuildingService";
import router from "@/router";
export default {
  name: 'RoundList',
  components: {ListPage, RoundListPage },
  data () {
    return {
      childComponent: ListBuildings,
      elements: [],
      keys: ['roundName', 'name', 'adres', 'manual']
    }
  },
  methods: {
    addMethod: function () {
      router.push({ path: '/create_round'});
    }
  },
  async beforeMount () {
    await RequestHandler.handle(RoundService.getRounds(), {id: 'getRounds', style: 'SNACKBAR'})
      .then(async result => {
        this.elements = result
        for (const el of this.elements) {
          for (let building of el.buildings) {
            await RequestHandler.handle(BuildingService.getBuildingById(building)).then(async resultBuilding => building = resultBuilding)
          }
        }
    })
  }
}
</script>

<style scoped>

</style>
