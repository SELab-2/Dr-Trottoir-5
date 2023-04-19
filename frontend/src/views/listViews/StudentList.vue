<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Studenten" :head-component="headComponent" :keys="keys"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import PersonHeader from '@/components/admin/PersonHeader'
import StudentCard from '@/components/admin/StudentCard'
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";

export default {
  name: 'StudentList',
  components: { ListPage },
  data () {
    return {
      childComponent: StudentCard,
      elements: [],
      keys: ['first_name', 'last_name', 'phone_nr', 'email'],
      headComponent: PersonHeader
    }
  },
  async beforeMount() {
    (await RequestHandler.handle(UserService.getUsers(), {id: 'getUsersError', style: 'SNACKBAR'})
      .then(async result => {
        for (const user of result){
          if (user.role === 'ST'){
            this.elements.push(user)
          }
        }
      }))
  }
}
</script>

<style scoped>

</style>
