<template>
  <ListPage :add-function="() => {}" :elements="[{ name: 'Alpha', argsCount: 2 }]" :child-component="childComponent" title="Gebouwen"/>
</template>

<script>
import { defineComponent } from 'vue'
// Components
// import HelloWorld from '../components/HelloWorld.vue'
import ListPage from '@/components/ListPage'
import TemplateMailCard from '@/components/admin/TemplateMailCard'
export default defineComponent({
  name: 'HomeView',
  components: {
    // HelloWorld
    ListPage
  },
  data () {
    return {
      childComponent: TemplateMailCard
    }
  }
})
</script>
