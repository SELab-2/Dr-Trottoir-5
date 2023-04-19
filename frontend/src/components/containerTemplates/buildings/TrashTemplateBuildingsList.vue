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
import RoundBuildingCard from "@/components/admin/RoundBuildingCard.vue";
import BuildingHeader from "@/components/admin/BuildingHeader.vue";

export default {
  name: "TrashTemplateBuildingsList",
  components: {ListPage, RoundBuildingCard, BuildingHeader},
  props: {
    id: Number
  },
  data() {
    return {
      childComponent: RoundBuildingCard,
      elements: [],
      headComponent: BuildingHeader,
      keys: ['name', 'adres', 'manual']
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
