<template>
<CreateEditMailTemplate :edit="true"/>
</template>

<script>
import CreateEditMailTemplate from "@/components/admin/mail/CreateEditMailTemplate.vue";

export default {
  name: 'AdminMailTemplateView',
  components: {CreateEditMailTemplate}
}
</script>

<style scoped>

</style>
