<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Syndici" :head-component="headComponent" :keys="keys" :map-keys="mapKeys"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import SyndicusCard from '@/components/admin/SyndicusCard'
import PersonHeader from '@/components/admin/PersonHeader'
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";

export default {
  name: 'SyndicusList',
  components: { ListPage },
  data () {
    return {
      childComponent: SyndicusCard,
      elements: [],
      keys: ['first_name', 'last_name', 'phone_nr', 'email'],
      mapKeys: {
        'first_name': 'voornaam',
        'last_name': 'achternaam',
        'phone_nr': 'gsm_nummer',
        'email': 'email'
      },
      headComponent: PersonHeader
    }
  },
  async beforeMount () {
    await RequestHandler.handle(UserService.getUsers(), {id: 'getUsers', style: 'SNACKBAR'})
      .then(async result => {
        for (const user of result) {
          if (user.role === "SY"){
            this.elements.push(user)
          }
        }
    })
  }
}
</script>

<style scoped>

</style>
