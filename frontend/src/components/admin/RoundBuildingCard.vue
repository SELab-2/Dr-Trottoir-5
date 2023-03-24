<template>
  <v-container class="container-border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ name }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ adres }}</p>
      </v-col>
      <v-col/>
      <v-col cols="3" class="d-flex align-center justify-end">
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
          <img :src="require('@/assets/edit.png')" alt="Button Image" style="max-height: 35px; max-width: 35px;"/>
        </v-btn>
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
  }
}
</script>

<style scoped>

</style>
