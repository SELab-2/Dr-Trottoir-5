<template>
  <ListPage :add-function="addMethod" :child-component="childComponent" :elements="elements" title="Email Templates" :head-component="headComponent" :keys="keys" :map-keys="mapKeys"/>
</template>

<script>
import ListPage from '@/components/admin/ListPage'
import TemplateMailCard from '@/components/admin/TemplateMailCard'
import TemplateMailCardHeader from '@/components/admin/TemplateMailCardHeader'
import {RequestHandler} from "@/api/RequestHandler";
import EmailTemplateService from "@/api/services/EmailTemplateService";
import router from "@/router";

export default {
  name: 'TemplateList',
  components: { ListPage },
  data () {
    return {
      childComponent: TemplateMailCard,
      headComponent: TemplateMailCardHeader,
      elements: [],
      keys: ['name'],
      mapKeys: {'name': 'naam'}
    }
  },
  methods: {
    addMethod: function () {
      router.push({ name: 'create_mail-template' })
    }
  },
  async beforeMount() {
    await RequestHandler.handle(EmailTemplateService.getEmailTemplates(), {id: 'getEmailTemplatesError', style: 'SNACKBAR'}).then(async result => {
      this.elements = result
    })
  }
}

</script>

<style scoped>

</style>
