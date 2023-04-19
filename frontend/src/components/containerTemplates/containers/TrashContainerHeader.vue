<template>
  <v-container class="border">
    <v-row align="center" justify="center">
      <v-col cols="2" class="col">
        <p title="Dag"> Dag </p>
      </v-col>
      <v-col cols="2" class="col">
        <p title="Uren"> Uren </p>
      </v-col>
      <v-col cols="2" class="col">
        <p  title="Type"> Type </p>
      </v-col>
      <v-col cols="2" class="col"/>
      <v-col cols="4" class="text-right">
        Acties
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'TrashContainerHeader',
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
