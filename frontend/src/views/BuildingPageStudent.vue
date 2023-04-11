<template>

</template>

<script>
import { defineComponent } from 'vue';
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";

export default defineComponent({
  name: "BuildingPageStudent",
  async created() {
    if ('date' in this.$route.query) this.date = this.$route.query.date;
    if ('building' in this.$route.query) {
      const user = this.$store.getters['session/currentUser'];
      const id = await user.then(user => user.id).catch(() => null);
      if (!id) return;

      const planning = await RequestHandler.handle(PlanningService.get(id, this.date), {
        id: "getDayplanningError",
        style: "NONE"
      }).then(planning => planning).catch(() => null);
      if (!planning) return;

      const building_index = planning.ronde.buildings.findIndex(b => b.id == this.$route.query.building);
      const infos = await RequestHandler.handle(PlanningService.getInfo(planning.id), {
        id: "getBuildingInfoError",
        style: "NONE"
      }).then(info => info).catch(() => null);
      if (!infos) return;
      const info = infos[building_index];

      const pictures = await RequestHandler.handle(PlanningService.getPictures(info.id), {
        id: "getPicturesError",
        style: "NONE"
      }).then(picture => picture).catch(() => null);
      if (!pictures) return;

      console.log(planning, info, pictures);
      // Get infoperbuilding for this day + corresponding images
      // Get trashcontainers for this building and day and display as tasks
    }
  },
  data: () => ({
    date: new Date().toISOString().split('T')[0]
  })
});
</script>
