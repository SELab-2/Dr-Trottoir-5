<!--
  A component card that gives information about a location.
    Name: String
-->

<template>
  <v-container class="container-border" resizable="true">
    <v-row>
      <v-col cols="2" class="d-flex align-center justify-center">
        <p>{{ data.name }}</p>
      </v-col>
      <v-col cols="10" class="d-flex align-center justify-end">
        <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deleteLocation">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import {RequestHandler} from "@/api/RequestHandler";
import LocationService from "@/api/services/LocationService";
import router from "@/router";
export default {
  name: "LocationCard",
  components: {DeleteIcon},
  props: {
    data: {
      type: Object,
      default: () => ({
        id: 0,
        name: '',
      })
    }
  },
  methods: {
    deleteLocation() {
      RequestHandler.handle(LocationService.deleteLocationById(this.data.id), {
        id: 'locationCardDeleteError',
        style: 'SNACKBAR',
        customMessages: [
          {
            code: '500',
            message: 'De locatie is nog verbonden aan student, gebouw ...',
            description: 'Key error'
          }
        ]
      })
        .then(() => {
          router.push({name: 'locations'})
          router.go(0)
        })
        .catch(() =>
        this.$store.dispatch("snackbar/open", {
          message: "De locatie is nog verbonden aan student, gebouw ...'",
          color: "error"
        }))
    }
  }
}
</script>

<style scoped>

</style>
