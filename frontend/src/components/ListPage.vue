<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <NavigationBar/>
      </v-col>
      <v-col cols="12">
        <v-row class="pa-5">
            <h1>{{ title }}</h1>
          <v-row></v-row>
            <NormalButton text="+" v-bind:parent-function="addFunction"/>
        </v-row>
      </v-col>
      <v-col cols="12">
        <SearchDropdown v-bind:options="elements" placeholder="Search ..."/>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import NormalButton from '@/components/NormalButton'
import SearchDropdown from '@/components/SearchDropdown'
export default {
  name: 'ListPage',
  components: { SearchDropdown, NormalButton },
  props: {
    title: { type: String, default: '' },
    addFunction: { type: Function, default: null }
  },
  data: () => ({
    elements: ['Banana', 'Appel', 'Kiwi']
  })
}
</script>

<style scoped>

</style>
