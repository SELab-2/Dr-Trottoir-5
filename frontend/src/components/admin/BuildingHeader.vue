<template>
  <v-container class="border">
    <v-row align="center" justify="center">
      <v-col cols="2" class="col">
        <p data-test="title" title="Gebouw"> Gebouw </p>
      </v-col>
      <v-col cols="2" class="col">
        <p data-test="adres" title="Adres"> Adres </p>
      </v-col>
      <v-col cols="1" class="col">
        <p data-test="round" v-if="!round" title="Efficiëntie"> Efficiëntie </p>
      </v-col>
      <v-col cols="2" class="col">
        <p data-test="manual" title="Handleiding"> Handleiding </p>
      </v-col>
      <v-col cols="3" class="col">
        <p data-test="status" title="Document status"> Document status </p>
      </v-col>
      <v-col cols="2" class="text-right">
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'BuildingHeader',
  props: {
    round: { type: Boolean, default: false }
  }
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
  .border {
      border: 1px solid #E3e3e3;
  }
</style>
