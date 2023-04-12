<template>
  <div align="center">
    <h1>{{ data.nameBuilding }}</h1>
    <v-container>
      <v-img style="max-height: 30vh;" :src="data.imageURL"></v-img>
    </v-container>
  </div>
  <v-container >
    <v-btn rounded="xl" @click="downloadFile">
      <v-icon color="#FFE600" dark>mdi-file</v-icon>
      <p style="color: #FFE600">Handleiding</p>
    </v-btn>
  </v-container>
  <v-container class="container-border">
    <h2>Opmerkingen:</h2>
    <v-list>
      <v-list-item v-for="remark in data.remarks">{{ remark }}</v-list-item>
    </v-list>
  </v-container>

</template>

<script>

/**
 * InfoScreenBuilding component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * nameBuilding: String naam van het gebouw
 * imageURL: String foto van het gebouw
 * remarks: Array de opmerkingen van het gebouw (code poort, locatie, etc.)
 */

export default {
  name: 'InfoScreenBuilding',
  props: {
    data: {
      type: Object,
      default: () => ({
        nameBuilding: "Empty",
        imageURL: 'empty',
        remarks: []
      })
    }
  },
  methods: {
    downloadFile: function () {
      // TODO file opvragen van de backend en downloaden
      console.log("Download file")
    }
  }
}
</script>

<style scoped>

</style>
