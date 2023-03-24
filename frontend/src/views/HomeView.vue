<template>
  <RoundBuildingCard />
</template>

<script>
import { defineComponent } from 'vue'

// Components
import RoundBuildingCard from '../components/admin/RoundBuildingCard.vue'

export default defineComponent({
  name: 'HomeView',

  components: {
    RoundBuildingCard
  }
})
</script>
