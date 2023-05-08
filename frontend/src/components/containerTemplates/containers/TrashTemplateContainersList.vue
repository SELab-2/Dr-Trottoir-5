<template>
  <ListPage :add-function="addTrashContainerTemplate" :child-component="childComponent" :elements="elements"
            :head-component="headComponent"
            :search="false"
            title="Containers voor deze vuilnis planning"/>
</template>

<script lang="ts">
import ListPage from '@/components/admin/ListPage.vue'
import {RequestHandler} from "@/api/RequestHandler";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import TrashContainerCard from "@/components/containerTemplates/containers/TrashContainerCard.vue";
import TrashContainerHeader from "@/components/containerTemplates/containers/TrashContainerHeader.vue";

export default {
  name: "TrashTemplateContainersList",
  components: {ListPage, TrashContainerCard, TrashContainerHeader},
  props: {
    id: Number
  },
  data() {
    return {
      childComponent: TrashContainerCard,
      elements: [],
      headComponent: TrashContainerHeader
    }
  },
  methods: {
    addTrashContainerTemplate: function () {
      router.push({name: 'createTrashtemplateContainers', params: {id: this.id}});
    }
  },
  async beforeMount() {
    await RequestHandler.handle(TrashTemplateService.getTrashContainersOfTemplate(this.id), {
      id: 'getTrashContainersListError',
      style: 'SNACKBAR'
    }).then(async result => {
      this.elements = result
    })
  }
}
</script>

<style scoped>

</style>
