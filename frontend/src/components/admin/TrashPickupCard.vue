<template>
  <v-container class="container-border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ args.name }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ args.day }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ args.formattedTime }}</p>
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
import EditIcon from '../EditIcon.vue'
import DeleteIcon from '../DeleteIcon.vue'

/**
 * TrashPickupCard component wordt gebruikt door als props een Object met de volgende keys mee te geven
 * name: String
 * day: String
 * formattedTime: String
 */

export default {
  name: 'TrashPickupCard',
  props: {
    args: {
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
