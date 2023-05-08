<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Maak een nieuwe container aan</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="type"
            :items="types"
            label="type container"
          ></v-select>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="day"
            :items="days"
            label="Dag van de week"
          ></v-select>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field v-model='start_hour' label='Beginuur' required></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field v-model='end_hour' label='Einduur' required></v-text-field>
        </v-col>
      </v-row>
      <v-row class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="createContainer()">Aanmaken</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import { RequestHandler } from '@/api/RequestHandler'
import TrashTemplateService from '@/api/services/TrashTemplateService'
import { ContainerType } from '@/api/models/ContainerType'
import { Weekday } from '@/api/models/Weekday'

export default {
  name: 'CreateTrashContainerView',
  props: {
    id: Number
  },
  data: () => {
    return {
      type: '',
      day: '',
      start_hour: '',
      end_hour: '',
      smallScreen: false,
      types: [
        ContainerType.GFT,
        ContainerType.PMD,
        ContainerType.PK,
        ContainerType.GLAS,
        ContainerType.REST
      ],
      days: [
        Weekday.SUNDAY,
        Weekday.MONDAY,
        Weekday.TUESDAY,
        Weekday.WEDNESDAY,
        Weekday.THURSDAY,
        Weekday.FRIDAY,
        Weekday.SATURDAY
      ]
    }
  },
  async beforeMount () {
  },
  methods: {
    createContainer () {
      RequestHandler.handle(
        TrashTemplateService.newContainerToTemplate(this.id, {
          type: this.type,
          collection_day: {
            day: this.day,
            start_hour: this.start_hour,
            end_hour: this.end_hour
          }
        }), {
          id: 'createContainerTemplateError',
          style: 'SNACKBAR'
        }
      ).then(() =>
        this.$store.dispatch('snackbar/open', {
          message: 'De container is aangemaakt',
          color: 'success'
        }))
    }
  }
}
</script>
<style>
.text_field {
  height: 40px;
  max-width: 350px;
  padding-left: 5px;
  padding-top: 5px;
}
</style>
