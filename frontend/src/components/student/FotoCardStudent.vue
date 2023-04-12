<template>
  <v-container fluid>
    <v-card max-width="800px" min-width="250px" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col align="left" cols="8">
            <p style="font-size: 8px">{{ data.description }}</p>
          </v-col>
          <v-col class="d-flex align-center" cols="4">
            <v-row justify="end" class="image-margin">
              <v-img :src="data.imageURL" :max-width="'150'" :max-height="150"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col align="left">
            <p style="font-size: 8px">{{ data.timeStamp }}</p>
          </v-col>
          <v-col>
            <v-row justify="end" class="row-margin">
              <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;"
                     v-on:click="goToEditPage">
                <EditIcon/>
              </v-btn>
              <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
                <DeleteIcon/>
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import EditIcon from '../icons/EditIcon.vue'
import DeleteIcon from '../icons/DeleteIcon.vue'

/**
 * FotoCardStudent component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * timeStamp: String
 * description: String
 * imageURL: String
 */

export default {
  name: 'FotoCardStudent',
  props: {
    data: {
      type: Object,
      default: () => ({ timeStamp: 'Empty', description: 'Empty', imageURL: 'Empty' })
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
