<template>
  <v-container class="container-border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ name }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ day }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ formattedTime }}</p>
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
export default {
  name: 'TrashPickupCard',
  props: {
    formattedTime: { type: String, default: 'Empty' },
    name: { type: String, default: 'Empty' },
    day: { type: String, default: 'Empty' }
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
