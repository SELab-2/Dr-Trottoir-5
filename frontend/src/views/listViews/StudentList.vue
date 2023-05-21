<template>
  <v-row class="pa-5">
    <v-col cols="12" sm="12" md="12" lg="12" class="d-flex align-center pl-16">
      <NormalButton text="Studenten registreren" :parent-function="goToRegister"></NormalButton>
    </v-col>
  </v-row>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Studenten" :head-component="headComponent" :keys="keys" :map-keys="mapKeys"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import PersonHeader from '@/components/admin/PersonHeader'
import StudentCard from '@/components/admin/StudentCard'
import {RequestHandler} from "@/api/RequestHandler";
import UserService from "@/api/services/UserService";
import NormalButton from "@/components/NormalButton";
import router from "@/router";

export default {
  name: 'StudentList',
  components: {NormalButton, ListPage },
  data () {
    return {
      childComponent: StudentCard,
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
  methods: {
    async goToRegister() {
      await router.push({name: 'admin_user_register'});
    }
  },
  async beforeMount() {
    (await RequestHandler.handle(UserService.getUsers(), {id: 'getUsersError', style: 'SNACKBAR'})
      .then(async result => {
        for (const user of result){
          if (user.role === 'ST' || user.role === 'SU'){
            this.elements.push(user)
          }
        }
      }))
  }
}
</script>

<style scoped>

</style>
