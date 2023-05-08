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
        <v-text-field v-model:model-value="data.first_name" :readonly="!edit" variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px"></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>Achternaam</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model:model-value="data.last_name" :readonly="!edit" variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px"></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>E-mail</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model:model-value="data.email" :readonly="!edit" variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px">
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-end justify-lg-end align-center pt-10">
        <h1>GSM</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6"
             class="d-flex justify-center justify-md-start justify-lg-start align-center">
        <v-text-field v-model:model-value="data.phone_nr" :readonly="!edit" variant="outlined"
                      style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px">
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center pt-10">
        <h1>Rol</h1>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center pb-10">
        <v-select variant="outlined" :items="roles" item-title="name" item-value="value" v-model:model-value="data.role"
                  :readonly="!edit || not_admin"
                  style="height: 40px; max-width: 350px; padding-left: 5px; padding-top: 5px">
        </v-select>
      </v-col>
      <!-- TODO Milestone 3
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center pt-10">
        <h1>Rondes</h1>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center">
        <template v-for="ronde in ['Ronde 1']" :key="ronde">
          <v-checkbox :model-value="data.rondes && ronde in data.rondes" readonly :label="ronde"></v-checkbox>
        </template>
      </v-col>
      ---->
      <div v-if="edit_permission">
        <v-col v-if="!edit" class="d-flex justify-center align-center pb-10" cols="12" sm="12" md="12" lg="12">
          <normal-button text='Pas aan' :parent-function='() => {this.edit = !this.edit}'/>
        </v-col>
        <v-col v-else class="d-flex justify-center align-center pb-10" cols="12" sm="12" md="12" lg="12">
          <normal-button text='Aanpassingen opslaan' :parent-function="save"/>
          <normal-button text='Annuleer' :parent-function="cancel_save" class="ml-2"/>
        </v-col>
      </div>
      <v-col v-if="!not_admin && edit_permission" class="d-flex justify-center align-center pb-10" cols="12" sm="12"
             md="12" lg="12">
        <v-btn @click="$refs.confirm.open()" icon="mdi-delete"></v-btn>
      </v-col>
    </v-row>
    <ConfirmDialog text="Bent u zeker dat u deze gebruiker wilt verwijderen?" :confirm_function="delete_current"
                   ref="confirm"></ConfirmDialog>
  </v-card>
</template>

<script>
import NormalButton from '@/components/NormalButton'
import ConfirmDialog from '@/components/util/ConfirmDialog'

export default {
  name: 'AccountInformation',
  components: { ConfirmDialog, NormalButton },
  props: {
    get_data: {
      type: Function,
default: () => {
      }
    },
    save_data: {
      type: Function,
default: () => {
      }
    },
    delete_current: {
      type: Function,
default: () => {

      }
    },
    not_admin: { type: Boolean, default: true },
    can_edit_permission: { type: Boolean, default: true }
  },
  data: () => {
    return {
      data: {
        type: Object,
        default: () => ({
          first_name: '',
          last_name: '',
          email: '',
          phone_nr: '',
          role: '',
          rondes: []
        })
      },
      roles: [
        { name: 'Aanvrager', value: 'AA' }, { name: 'Student', value: 'ST' },
        { name: 'Superstudent', value: 'SU' }, { name: 'Admin', value: 'AD' },
        { name: 'Syndicus', value: 'SY' }],
      edit: false,
      smallScreen: false,
      edit_permission: true
    }
  },
  async beforeMount () {
    this.edit_permission = this.can_edit_permission
    this.data = await this.get_data()
    const currentUser = await this.$store.getters['session/currentUser']
    if (!this.not_admin) {
      const currentUserRole = currentUser.role
      if (currentUserRole === 'SU') {
        if (this.data.role === 'AD') {
          this.edit_permission = false
        } else {
          this.roles = [{ name: 'Aanvrager', value: 'AA' }, { name: 'Student', value: 'ST' },
            { name: 'Superstudent', value: 'SU' }]
        }
      }
    }
  },
  beforeUnmount () {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.onResize, { passive: true })
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
  },
  methods: {
    async cancel_save () {
      this.edit = !this.edit
      this.data = await this.get_data()
    },
    async save () {
      this.edit = !this.edit
      await this.save_data(this.data)
    },
    onResize () {
      this.smallScreen = window.innerWidth < 500
    }
  }
}
</script>
