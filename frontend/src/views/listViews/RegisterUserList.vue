<template>
  <ListPage :child-component="childComponent" :elements="elements" title="Registreer gebruikers" :keys="keys"
            :add-function="() => {}"></ListPage>
</template>

<script>
import ListPage from "@/components/admin/ListPage";
import StudentCard from "@/components/admin/StudentCard";
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";

export default {
  name: "RegisterUserList",
  components: {ListPage},
  data() {
    return {
      childComponent: StudentCard,
      elements: [],
      keys: ['first_name', 'last_name', 'phone_nr', 'email']
    }
  },
  async beforeMount() {
    RequestHandler.handle(UserService.getUsers(), {id: 'getUsersError', style: 'SNACKBAR'})
      .then(async result => {
        for (const user of result) {
          if (user.role === 'AA') {
            this.elements.push(user)
          }
        }
      })
  }
}
</script>

<style scoped>

</style>
