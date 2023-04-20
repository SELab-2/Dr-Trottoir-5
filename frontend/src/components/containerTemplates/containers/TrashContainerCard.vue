<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p class="text-style-title">{{ this.data.trash_container.collection_day.day }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{
            this.data.trash_container.collection_day.start_hour + ' - ' + this.data.trash_container.collection_day.end_hour
          }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{ this.data.trash_container.type.toString() }}</p>
      </v-col>
      <v-col cols="4"/>
      <v-col class="text-right" cols="1">
        <v-btn class="button-style" icon v-on:click="editContainer">
          <EditIcon/>
        </v-btn>
      </v-col>
      <v-col class="text-right" cols="1">
        <v-btn class="button-style" icon v-on:click="deleteContainer">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import EditIcon from '@/components/icons/EditIcon.vue'
import router from '@/router'

export default {
  name: 'TrashContainerCard',
  components: {EditIcon, DeleteIcon},
  props: {
    data: {
      default: Object(),
    },
  },
  data: () => ({
    id: null
  }),
  methods: {
    editContainer: function () {
      router.push({
        path: '/trashtemplates/' + this.id + '/containers/' + this.data.extra_id + '/edit'
      });
    },
    deleteContainer: function () {
      //todo
    },
  },
  async beforeMount() {
    this.id = this.$route.params.id
  }
}
</script>

<style scoped>
.text-style-title {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
