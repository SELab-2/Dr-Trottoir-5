<template>
  <CreateEditPostStudent :data="data" />
</template>

<script>
import CreateEditPostStudent from "@/components/student/CreateEditPostStudent";

export default {
  name: "StudentEditPost",
  components: {
    CreateEditPostStudent
  },
  data: () => ({
    data: {buildingName: '', type: '', info: '', edit: false, id: ''}
  }),
  created() {
    const buildingName = 'building' in this.$route.query ? this.$route.query.building : '';
    const type = 'type' in this.$route.query ? this.$route.query.type : '';
    const info = 'info' in this.$route.query ? this.$route.query.info : '';
    const id = 'id' in this.$route.query ? this.$route.query.id : '';

    this.data = {buildingName: buildingName, type: type, info: info, edit: true, id: id};
  }
}
</script>
