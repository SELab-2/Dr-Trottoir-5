<template>
  <AccountInformation :get_data="set_data" :save_data="save_data"></AccountInformation>
</template>

<script>
import AccountInformation from "@/components/AccountInformation";
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";

export default {
  name: 'AccountView',
  components: {AccountInformation},
  methods: {
    async set_data() {
      let result = {}
      await RequestHandler.handle(UserService.get(), {
        id: "getUserError",
        style: "SNACKBAR",
        customMessages: [{
          code: '500',
          message: 'Kon user informatie niet ophalen',
          description: 'Kon user informatie niet ophalen'
        }]
      }).then(data => {
        result.first_name = data.first_name
        result.last_name = data.last_name
        result.email = data.email
        result.phone_nr = data.phone_nr
        result.role = data.role
        result.rondes = []
      });
      return result
    },
    save_data(data) {
      RequestHandler.handle(UserService.update({
        first_name: data.first_name,
        last_name: data.last_name,
        email: data.email,
        phone_nr: data.phone_nr
      }), {
        id: "patchUserError",
        style: "SNACKBAR",
        customMessages: [
          {
            code: '500',
            message: 'Kon informatie van de user niet aanpassen',
            description: 'Kon informatie van de user niet aanpassen'
          }
        ]
      })
    }
  }
}
</script>
