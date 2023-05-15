<template>
  <ListPage :add-function="addTrashContainerTemplate" :child-component="childComponent" :elements="elements"
            :head-component="headComponent"
            :keys="keys" title="Vuilnis plannings"/>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import TrashContainerTemplateCard from "@/components/containerTemplates/TrashContainerTemplateCard.vue";
import TrashContainerTemplateHeader from "@/components/containerTemplates/TrashContainerTemplateHeader.vue";
import ListPage from "@/components/admin/ListPage.vue";

export default {
  name: 'TrashContainerTemplateList',
  components: {ListPage},
  data() {
    return {
      childComponent: TrashContainerTemplateCard,
      elements: [],
      headComponent: TrashContainerTemplateHeader,
      keys: ['name', 'year', 'week', 'location']
    }
  },
  methods: {
    addTrashContainerTemplate: function () {
      router.push({name: 'createTrashtemplates'});
    }
  },
  async beforeMount() {
    await RequestHandler.handle(TrashTemplateService.getTrashTemplates(), {
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
