<template>
  <AccountInformation :can_edit_permission="false" :not_admin="true" :get_data="get_data" :save_data="() => {}"
                      :delete_current="() => {}"></AccountInformation>
</template>

<script>
import AccountInformation from "@/components/AccountInformation";
import UserService from "@/api/services/UserService";
import {RequestHandler} from "@/api/RequestHandler";

export default {
  name: "AdminStudentInfoUser",
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
      }).catch(() => {
        this.$router.push({name: 'admin_user_register'})
      });
    },
  }
}
</script>

<style scoped>

</style>
