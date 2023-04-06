<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-row class="pa-5 row">
          <h2>{{ data.title }}</h2>
          <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="editRound">
            <EditIcon/>
          </v-btn>
          <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deleteRound">
            <DeleteIcon/>
          </v-btn>
        </v-row>
      </v-col>
      <v-col cols="12" class="col">
        <BuildingHeader :round="true"/>
      </v-col>
      <v-col/>
      <v-col cols="12" class="col">
        <ul>
          <li v-for="(el) in filteredOptions" :key="el">
            <RoundBuildingCard v-bind:data="el"/>
            <v-col/>
          </li>
        </ul>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>

import EditIcon from '@/components/icons/EditIcon.vue'
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import RoundBuildingCard from '@/components/admin/RoundBuildingCard'
import BuildingHeader from '@/components/admin/BuildingHeader'

export default {
  name: 'BuildingList',
  components: { BuildingHeader, RoundBuildingCard, EditIcon, DeleteIcon },
  props: {
    data: {
      title: {type: String, default: 'Ronde X'},
      buildings: {type: Array, default: () => []}
    },
    keyValue: { type: String, default: 'title' },
    searched: { type: String, default: '' }
  },
  methods: {
    deleteRound () {
      // TODO
    },
    editRound () {
      // TODO
    }
  },
  computed: {
    filteredOptions () {
      console.log(this.keyValue)
      console.log(this.searched)
      if (this.keyValue !== 'title'){
        const filtered = []
        const regex = new RegExp(this.searched, 'ig')
        for (const el of this.data.buildings) {
          if (this.searched.length < 1 || el[this.keyValue].toString().match(regex)) {
            filtered.push(el)
          }
        }
        return filtered
      } else {
        return this.data.buildings
      }
    }
  },
}
</script>

<style scoped>
  ul { list-style-type: none; }

  .col {
    padding-left: 50px;
  }

  .row {
    column-gap: 15px;
  }

</style>
