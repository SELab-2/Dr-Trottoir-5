<template>
  <v-container fluid>
    <v-card max-width="900px" min-width="500px" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col align="left" cols="8">
            <p style="font-size: 16px; font-weight: bold;">{{ data.remark }}</p>
          </v-col>
          <v-col class="d-flex align-center" cols="4">
            <v-row justify="end" class="image-margin">
              <v-img :src="data.image" :max-width="300" :max-height="300"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col align="left">
            <p style="font-size: 16px">{{ data.time.split('.')[0] }}</p>
          </v-col>
          <v-col>
            <v-row justify="end" class="row-margin">
              <v-icon class="row-margin" v-on:click="goToMailPage" dark size="30px">mdi-email-outline</v-icon>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>

/**
 * FotoCardAdmin component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * time: String
 * remark: String
 * image: String
 */

export default {
  name: 'FotoCardAdmin',
  props: {
    data: {
      type: Object,
      default: () => ({ time: 'Empty', remark: 'Empty', image: 'empty' })
    }
  },
  methods: {
    goToMailPage: function () {
      // TODO
    }
  },
  components: {}
}
</script>

<style scoped>

</style>
