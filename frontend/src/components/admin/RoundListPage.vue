<!--
Template voor een oplijstingspagina
Heeft als nodige argumenten nodig:
  Title: Titel van de pagina
  addFunction: Een functie voor het aanmaken van een nieuw item
  headComponent: Een html component of html tekst die de header voorstelt voor de lijst
  childComponent: Een html component die de elementen van de lijst weergeven
  elements: Een lijst met objecten die de elementen voorstellen

-->

<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-row class="pa-5">
            <h1>{{ title }}</h1>
          <v-row></v-row>
            <NormalButton text="+" v-bind:parent-function="addFunction"/>
        </v-row>
      </v-col>
      <v-col cols="12">
        <RoundSearchDropdown placeholder="Zoeken ..." v-on:selected="onSearch" v-on:key="onKeyChange" :elements="elements" :keys="this.keys" :map-keys="mapKeys"/>
      </v-col>
      <v-col/>
      <v-col cols="12">
        <component :is="headComponent"/>
      </v-col>
      <v-col/>
      <v-col cols="12">
        <ul>
          <li v-for="(el) in filteredOptions" :key="el">
            <v-col cols="12">
              <component :is="childComponent" v-bind:data="el" v-bind:keyValue="this.key" v-bind:searched="this.searched"/>
            </v-col>
          </li>
        </ul>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import NormalButton from '@/components/NormalButton'
import RoundSearchDropdown from "@/components/util/RoundSearchDropdown";
export default {
  name: 'ListPage',
  components: { RoundSearchDropdown, NormalButton },
  props: {
    title: {
      type: String,
      default: '',
      required: true
    },
    addFunction: {
      type: Function,
      default: () => null,
      required: true
    },
    headComponent: {
      type: [String],
      default: 'div',
      required: false
    },
    childComponent: {
      type: String,
      default: 'div',
      required: true
    },
    elements: {
      type: Array,
      default: () => [],
      required: true
    },
    keys: {
      type: Array,
      default: () => ['default'],
      required: true
    },
    mapKeys: {
      type: Map,
      default: {},
      required: true
    }
  },
  methods: {
    onSearch (newValue) {
      this.searched = newValue
    },
    onKeyChange (newValue) {
      this.key = newValue
    }
  },
  computed: {
    filteredOptions () {
      const filtered = []
      const regex = new RegExp(this.searched, 'ig')
      if (this.key === 'roundName') {
        for (const el of this.elements) {
          if (this.searched.length < 1 || el['name'].toString().match(regex)) {
            filtered.push(el)
          }
        }
      } else {
          return this.elements
      }
      return filtered
    }
  },
  data () {
    return {
      searched: '',
      key: this.keys[0]
    }
  },
}
</script>

<style scoped>
  ul { list-style-type: none; }
</style>
