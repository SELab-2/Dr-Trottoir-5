<!--
Component to be shown after a successful account registration.
This card component will display a clear success message with
additional information for the user that just registered.
-->

<template>
  <trash-container-template-list/>
</template>

<script>
import TrashContainerTemplateList from '@/components/containerTemplates/TrashContainerTemplateList.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'RegisterDone',
  components: { TrashContainerTemplateList }
})
</script>
