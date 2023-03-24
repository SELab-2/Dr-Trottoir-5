<template>
  <v-container class="container-border test-style">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p>{{ this.args.name }}</p>
      </v-col>
      <v-col cols="3">
        <p>{{ this.args.adres }}</p>
      </v-col>
      <v-col cols="1">
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
            >
              <v-icon icon="mdi-file"></v-icon>
              <v-icon right>mdi-menu-down</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item value="download" @click="downloadDocument">
              <v-icon color="red" icon="mdi-file-pdf-box"></v-icon>
              PFD
            </v-list-item>
            <v-list-item value="upload" @click="uploadDocument">
              <v-icon color="#FFE600" icon="mdi-file-upload-outline"></v-icon>
              Upload
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2">
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn
              color="primary"
              v-bind="props"
            >
              {{ args.status }}
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in documentStatus"
              :key="index"
              :value="index"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2" class="text-right">
        <v-btn icon class="button-style" v-on:click="deletePost">
          <v-avatar color="red" class="button-style">
            <v-icon dark>mdi-delete</v-icon>
          </v-avatar>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'RoundBuildingCard',
  props: {
    args: {
      type: Object,
      default: () => ({ name: 'Empty', adres: 'Empty', status: '' })
    }
  },
  data: () => ({
    documentStatus: [
      { title: 'Klaar' },
      { title: 'Update nodig' },
      { title: 'Bezig' },
      { title: 'Geüpdatet' }
    ] // TODO + updaten in database
  }),
  methods: {
    deletePost: function () {
      // TODO
    },
    uploadDocument: function () {
      // TODO
    },
    downloadDocument: function () {
      // TODO
    }
  }
}
</script>

<style scoped>
.test-style {
  margin-top: 10px;
}

</style>
