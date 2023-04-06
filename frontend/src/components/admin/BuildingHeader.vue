<template>
  <v-container class="border">
    <v-row align="center" justify="center">
      <v-col cols="2" class="col">
        <p title="Gebouw"> Gebouw </p>
      </v-col>
      <v-col cols="2" class="col">
        <p title="Adres"> Adres </p>
      </v-col>
      <v-col cols="1" class="col">
        <p v-if="!round" title="Efficiëntie"> Efficiëntie </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Handleiding"> Handleiding </p>
      </v-col>
      <v-col cols="1" class="col"/>
      <v-col cols="3" class="col">
        <p title="Document status"> Document status </p>
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
