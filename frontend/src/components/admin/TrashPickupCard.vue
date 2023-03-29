<template>
  <v-container class="container-border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ data.name }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ data.day }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ data.formattedTime }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center justify-end">
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
          <EditIcon/>
        </v-btn>
        <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import EditIcon from '../icons/EditIcon.vue'
import DeleteIcon from '../icons/DeleteIcon.vue'

/**
 * TrashPickupCard component wordt gebruikt door als props een Object met de volgende keys mee te geven
 * name: String
 * day: String
 * formattedTime: String
 */

export default {
  name: 'TrashPickupCard',
  props: {
    data: {
      type: Object,
      default: () => ({ name: 'Empty', day: 'Empty', formattedTime: 'Empty' })
    }
  },
  methods: {
    goToEditPage: function () {
      // TODO
    },
    deletePost: function () {
      // TODO
    }
  },
  components: {
    EditIcon,
    DeleteIcon
  }
}
</script>

<style scoped>

</style>
