<template>
  <ListPage title="Gebouwen" :head-component="ChildComponent" :child-component="ChildComponent" v-bind:elements="list" v-bind:terms="list.map((el) => el.name)"/>
</template>

<script>
import { defineComponent } from 'vue'

// Components
// import HelloWorld from '../components/HelloWorld.vue'
import NormalButton from '@/components/NormalButton'
import ListPage from '@/components/ListPage'

export default defineComponent({
  name: 'HomeView',

  components: {
    ListPage
    // HelloWorld
  },
  data () {
    return {
      ChildComponent: <NormalButton text="This is a button"/>,
      list: [
        { name: 'a' },
        { name: 'aa' },
        { name: 'aaa' },
        { name: 'av' }]
    }
  }
})
</script>
