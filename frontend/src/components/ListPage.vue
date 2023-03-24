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
        <SearchDropdown v-bind:options="terms" placeholder="Search ..." v-on:selected="onSearch"/>
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
              <component :is="childComponent" v-bind:text="el"/>
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
      type: [String],
      default: 'div',
      required: true
    },
    childComponent: {
      type: String,
      default: 'div',
      required: true
    },
    elements: {
      type: Array,
      default: () => [],
      required: false
    },
    terms: {
      type: Array,
      default: () => [],
      required: false
    }
  },
  methods: {
    onSearch (newValue) {
      this.searched = newValue
    }
  },
  computed: {
    filteredOptions () {
      const filtered = []
      const regex = new RegExp(this.searched, 'ig')
      for (const el of this.elements) {
        if (this.searched.length < 1 || el.match(regex)) {
          filtered.push(el)
        }
      }
      return filtered
    }
  },
  data () {
    return {
      searched: ''
    }
  }
}
</script>

<style scoped>
  ul { list-style-type: none; }
</style>
