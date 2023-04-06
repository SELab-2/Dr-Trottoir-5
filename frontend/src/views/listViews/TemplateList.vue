<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Templates" :head-component="headComponent" />
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import TemplateMailCard from '@/components/admin/TemplateMailCard'
import TemplateMailCardHeader from '@/components/admin/TemplateMailCardHeader'

export default {
  name: 'TemplateList',
  components: { ListPage },
  data () {
    return {
      childComponent: TemplateMailCard,
      elements: [
        { name: 'Template 1', argsCount: 3 },
        { name: 'Template 2', argsCount: 2 },
        { name: 'Template 3', argsCount: 1 }
      ],
      headComponent: TemplateMailCardHeader
    }
  }
}

</script>

<style scoped>

</style>
