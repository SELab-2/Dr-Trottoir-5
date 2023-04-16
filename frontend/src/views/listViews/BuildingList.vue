<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Gebouwen" :head-component="headComponent" key-value="gebouw"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import BuildingCard from '@/components/admin/BuildingCard'
import BuildingHeader from '@/components/admin/BuildingHeader'
import {RequestHandler} from "@/api/RequestHandler";
import EmailTemplateService from "@/api/services/EmailTemplateService";
import BuildingService from "@/api/services/BuildingService";
export default {
  name: 'BuildingList',
  components: { ListPage },
  data () {
    return {
      childComponent: BuildingCard,
      elements: [
        { gebouw: 'Gebouw A', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar', efficiency: 60 },
        { gebouw: 'Gebouw B', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Update nodig', efficiency: 20 },
        { gebouw: 'Gebouw C', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar', efficiency: 90 }
      ],
      headComponent: BuildingHeader
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
