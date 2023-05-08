<template>
  <CreateEditPostStudent :data="data" />
</template>

<script>
import CreateEditPostStudent from '@/components/student/CreateEditPostStudent'

export default {
  name: 'StudentCreatePost',
  components: {
    CreateEditPostStudent
  },
  data: () => ({
    data: { buildingName: '', type: '', info: '', edit: false, planning: '' }
  }),
  created () {
    const buildingName = 'building' in this.$route.query ? this.$route.query.building : ''
    const type = 'type' in this.$route.query ? this.$route.query.type : ''
    const info = 'info' in this.$route.query ? this.$route.query.info : ''
    const planning = 'planning' in this.$route.query ? this.$route.query.planning : ''
    const buildingID = 'building_id' in this.$route.query ? this.$route.query.building_id : ''

    this.data = { buildingName: buildingName, type: type, info: info, edit: false, planning: planning, building_id: buildingID }
  }
}
</script>
