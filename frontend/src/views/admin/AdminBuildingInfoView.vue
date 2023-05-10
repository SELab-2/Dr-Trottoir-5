<template>
  <AdminBuildingInfo :edit="false"></AdminBuildingInfo>
<!--  <BuildingFollowUp/>-->
</template>

<script>
import AdminBuildingInfo from "@/components/admin/AdminBuildingInfo";
import BuildingFollowUp from "@/components/admin/BuildingFollowUp.vue";

export default {
  name: "AdminBuildingInfoView",
  components: {BuildingFollowUp, AdminBuildingInfo}
}
</script>
