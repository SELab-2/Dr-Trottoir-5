<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Gebouwen" :head-component="headComponent" />
</template>

<script>
import ListPage from '@/components/ListPage'
import BuildingCard from '@/components/admin/BuildingCard'
import BuildingHeader from '@/components/admin/BuildingHeader'
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
  }
}
</script>

<style scoped>

</style>
