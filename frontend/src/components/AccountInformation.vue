<template>
  <v-row justify="center" align="center" class="pt-10">
    <h1>Account</h1>
  </v-row>
  <v-card color="white" :class="`mx-auto my-16 h-70 ${smallScreen ? 'w-100' : 'w-75'}`">
    <v-row justify="center" align="center" class="xs-flex-column">
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>Voornaam</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model="first_name" :error-messages="check_errors(this.errors, 'first_name')"
                      :readonly="!edit || !not_admin"
                      variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px"></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>Achternaam</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model="last_name" :error-messages="check_errors(this.errors, 'last_name')"
                      :readonly="!edit || !not_admin"
                      variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px"></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>E-mail</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model="email" :error-messages="check_errors(this.errors, 'email')"
                      :readonly="!edit || !not_admin"
                      variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px">
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>GSM</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model="phone_nr" :error-messages="check_errors(this.errors, 'phone_nr')"
                      :readonly="!edit || !not_admin"
                      variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px">
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center pt-10">
        <h1>Rol</h1>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center pb-10">
        <v-select variant="outlined" :items="roles" :error-messages="check_errors(this.errors, 'role')"
                  item-title="name" item-value="value" v-model="role"
                  :readonly="!edit || not_admin"
                  style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px">
        </v-select>
      </v-col>
      <div v-if="can_edit">
        <v-col v-if="!edit" class="d-flex justify-center align-center pb-10" cols="12" sm="12" md="12" lg="12">
          <normal-button data-test="edit-button" text='Pas aan' :parent-function='() => {this.edit = !this.edit}'/>
        </v-col>
        <v-col v-else class="d-flex justify-center align-center pb-10" cols="12" sm="12" md="12" lg="12">
          <normal-button data-test="save-button" text='Aanpassingen opslaan' :parent-function="save"/>
          <normal-button data-test="cancel-button" text='Annuleer' :parent-function="cancel_save" class="ml-2"/>
        </v-col>
      </div>
      <v-col v-if="!not_admin && can_edit" class="d-flex justify-center align-center pb-10" cols="12" sm="12"
             md="12" lg="12">
        <v-btn data-test="delete-button" @click="$refs.confirm.open()" icon="mdi-delete"></v-btn>
      </v-col>
    </v-row>
    <ConfirmDialog text="Bent u zeker dat u deze gebruiker wilt verwijderen?" :confirm_function="delete_current"
                   ref="confirm"></ConfirmDialog>
  </v-card>
</template>

<script>
import NormalButton from '@/components/NormalButton'
import ConfirmDialog from '@/components/util/ConfirmDialog'
import UserService from "@/api/services/UserService";
import {check_errors, get_errors} from "@/error_handling";
import AuthService from "@/api/services/AuthService";
import {RequestHandler} from "@/api/RequestHandler";

export default {
  name: 'AccountInformation',
  components: {ConfirmDialog, NormalButton},
  props: {
    not_admin: {type: Boolean, default: true},
    can_edit_permission: {type: Boolean, default: true}
  },
  data: () => ({
    user: null,
    first_name: '',
    last_name: '',
    email: '',
    phone_nr: '',
    role: '',
    rondes: [],
    roles: [
      {name: 'Aanvrager', value: 'AA'}, {name: 'Student', value: 'ST'},
      {name: 'Superstudent', value: 'SU'}, {name: 'Admin', value: 'AD'},
      {name: 'Syndicus', value: 'SY'}
    ],
    edit: false,
    smallScreen: false,
    can_edit: true,
    errors: null
  }),
  async beforeMount() {
    let id = this.$route.params.id
    const currentUser = await this.$store.getters['session/currentUser']
    this.user = currentUser

    if (id !== undefined) {
      await UserService.getUserById(id)
        .then(async data => {
          this.user = data
        })
        .catch(async (error) => {
          this.errors = await get_errors(error)
        });
    }

    this.first_name = this.user.first_name
    this.last_name = this.user.last_name
    this.email = this.user.email
    this.phone_nr = this.user.phone_nr
    this.role = this.user.role

    this.can_edit = this.can_edit_permission
    if (!this.not_admin) {
      const currentUserRole = currentUser.role
      if (currentUserRole === 'SU') {
        if (this.role === 'AD') {
          this.can_edit = false
        } else {
          this.roles = [{name: 'Aanvrager', value: 'AA'}, {name: 'Student', value: 'ST'},
            {name: 'Superstudent', value: 'SU'}]
        }
      }
    }
  },
  beforeUnmount() {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.onResize, {passive: true})
    }
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
  }
  ,
  methods: {
    check_errors,
    async cancel_save() {
      this.edit = !this.edit

      this.first_name = this.user.first_name
      this.last_name = this.user.last_name
      this.email = this.user.email
      this.phone_nr = this.user.phone_nr
      this.role = this.user.role
    },
    async save() {
      let id = this.$route.params.id

      let handle
      if (id !== undefined) {
        handle = RequestHandler.handle(AuthService.updateRoleOfUser({
          role: this.role,
          email: this.email
        }), {
          id: 'updateRoleOfUserAccountInformation',
          style: 'SNACKBAR',
        }).then()
      } else {
        handle = RequestHandler.handle(UserService.patchLoggedInUser({
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          role: this.role,
          phone_nr: this.phone_nr
        }), {
          id: 'patchLoggedInUserAccountInformation',
          style: 'SNACKBAR'
        })
      }
      handle.then(() => {
        this.edit = !this.edit
        this.email = this.email.toLowerCase()
        this.errors = null
      }).catch(async (error) => {
        this.errors = await get_errors(error)
      })
    },
    delete_current() {
      UserService.deleteUserById(this.id)
      this.$router.push({name: 'admin_user_register'})
    },
    onResize() {
      this.smallScreen = window.innerWidth < 500
    }
  }
}
</script>
