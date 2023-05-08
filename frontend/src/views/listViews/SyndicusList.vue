<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Syndicusen" :head-component="headComponent" :keys="keys"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import SyndicusCard from '@/components/admin/SyndicusCard'
import PersonHeader from '@/components/admin/PersonHeader'
import { RequestHandler } from '@/api/RequestHandler'
import UserService from '@/api/services/UserService'

export default {
  name: 'SyndicusList',
  components: { ListPage },
  data () {
    return {
      childComponent: SyndicusCard,
      elements: [],
      keys: ['first_name', 'last_name', 'phone_nr', 'email'],
      headComponent: PersonHeader
    }
  },
  async beforeMount () {
    this.headComponent.props.student = false
    await RequestHandler.handle(UserService.getUsers(), { id: 'getUsers', style: 'SNACKBAR' })
      .then(async result => {
        for (const user of result) {
          if (user.role === 'SY') {
            console.log(user)
            this.elements.push(user)
          }
        }
    })
  }
}
</script>

<style scoped>

</style>
