<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p @click="goToBuildingPage" class="text-style-building">{{ this.args.gebouw }}</p>
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
              <v-icon color="#FFE600" icon="mdi-file"></v-icon>
              <v-icon color="#FFE600" right>mdi-menu-down</v-icon>
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
              v-bind="props"
            >
              <span :style="{ color: status === 'Update nodig' ? 'red' : status === 'Klaar' ? 'green' : '' }">{{
                  status
                }}</span>

              <v-icon right>mdi-menu-down</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in documentStatus"
              :key="index"
              :value="index"
              @click="updateStatus(item.title)"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2" class="text-right">
        <v-btn icon class="button-style" v-on:click="deletePost">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DeleteIcon from '@/components/DeleteIcon.vue'
/**
 * RoundBuildingCard component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * gebouw: String
 * adres: String
 * status: String
 */

export default {
  name: 'RoundBuildingCard',
  components: { DeleteIcon },
  props: {
    args: {
      type: Object,
      default: () => ({ gebouw: 'Empty', adres: 'Empty', status: '' })
    }
  },
  data: () => ({
    status: '',
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
    },
    updateStatus: function (newStatus) {
      this.status = newStatus
      // TODO opslaan in database
    },
    goToBuildingPage: function () {
      // TODO
    }
  },
  async mounted () {
    this.status = this.args.status
  }
}
</script>

<style scoped>
.text-style-building{
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
