<template>
  <v-app>
    <BuildingCard/>
  </v-app>
</template>

<script>

import BuildingCard from '@/components/admin/BuildingCard.vue'

export default {
  name: 'App',
  components: {
    BuildingCard
  },
  data: () => ({
    //
  })
}
</script>
