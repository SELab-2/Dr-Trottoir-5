<template>
  <v-container class="container-border" resizable="true">
    <v-row>
      <v-col cols="9">
        <v-row>
          <v-col>
            <p>{{ data.firstName }}</p>
          </v-col>
          <v-col>
            <p>{{ data.secondName }}</p>
          </v-col>
          <v-col>
            <p>{{ data.mobileNumber }}</p>
          </v-col>
          <v-col>
            <p>{{ data.location }}</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <p>{{ data.email }}</p>
          </v-col>
          <v-col>
            <p>{{ data.rounds }}</p>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="3" class="d-flex align-center justify-end">
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToInfoPage">
          <InfoIcon/>
        </v-btn>
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
          <EditIcon/>
        </v-btn>
        <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import EditIcon from '@/components/icons/EditIcon.vue'
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import InfoIcon from '@/components/icons/InfoIcon.vue'

/**
 * StudentCard component wordt gebruikt door als props een Object met de volgende keys mee te geven
 * firstName: String
 * secondName: String
 * mobileNumber: String
 * location: String
 * email: String
 * rounds: String
 */

export default {
  name: 'StudentCard',
  props: {
    data: {
      type: Object,
      default: () => ({ firstName: 'Empty', secondName: 'Empty', mobileNumber: '0123456789', location: 'Empty', email: 'Empty', rounds: 'Empty' })
    }
  },
  methods: {
    goToEditPage: function () {
      // TODO
    },
    deletePost: function () {
      // TODO
    },
    goToInfoPage: function () {
      // TODO
    }
  },
  components: {
    EditIcon,
    DeleteIcon,
    InfoIcon
  }
}
</script>

<style scoped>
p {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
