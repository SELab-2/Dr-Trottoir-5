<template>
  <v-card class='px-4'>
    <h1>Should be the navbar</h1>
    <v-spacer></v-spacer>
  </v-card>
  <v-card color="white" :class="`mx-auto my-16 h-70 ${smallScreen ? 'w-100' : 'w-75'}`">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center pt-10">
        <h1>Voornaam</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center pt-10">
        <h1>Achternaam</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center">
        <v-text-field :readonly="!edit" variant="outlined"
                      style="height: 40px; width: 450px; padding-left: 5px; padding-top: 5px">
          {{ first_name }}
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center">
        <v-text-field :readonly="!edit" variant="outlined"
                      style="height: 40px; width: 450px; padding-left: 5px; padding-top: 5px">
          {{ last_name }}
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center pt-10">
        <h1>E-mail</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center pt-10">
        <h1>GSM</h1>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center">
        <v-text-field :readonly="!edit" variant="outlined"
                      style="height: 40px; width: 450px; padding-left: 5px; padding-top: 5px">
          {{ email }}
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="6" class="d-flex justify-center align-center">
        <v-text-field :readonly="!edit" variant="outlined"
                      style="height: 40px; width: 450px; padding-left: 5px; padding-top: 5px">
          {{ phone_nr }}
        </v-text-field>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center pt-10">
        <h1>Rol</h1>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center">
        <template v-for="(value, key) in {'ST':'Student', 'SS':'Superstudent', 'AD':'Admin'}" :key="key">
          <v-checkbox :model-value="key === role" :readonly="!edit"
                      :label="value"></v-checkbox>
        </template>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center">
        <h1>Rondes</h1>
      </v-col>
      <v-col cols="12" sm="12" md="12" lg="12" class="d-flex justify-center align-center">
        <template v-for="ronde in ['Ronde 1']" :key="ronde">
          <v-checkbox :model-value="ronde in rondes" :readonly="!edit" :label="ronde"></v-checkbox>
        </template>
      </v-col>
      <v-col v-if="!edit" class="d-flex justify-center align-center pb-10" cols="12" sm="12" md="12" lg="12">
        <normal-button text='Pas aan' :parent-function='edit_click'/>
      </v-col>
      <v-col v-else class="d-flex justify-center align-center pb-10" cols="12" sm="12" md="12" lg="12">
        <normal-button text='Aanpassingen opslaan' :parent-function="save"/>
        <normal-button text='Annuleer' :parent-function="cancel_save" class="ml-2"/>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import NormalButton from '@/components/NormalButton'
import { request } from '@/authorized'

export default {
  components: { NormalButton },
  data: () => {
    return {
      first_name: '',
      last_name: '',
      email: '',
      phone_nr: '',
      show: false,
      role: '',
      rondes: [],
      edit: false,
      smallScreen: false
    }
  },
  async created () {
    await this.set_data()
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
    async set_data () {
      const data = await request('api/user', 'GET')
      this.first_name = data.first_name
      this.last_name = data.last_name
      this.email = data.email
      this.phone_nr = data.phone_nr
      this.role = data.role
    },
    cancel_save () {
      this.edit = !this.edit
      this.set_data()
    },
    edit_click () {
      this.edit = !this.edit
    },
    save () {
      // TODO save request
      this.edit = !this.edit
      console.log('Saved!')
    },
    onResize () {
      this.smallScreen = window.innerWidth < 500
    }
  }
}
</script>
