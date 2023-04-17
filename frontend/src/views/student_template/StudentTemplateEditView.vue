<template>
<v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-text-field v-model='name' label='Naam' :readonly="!edit" required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='status' label='Status' readonly required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-checkbox label="Even" v-model="even" :readonly="!edit"></v-checkbox>
        </v-col>
      </v-row>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' sm='6' md='6'>
          <v-text-field v-model='location' label='Locatie' :readonly="!edit" required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='start_hour' label='Standaard Startuur' :readonly="!edit" required></v-text-field>
        </v-col>
        <v-col cols="12" sm="3" md="3">
          <v-text-field v-model='end_hour' label='Standaard Einduur' :readonly="!edit" required></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex justify-center mx-auto" cols="12" sm="3" md="3">
          <NormalButton text="Pas aan" v-bind:parent-function="validate" block></NormalButton>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
  <v-row class="justify-center">
    <div class="text-h3">
        Rondes
    </div>
  </v-row>
</template>

<script>
import NormalButton from '@/components/NormalButton.vue';

export default {
  name: "StudentTemplateEditView",
  components: {
    NormalButton
  },
  data: () => ({
    edit: false,
    id: 0,
    name: 'Test Student Template',
    status: 'Actief',
    even: true,
    location: 'Gent',
    start_hour: '17:00',
    end_hour: '20:00'
  }),
  created() {
    this.id = this.$route.params.id
  }
}
</script>

<style scoped>

</style>
