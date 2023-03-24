<template>
  <v-container class="container-border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ name }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ argsCount }}</p>
      </v-col>
      <v-col/>
      <v-col cols="3" class="d-flex align-center justify-end">
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
          <EditIcon/>
        </v-btn>
        <v-btn icon tile class="button-style" v-on:click="deletePost">
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
  name: 'TemplateMailCard',
  props: {
    name: { type: String, default: 'Empty' },
    argsCount: { type: Number, default: 0 }
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
