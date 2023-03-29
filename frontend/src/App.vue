<template>
  <v-app>
    <StudentCard/>
  </v-app>
</template>

<script>

import StudentCard from '@/components/admin/StudentCard.vue'

export default {
  name: 'App',
  components: {
    StudentCard
  },
  data: () => ({
    //
  })
}
</script>
