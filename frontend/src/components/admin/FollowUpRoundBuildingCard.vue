<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p @click="goToBuildingPage" class="text-style-building">{{ this.data.gebouw }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{ this.data.adres }}</p>
      </v-col>
      <v-col cols="1">
        <p :style="{
    color:
      this.data.efficiency < 50 ? '#FF1F00' :
      this.data.efficiency < 75 ? '#E88E4D' :
      '#39AE68'
  }">{{ this.data.efficiency }}%</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'FollowUpRoundBuildingCard',
  props: {
    data: {
      type: Object,
      default: () => ({ gebouw: 'Empty', adres: 'Empty', status: '', efficiency: 0 })
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
    editPost: function () {
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
    this.status = this.data.status
  }
}
</script>

<style scoped>
.text-style-building {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
