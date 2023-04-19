<template>
  <v-container>

    <label class="black-text">Gebouwen</label>
    <v-autocomplete
      clearable
      :items="this.buildingsSyndicus"
      item-title="name"
      item-value="id"
      v-model="search"
    >
      <template v-slot:no-data>
        <div class="px-4">Er zijn geen gebouwen beschikbaar.</div>
      </template>
    </v-autocomplete>

    <div>TODO planning</div>

    <div align="center">
      <NormalButton text="Kopieer link gebouw" :parent-function="coppyLink"/>
    </div>

  </v-container>

</template>

<script>

import NormalButton from "@/components/NormalButton.vue";

export default {
  name: 'SyndicusHomeView',
  components: {NormalButton},
  data: function () {
    return {
      search: '',
      buildingsSyndicus: [
        {
          id: 1,
          name: 'Gebouw 1'
        },
        {
          id: 2,
          name: 'Gebouw 2'
        },
        {
          id: 3,
          name: 'Gebouw 3'
        }
      ]
    }
  }, methods: {
    coppyLink: function () {
      // TODO unieke link naar gebouw kopieren
    }
  }

}
</script>

<style scoped>

</style>
