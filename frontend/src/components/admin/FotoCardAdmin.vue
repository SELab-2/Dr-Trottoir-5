<template>
  <v-container fluid>
    <v-card max-width="450px" min-width="330px" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col>
            <p style="font-size: 8px">{{ data.description }}</p>
          </v-col>
          <v-col class="d-flex align-center">
            <v-row justify="end" class="image-margin">
              <v-img :src="data.imageURL" :max-width="'150'" :max-height="150"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col>
            <p style="font-size: 8px">{{ data.timeStamp }}</p>
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
 * timeStamp: String
 * description: String
 * imageURL: String
 */

export default {
  name: 'FotoCardAdmin',
  props: {
    data: {
      type: Object,
      default: () => ({ timeStamp: 'Empty', description: 'Empty', imageURL: 'Empty' })
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
.row-margin {
  margin-bottom: 0;
  margin-right: 0;
  margin-top: 5px;
}

.image-margin {
  margin-right: 0;
  margin-top: 0;
}

.container-border{
  border: 1px solid #E3e3e3;
  border-radius: 25px;
}
</style>
