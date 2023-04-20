<template>
  <v-container class="border">
    <v-row align="center" justify="center">
      <v-col class="col" cols="2">
        <p title="Gebouw"> Gebouw </p>
      </v-col>
      <v-col class="col" cols="2">
        <p title="Adres"> Adres </p>
      </v-col>
      <v-col class="col" cols="1">
        <p v-if="!round" title="Efficiëntie"> Efficiëntie </p>
      </v-col>
      <v-col class="col" cols="1">
        <p title="Handleiding"> Handleiding </p>
      </v-col>
      <v-col class="col" cols="1"/>
      <v-col class="col" cols="3">
        <p title="Document status"> Document status </p>
      </v-col>
      <v-col class="text-right" cols="2">
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'TrashTemplateBuildingHeader',
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
