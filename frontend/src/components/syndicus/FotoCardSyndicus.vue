<template>
  <v-container fluid>
    <v-card max-width="450px" min-width="250px" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col align="left" cols="8">
            <p data-test="description" style="font-size: 15px">{{ data.description }}</p>
          </v-col>
          <v-col class="d-flex align-center" cols="4">
            <v-row justify="end" class="image-margin">
              <v-img data-test="image" :src="data.imageURL" :max-width="'150'" :max-height="150"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col align="left">
            <p data-test="time" style="font-size: 10px">{{ data.timeStamp }}</p>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>

/**
 * FotoCardSyndicus component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * timeStamp: String
 * description: String
 * imageURL: String
 */

export default {
  name: 'FotoCardSyndicus',
  props: {
    data: {
      type: Object,
      default: () => ({ timeStamp: 'Empty', description: 'Empty', imageURL: 'Empty' })
    }
  }
}
</script>

<style scoped>

</style>
