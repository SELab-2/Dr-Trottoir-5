<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Studenten" :head-component="headComponent" />
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import PersonHeader from '@/components/admin/PersonHeader'
import StudentCard from '@/components/admin/StudentCard'

export default {
  name: 'StudentList',
  components: { ListPage },
  data () {
    return {
      childComponent: StudentCard,
      elements: [
        { firstName: 'Alice', secondName: 'Van Hengouwen', mobileNumber: '0498636925', location: 'Gent', email: 'avanhengouwen@gmail.com', rounds: 'zuid, station, kouter, coupure, haven, extra' },
        { firstName: 'BoB', secondName: 'Van Butsele', mobileNumber: '0498636926', location: 'Gent', email: 'bobvanbutsele@gmail.com', rounds: 'zuid, station, coupure' },
        { firstName: 'Trudy', secondName: 'Van Dorpe', mobileNumber: '0498636927', location: 'Antwerpen', email: 'trudyvdorpe@gmail.com', rounds: 'Antwerpen' }
      ],
      headComponent: PersonHeader
    }
  }
}
</script>

<style scoped>

</style>
