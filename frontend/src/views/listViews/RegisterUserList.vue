<template>
  <ListPage :refresh="true" :refresh_function="get_data" :child-component="childComponent" :elements="elements"
            title="Registreer gebruikers"
            :keys="keys" :map-keys="mapKeys"
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
      keys: ['first_name', 'last_name', 'phone_nr', 'email'],
      mapKeys: {
        'first_name': 'voornaam',
        'last_name': 'achternaam',
        'phone_nr': 'gsm-nummer',
        'email': 'email'
      }
    }
  },
  async beforeMount() {
    await this.get_data()
  },
  methods: {
    async get_data() {
      this.elements = await RequestHandler.handle(UserService.getUsers(), {
        id: 'RegisterUserListgetUsersError',
        style: 'SNACKBAR'
      })
        .then(async result => {
          let temp = []
          for (const user of result) {
            if (user.role === 'AA') {
              temp.push(user)
            }
          }
          return temp
        })
    }
  }
}
</script>

<style scoped>

</style>
