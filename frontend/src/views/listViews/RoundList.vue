<template>
  <RoundListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Rondes" key-value="name" />
</template>

<script>
import RoundListPage from '@/components/admin/RoundListPage'
import ListPage from '@/components/admin/ListPage'
import ListBuildings from '@/components/admin/ListBuildings'
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";
import RoundService from "@/api/services/RoundService";
export default {
  name: 'RoundList',
  components: {ListPage, RoundListPage },
  data () {
    return {
      childComponent: ListBuildings,
      elements: [
        {
          name: 'Ronde 1',
          buildings: [
            { gebouw: 'Gebouw A', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar' },
            { gebouw: 'Gebouw B', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Update nodig' }
          ]
        },
        {
          name: 'Ronde 2',
          buildings: [
            { gebouw: 'Gebouw A', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar' },
            { gebouw: 'Gebouw B', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Update nodig' },
            { gebouw: 'Gebouw C', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar' }
          ]
        },
      ]
    }
  },
  async beforeMount () {
    await RequestHandler.handle(RoundService.getRounds(), {id: 'getRounds', style: 'SNACKBAR'})
      .then(async result => {
        for (const round in result) {
          this.elements.push(round)
        }
    })
  }
}
</script>

<style scoped>

</style>
