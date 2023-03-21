<template>
  <v-container fluid>
    <v-card max-width="500px" min-width="345">
      <v-card-text>
        <v-row align-end>
          <v-col>
            <p>{{ description }}</p>
          </v-col>
          <v-col class="d-flex align-center">
            <v-row justify="center">
              <v-img :src="imageURL" :max-width="mobile ? '100%' : '250'" :max-height="150"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col>
            <p style="font-size: 8px">{{ timeStamp }}</p>
          </v-col>
          <v-col>
            <v-row justify="center">
                <v-btn v-on:click="goToEditPage" class="button-margin mr-2" color="primary" text
                       style="font-size: 45%;">
                  Pas aan
                </v-btn>
                <v-btn v-on:click="deletePost" color="primary" text style="font-size: 45%;">
                  Verwijder
                </v-btn>
            </v-row>
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
