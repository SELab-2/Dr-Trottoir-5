<template>
  <v-container class="border">
    <v-row align="center" justify="center">
      <v-col cols="2" class="col">
        <p title="Naam"> Naam </p>
      </v-col>
      <v-col cols="2" class="col">
        <p title="Vuilnisbakken"> Vuilnisbakken </p>
      </v-col>
      <v-col cols="2" class="col">
        <p  title="Gebouwen"> Gebouwen </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Jaar"> Jaar </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Week"> Week </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Locatie"> Locatie </p>
      </v-col>
      <v-col cols="1" class="col">
        <p title="Even"> Even </p>
      </v-col>
      <v-col cols="2" class="text-right">
        Acties
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'TrashContainerTemplateHeader',
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
