<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Syndicusen" :head-component="headComponent" />
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import SyndicusCard from '@/components/admin/SyndicusCard'
import PersonHeader from '@/components/admin/PersonHeader'

export default {
  name: 'SyndicusList',
  components: { ListPage },
  data () {
    return {
      childComponent: SyndicusCard,
      elements: [
        { firstName: 'Baas A', secondName: 'Van Hengouwen', mobileNumber: '0498636925', location: 'Gent', email: 'baasgebouwA@gmail.com', buildings: 'Gebouw A' },
        { firstName: 'Baas B', secondName: 'Van Den Berge', mobileNumber: '0498626925', location: 'Gent', email: 'baasgebouwB@gmail.com', buildings: 'Gebouw B' },
        { firstName: 'Baas C', secondName: 'Van Dorpe', mobileNumber: '0498638925', location: 'Gent', email: 'baasgebouwC@gmail.com', buildings: 'Gebouw C' }
      ],
      headComponent: PersonHeader
    }
  },
  beforeMount () {
    this.headComponent.props.student = false
  }
}
</script>

<style scoped>

</style>
