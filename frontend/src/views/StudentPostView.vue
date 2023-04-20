<template>
  <OverviewScreenStudentPosts :data="data" />
</template>

<script>
import {defineComponent} from "vue";
import OverviewScreenStudentPosts from "@/components/student/OverviewScreenStudentPosts";
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import RoundService from "@/api/services/RoundService";

export default defineComponent({
  name: "StudentPostView",
  components: {
    OverviewScreenStudentPosts
  },
  data: () => ({
    data: {images: [], type: '', buildingName: '', info: '', planning: ''}
  }),
  async created() {
    if (!('building' in this.$route.query)) return;
    if (!('type' in this.$route.query)) return;
    if (!('planning' in this.$route.query)) return;
    const typeMap = {Extra: 'EX', Aankomst: 'AR', Vertrek: 'DE', Berging: 'ST'};
    if ('info' in this.$route.query) {
      const images = await RequestHandler.handle(PlanningService.getPictures(this.$route.query.info), {
        id: "getPicturesError",
        style: "NONE"
      }).then(pictures => pictures.filter(p => p.pictureType === typeMap[this.$route.query.type])).catch(() => null);
      if (!images) return;

      const building = await RequestHandler.handle(RoundService.getBuilding(this.$route.query.building), {
        id: "getBuildingError",
        style: "NONE"
      }).then(b => b).catch(() => null);
      if (!building) return;

      this.data = {
        images: images, type: this.$route.query.type, buildingName: building.name, info: this.$route.query.info,
        planning: this.$route.query.planning, building_id: building.id
      };
    }
  }
});
</script>
