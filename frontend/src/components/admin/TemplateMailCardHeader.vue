<template>
  <v-container class="border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>Titel</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>Aantal argumenten</p>
      </v-col>
      <v-col/>
      <v-col cols="3" class="d-flex align-center justify-end"/>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'TemplateMailCardHeader'
}
</script>

<style scoped>

.border {
  border: 1px solid #E3e3e3;
}

</style>
