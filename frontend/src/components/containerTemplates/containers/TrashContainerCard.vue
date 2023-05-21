<template>
  <v-container class="container-border">
    <v-row align="center" justify="center">
      <v-col cols="2">
        <p>{{ Weekday[weekday_from_api(this.data.trash_container.collection_day.day)] }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{
            this.data.trash_container.collection_day.start_hour + ' - ' + this.data.trash_container.collection_day.end_hour
          }}</p>
      </v-col>
      <v-col cols="2">
        <p>{{ ContainerType[container_from_api(this.data.trash_container.type)] }}</p>
      </v-col>
      <v-col cols="4"/>
      <v-col class="text-right" cols="1">
        <v-btn data-test="edit" class="button-style" icon v-on:click="editContainer">
          <EditIcon/>
        </v-btn>
      </v-col>
      <v-col class="text-right" cols="1">
        <v-btn data-test="delete" class="button-style" icon v-on:click="deleteContainer">
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
import {container_from_api, ContainerType} from "@/api/models/ContainerType";
import Container from "@/api/models/Container";
import {Weekday, weekday_from_api} from "@/api/models/Weekday";
import trashTemplateService from "@/api/services/TrashTemplateService";
import {RequestHandler} from "@/api/RequestHandler";

export default {
  name: 'TrashContainerCard',
  computed: {
    Weekday() {
      return Weekday
    },
    ContainerType() {
      return ContainerType
    }
  },
  components: {EditIcon, DeleteIcon},
  props: {
    data: {
      default: Object(),
      type: Container
    },
  },
  data: () => ({
    id: null
  }),
  methods: {
    container_from_api,
    weekday_from_api,
    editContainer: function () {
      router.push({
        name: 'editTrashtemplateContainers',
        params: {id: this.id, containerId: this.data.extra_id}
      });
    },
    async deleteContainer() {
      await RequestHandler.handle(trashTemplateService.deleteContainerFromTemplate(this.id, this.data.extra_id), {
        id: 'deleteContainerFromTemplateError',
        style: 'SNACKBAR'
      }).then(() => null).catch(() => null);
      window.location.reload()
    },
  },
  async beforeMount() {
    this.id = this.$route.params.id
  }
}
</script>
