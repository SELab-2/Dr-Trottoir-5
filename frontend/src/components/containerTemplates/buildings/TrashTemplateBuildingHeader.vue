<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col class="d-flex align-center" cols="2">
        <p title="Gebouw"> Gebouw </p>
      </v-col>
      <v-col class="d-flex align-center" cols="2">
        <p title="Adres"> Adres </p>
      </v-col>
      <v-col class="d-flex align-center" cols="1">
        <p v-if="!round" title="Efficiëntie"> Efficiëntie </p>
      </v-col>
      <v-col class="d-flex align-center" cols="1">
        <p title="Handleiding"> Handleiding </p>
      </v-col>
      <v-col cols="1"/>
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
