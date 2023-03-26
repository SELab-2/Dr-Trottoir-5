<!--
Template voor een zoekbalk met een een knop ernaast om te zoeken op een bepaald argument
Indien er een zoekbalk alleen nodig is, kunnen we deze nog splitsen in twee aparte componenten
Er moet een lijst van objecten worden meegegeven, het standaard zoek argument is de eerste parameter van het object.
De parameter kan verandert worden door op de knop een andere parameter te kiezen.
-->

<template>
  <v-row align="center">
    <v-col cols="12" class="d-flex justify-center">
      <v-icon class="icon">mdi-magnify</v-icon>
      <div class="dropdown" v-if="filteredOptions">
        <div class="dropdown-toggle">
          <input
            :name="name"
            @focus="showOptions()"
            @blur="exit()"
            @keyup="keyMonitor"
            v-model="searchFilter"
            v-on:input="showOptions"
            :placeholder="placeholder"
          />
        </div>
        <transition name="fade">
          <ul class="dropdown-menu" v-show="optionsShown">
            <li
              @mousedown="selectOption(option)"
              v-for="(option) in filteredOptions"
              :key="option"
            >
              <a href="javascript:void(0)">
                {{ option }}
              </a>
            </li>
          </ul>
        </transition>
      </div>
      <NormalButton :text="this.key" id="menu-activator" class="button"/>
      <v-menu activator="#menu-activator" class="text-yellow">
        <v-list>
          <v-list-item
            v-for="property in Object.keys(elements[0])"
            :key="property"
            :value="property"
            @click="changeKey(property)"
          >
            <v-list-item-title>{{ property }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-col>
  </v-row>
</template>

<script>
import NormalButton from '@/components/NormalButton'

export default {
  name: 'SearchDropdown',
  components: { NormalButton },
  props: {
    name: {
      type: String,
      required: false,
      default: 'input'
    },
    elements: {
      type: Array,
      default: () => [],
      required: true
    },
    placeholder: {
      type: String,
      required: false,
      default: 'Please select an option'
    }
  },
  data () {
    return {
      selected: '',
      optionsShown: false,
      searchFilter: '',
      key: Object.keys(this.elements[0])[0]
    }
  },
  computed: {
    filteredOptions () {
      const filtered = []
      const regex = new RegExp(this.searchFilter, 'ig')
      for (const option of this.elements) {
        if (this.searchFilter.length < 1 || option[this.key].toString().match(regex)) {
          filtered.push(option[this.key].toString())
        }
      }
      return filtered
    }
  },
  methods: {
    changeKey (key) {
      this.key = key
      this.selected = ''
      this.searchFilter = ''
      this.$emit('key', this.key)
      this.$emit('selected', this.selected)
    },
    selectOption (option) {
      this.selected = option
      this.optionsShown = false
      this.searchFilter = this.selected
      this.$emit('selected', this.selected)
    },
    showOptions () {
      this.optionsShown = true
    },
    // When clicking out of the searchmenu
    exit () {
      this.optionsShown = false
      this.$emit('selected', this.searchFilter)
    },
    // Selecting when pressing Enter
    keyMonitor: function (event) {
      if (event.key === 'Enter') {
        if (this.filteredOptions[0] === this.searchFilter) {
          this.selectOption(this.filteredOptions[0])
        } else {
          this.exit()
        }
      }
    }
  }
}
</script>

<style scoped>

.icon {
  position: relative;
  overflow: hidden;
  display: inline-block;
  top: 38px;
  left: 37px;
  z-index: 200;

}

.button {
  position: relative;
  top: 35px;
  left: 20px;
  display: inline-block;
  vertical-align: middle;

}

.dropdown {
  min-width: 160px;
  height: 40px;
  position: relative;
  margin: 10px 1px;
  display: inline-block;
  vertical-align: middle;
  overflow: visible !important;
}
.dropdown a:hover {
  text-decoration: none;
}

.dropdown-toggle {
  position: relative;
  display: inline-block;
  transition: 0.75s ease-in;
  border-radius: 2px 2px 0 0;
}
.dropdown-toggle input {
  display: block;
  width: 350px;
  margin: 20px auto;
  padding: 10px 45px;
  background: white;
  background-size: 15px 15px;
  font-size: 16px;
  border: #e3e3e3;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0 2px 5px -1px,
    #e3e3e3 0 1px 3px -1px;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  float: left;
  min-width: 160px;
  width: 100%;
  padding: 10px 20px 10px 10px;
  margin: 25px 0 0;
  list-style: none;
  font-size: 14px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 4px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}

.dropdown-menu > li > a {
  padding: 10px 20px;
  display: block;
  clear: both;
  font-weight: normal;
  line-height: 1.6;
  color: #333333;
  white-space: nowrap;
  text-decoration: none;
  max-width: 100%;
}
.dropdown-menu > li > a:hover {
  background: #efefef;
  color: #333333;
  border-radius: 4px;
}

.dropdown-menu > li {
  overflow: hidden;
  position: relative;
  margin: 0;
}

li {
  list-style: none;
}
</style>
