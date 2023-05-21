<template>
  <v-row v-if="this.status === 'A'" class="px-5 justify-center mx-auto">
    <v-col cols="12" sm="3" md="3">
      <v-btn class="mx-5 bg-secondary text-primary" @click="eenmalig">Eenmalig aanpassen</v-btn>
    </v-col>
    <v-col cols="12" sm="3" md="3">
      <v-btn class="mx-5 bg-primary text-secondary"  @click="permanent" block>Permanent aanpassen</v-btn>
    </v-col>
  </v-row>
  <v-row v-if="this.status === 'E'" class="px-5 justify-center mx-auto">
    <v-col cols="12" sm="3" md="3">
      <v-btn class="mx-5 bg-primary text-secondary" @click="eenmalig">Aanpassing opslaan</v-btn>
    </v-col>
  </v-row>
  <div v-if="this.status === 'V'" class="px-3 text-caption">Om deze template aan te passen moeten eerst de eenmalige aanpassingen ongedaan worden.</div>

</template>

<script>
export default {
  name: "StateButtons",
  props: {
    eenmalig: Function,
    permanent: Function,
    status: String
  }
}
</script>

<style scoped>

</style>
