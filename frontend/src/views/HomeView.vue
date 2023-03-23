<template>
  <ListPage title="Gebouwen" />
</template>

<script>
import { defineComponent } from 'vue'

// Components
// import HelloWorld from '../components/HelloWorld.vue'
import ListPage from '@/components/ListPage'

export default defineComponent({
  name: 'HomeView',

  components: {
    ListPage
    // HelloWorld
  }
})
</script>
