<template>
  <v-container class="container-border">
    <v-row align="center">
      <v-col cols="3">
        <p>{{ name }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{ adres }}</p>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="1">
        <v-select
          :items="documentActions"
          v-model="selectedActions"
        ></v-select>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="1">
        <v-select
          :items="documentStatus"
          v-model="selectedStatus"
        ></v-select>
      </v-col>
      <v-col cols="1"/>
      <v-col cols="2" class="text-right">
        <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
          <img :src="require('@/assets/delete.png')" alt="Button Image" style="max-height: 35px; max-width: 35px"/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'RoundBuildingCard',
  props: {
    name: { type: String, default: 'Empty' },
    adres: { type: String, default: 'Empty' }
  },
  data: () => ({
    documentActions: ['Type 1', 'Type 2', 'Type 3'],
    selectedActions: null,
    documentStatus: ['Option 1', 'Option 2', 'Option 3'],
    selectedStatus: null // TODO
  }),
  methods: {
    deletePost: function () {
      // TODO
    }
  }
}
</script>

<style scoped>

</style>
