<template>
  <RoundListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Gebouwen" />
</template>

<script>
import RoundListPage from '@/components/admin/RoundListPage'
import ListPage from '@/components/admin/ListPage'
import ListBuildings from '@/components/admin/ListBuildings'
export default {
  name: 'RoundList',
  components: {ListPage, RoundListPage },
  data () {
    return {
      childComponent: ListBuildings,
      elements: [
        {
          title: 'Ronde 1',
          buildings: [
            { gebouw: 'Gebouw A', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar' },
            { gebouw: 'Gebouw B', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Update nodig' }
          ]
        },
        {
          title: 'Ronde 2',
          buildings: [
            { gebouw: 'Gebouw A', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar' },
            { gebouw: 'Gebouw B', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Update nodig' },
            { gebouw: 'Gebouw C', adres: 'Zwijnaarde straat 40, 9052 Gent', status: 'Klaar' }
          ]
        },
      ]
    }
  }
}
</script>

<style scoped>

</style>
