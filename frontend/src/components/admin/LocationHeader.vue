<!--
  The header of the Location list page. It only shows the name of the location.
    Name: String
-->

<template>
  <v-container class="border">
    <v-row align="center" justify="start">
      <v-col cols="2" class="col pl-10">
        <p title="Name"> Naam </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "LocationHeader"
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
