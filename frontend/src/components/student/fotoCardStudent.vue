<template>
  <v-container fluid>
    <v-card max-width="600px" min-width="345">
      <v-card-text>
        <v-row align-end>
          <v-col>
            <p>{{ description }}</p>
          </v-col>
          <v-col align="right">
            <v-img :src="imageURL" :max-width="mobile ? '100%' : '250'" :max-height="250"></v-img>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <p>{{ timeStamp }}</p>
          </v-col>
          <v-col align="right">
            <v-btn v-on:click="goToEditPage" class="button-margin" color="primary" text style="font-size: 45%;">Pas aan</v-btn>
            <v-btn v-on:click="deletePost" color="primary" text style="font-size: 45%;" >Verwijder</v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'fotoCardStudent',
  props: {
    timeStamp: Date,
    description: { type: String, default: 'Geen description meegegeven' },
    imageURL: String
  },
  methods: {
    goToEditPage: function () {
      // TODO
    },
    deletePost: function () {
      // TODO
    }
  }
}
</script>

<style scoped>
.button-margin {
  margin-right: 6px;
}
</style>
