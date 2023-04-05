<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2" class="col">
        <p title="Naam"> Naam </p>
      </v-col>
      <v-col cols="2" class="col">
        <p title="Adres"> Adres </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Efficiëntie"> Efficiëntie </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Handleiding"> Handleiding </p>
      </v-col>
      <v-col cols="1" class="col"/>
      <v-col cols="3" class="col">
        <p title="Status"> Status </p>
      </v-col>
      <v-col cols="2" class="text-right">
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'BuildingHeader'
}
</script>

<style scoped>
  .col {
    display: inline-block;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
  }
  .col:hover {
    white-space: normal;
  }
</style>
