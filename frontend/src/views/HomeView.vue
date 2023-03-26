<template>
  <ListPage title="Gebouwen" :head-component="Headcomponent" :child-component="ChildComponent" v-bind:elements="list"/>
</template>

<script>
import { defineComponent } from 'vue'

// Components
// import HelloWorld from '../components/HelloWorld.vue'
import NormalButton from '@/components/NormalButton'
import ListPage from '@/components/ListPage'
import TemplateMailCard from '@/components/admin/TemplateMailCard'

export default defineComponent({
  name: 'HomeView',

  components: {
    ListPage
    // HelloWorld
  },
  data () {
    return {
      Headcomponent: <NormalButton text="This is a button"/>,
      ChildComponent: <TemplateMailCard/>,
      list: [
        { name: 'alpha', argsCount: 0 },
        { name: 'beta', argsCount: 1 },
        { name: 'gamma', argsCount: 2 },
        { name: 'delta', argsCount: 3 },
        { name: 'epsilon', argsCount: 4 },
        { name: 'dzeta', argsCount: 5 }
      ]
    }
  }
})
</script>
