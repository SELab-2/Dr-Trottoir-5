<!--
  A component card that gives information about a location.
    Name: String
-->

<template>
  <v-container class="container-border" resizable="true">
    <v-row>
      <v-col cols="9">
        <v-row>
          <v-col>
            <p>{{ data.name }}</p>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="3" class="d-flex align-center justify-end">
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
      })
      this.$emit('removed')
    }
  }
}
</script>

<style scoped>

</style>
