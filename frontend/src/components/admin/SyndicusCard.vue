<template>
  <v-container class="container-border" resizable="true">
    <v-row>
      <v-col cols="9">
        <v-row>
          <v-col>
            <p>{{ data.first_name }}</p>
          </v-col>
          <v-col>
            <p>{{ data.last_name }}</p>
          </v-col>
          <v-col>
            <p>{{ data.phone_nr }}</p>
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
            <p>{{ data.buildings }}</p>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="3" class="d-flex align-center justify-end">
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
import User from "@/api/models/User";
import router from "@/router";

/**
 * SyndicusCard component wordt gebruikt door als props een Object met de volgende keys mee te geven
 * firstName: String
 * secondName: String
 * mobileNumber: String
 * location: String
 * email: String
 * buildings: String
 */

export default {
  name: 'SyndicusCard',
  props: {
    data: {
      type: User,
    }
  },
  methods: {
    goToEditPage: function () {
      router.push({name: 'syndicus_adjust'})
    },
    deletePost: function () {
      router.push({name: 'admin_edit_user', params: {id: this.data.id}})
    }
  },
  components: {
    EditIcon,
    DeleteIcon
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
