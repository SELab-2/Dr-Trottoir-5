<template>
  <ListPage :add-function="addTrashContainerTemplate" :child-component="childComponent" :elements="elements"
            :head-component="headComponent"
            :keys="keys" title="Gebouwen voor deze vuilnis planning"/>
</template>

<script lang="ts">
import ListPage from '@/components/admin/ListPage.vue'
import {RequestHandler} from "@/api/RequestHandler";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import router from "@/router";
import TrashTemplateBuildingHeader from "@/components/containerTemplates/buildings/TrashTemplateBuildingHeader.vue";
import TrashTemplateBuildingCard from "@/components/containerTemplates/buildings/TrashTemplateBuildingCard.vue";

export default {
  name: "TrashTemplateBuildingsList",
  components: {ListPage, TrashTemplateBuildingHeader, TrashTemplateBuildingCard},
  props: {
    id: Number
  },
  data() {
    return {
      childComponent: TrashTemplateBuildingCard,
      elements: [],
      headComponent: TrashTemplateBuildingHeader,
      keys: ['name', 'address', 'manual']
    }
  },
  methods: {
    addTrashContainerTemplate: function () {
      router.push({path: '/trashtemplates/' + this.id + '/buildings/create'});
    }
  },
  async beforeMount() {
    await RequestHandler.handle(TrashTemplateService.getBuildingsOfTemplate(this.id), {
      id: 'getTrashBuildingsListError',
      style: 'SNACKBAR'
    }).then(async result => {
      this.elements = result
    })
  }
}
</script>

<style scoped>

</style>
