<template>
  <v-container fluid>
    <v-card max-width="800px" min-width="345" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col>
            <p style="font-size: 8px">{{ description }}</p>
          </v-col>
          <v-col class="d-flex align-center">
            <v-row justify="end" class="image-margin">
              <v-img :src="imageURL" :max-width="'150'" :max-height="150"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col>
            <p style="font-size: 8px">{{ timeStamp }}</p>
          </v-col>
          <v-col>
            <v-row justify="end" class="row-margin">
              <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;"
                     v-on:click="goToEditPage">
                <img :src="require('@/assets/edit.png')" alt="Button Image" style="max-height: 35px; max-width: 35px;"/>
              </v-btn>
              <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
                <img :src="require('@/assets/delete.png')" alt="Button Image"
                     style="max-height: 35px; max-width: 35px"/>
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
  name: 'FotoCardStudent',
  props: {
    timeStamp: { type: String, default: 'Empty time' },
    description: { type: String, default: 'Geen description meegegeven' },
    imageURL: { type: String, default: require('@/assets/emptyImage.png') }
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
  margin-right: 12px;
}
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
