<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p class="text-style-title">{{ this.data.day }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{ this.data.start_hour + ' - ' + this.data.end_hour }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{ this.data.type }}</p>
      </v-col>
      <v-col cols="2"/>
      <v-col class="text-right" cols="2">
        <v-btn class="button-style" icon v-on:click="editContainer">
          <EditIcon/>
        </v-btn>
      </v-col>
      <v-col class="text-right" cols="2">
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
import Container from "@/api/models/Container";

export default {
  name: 'TrashContainerCard',
  components: {EditIcon, DeleteIcon},
  props: {
    data: {
      type: Container,
      default: () => (new Container())
    }
  },
  data: () => ({
  }),
  methods: {
    editContainer: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/containers/edit', params: {//TODO add to router
          toEdit: this.data // TODO deze pagina maken
        }
      });
    },
    deleteContainer: function () {
      //todo
    },
    goToTrashTemplateBuildingsPage: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/buildings', params: {
          trashTemplate: this.data // TODO deze pagina maken
        }
      });
    },
    goToTrashTemplateContainersPage: function () {
      router.push({
        path: '/trashtemplates/' + this.data.id + '/containers', params: {
          trashTemplate: this.data // TODO deze pagina maken
        }
      })
    }
  },
  async beforeMount() {

  }
}
</script>

<style scoped>
.text-style-title {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
