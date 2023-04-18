<template>
  <AccountInformation :not_admin="false" :get_data="get_data" :save_data="update"
                      :delete_current="delete_user"></AccountInformation>
</template>

<script>
import AccountInformation from "@/components/AccountInformation";
import UserService from "@/api/services/UserService";
import {RequestHandler} from "@/api/RequestHandler";

export default {
  name: "AdminStudentChangeUser",
  components: {AccountInformation},
  props: {id: String},
  methods: {
    async get_data() {
      return RequestHandler.handle(UserService.getUserById(Number(this.id)), {
        id: 'getUserInfoByIdError',
        style: 'SNACKBAR',
        customMessages: [{
          code: '500',
          message: 'Kon data van gebruiker niet ophalen',
          description: 'Kon data van gebruiker niet ophalen'
        }]
      });
    },
    update(data) {
      // TODO Use role view from other branch
      RequestHandler.handle(UserService.updateUserById(Number(this.id), {
        role: data.role,
      }), {
        id: 'updateUserRoleError',
        style: 'SNACKBAR',
        customMessages: [{
          code: '500',
          message: 'Kon rol van gebruiker niet aanpassen',
          description: 'Kon rol van gebruiker niet aanpassen'
        }]
      })
    },
    delete_user() {
      // TODO redirect to list of students
      RequestHandler.handle(UserService.deleteUserById(Number(this.id)), {
        id: 'deleteUserError',
        style: 'SNACKBAR',
        customMessages: [{
          code: '500',
          message: 'Kon gebruiker niet verwijderen',
          description: 'Kon gebruiker niet verwijderen'
        }]
      })
    }
  }
}
</script>

<style scoped>

</style>
