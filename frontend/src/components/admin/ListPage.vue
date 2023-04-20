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
          <h1>{{ this.title }}</h1>
          <v-row></v-row>
          <div v-if="this.title !== 'Studenten' && this.title !== 'Syndicusen'">
            <NormalButton text="+" v-bind:parent-function="addFunction"/>
          </div>
            <div v-if="!refresh && this.title !== 'Studenten' && this.title !== 'Syndicusen'">
              <NormalButton text="+" v-bind:parent-function="addFunction"/>
            </div>
            <div v-else-if="refresh">
              <v-btn icon="mdi-refresh" @click="refresh_function"></v-btn>
            </div>
        </v-row>
      </v-col>
      <v-col cols="12" v-if="this.search">
        <SearchDropdown :elements="elements" :keys="keys" placeholder="Search ..."
                        v-on:keyChange="onKeyChange" v-on:selected="onSearch"/>
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
              <component :is="childComponent" v-bind:data="el"/>
            </v-col>
          </li>
        </ul>
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
    title: {
      type: String,
      default: '',
      required: true
    },
    addFunction: {
      type: Function,
      default: null,
      required: true
    },
    headComponent: {
      type: Object,
      default: 'div',
      required: false
    },
    childComponent: {
      type: Object,
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
    refresh : {
      type: Boolean,
      default: false
    },
    refresh_function : {
      type: Function,
      default: () => {}
    },
    search: {
      type: Boolean,
      default: true,
      required: false
    }
  },
  methods: {
    onSearch(newValue) {
      this.searched = newValue
    },
    onKeyChange(newValue) {
      this.key = newValue
    }
  },
  computed: {
    filteredOptions() {
      const filtered = []
      if (this.key !== 'key') {
        const regex = new RegExp(this.searched, 'ig')
        for (const el of this.elements) {
          if (this.searched.length < 1 || el[this.key].toString().match(regex)) {
            filtered.push(el)
          }
        }
        return filtered
      }
    }
  },
  data() {
    return {
      searched: '',
      key: this.keys[0]
    }
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
}
</style>
