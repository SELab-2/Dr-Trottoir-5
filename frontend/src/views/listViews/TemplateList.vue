<template>
  <ListPage :add-function="() => {}" :child-component="childComponent" :elements="elements" title="Templates" :head-component="headComponent" />
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import TemplateMailCard from '@/components/admin/TemplateMailCard'
import TemplateMailCardHeader from '@/components/admin/TemplateMailCardHeader'
import {RequestHandler} from "@/api/RequestHandler";
import EmailTemplateService from "@/api/services/EmailTemplateService";

export default {
  name: 'TemplateList',
  components: { ListPage },
  data () {
    return {
      childComponent: TemplateMailCard,
      headComponent: TemplateMailCardHeader,
      elements: []
    }
  },
  beforeCreate() {
    RequestHandler.handle(EmailTemplateService.getEmailTemplates()).then(async result => {
      for (const el of result){
          this.elements.push({ titel: el.name, argsCount: 0 })
      }
    })
  }
}

</script>

<style scoped>

</style>
