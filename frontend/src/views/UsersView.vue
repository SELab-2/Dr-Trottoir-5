<template>
  <h3>{{JSON.stringify(users)}}</h3>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue'
import { request } from '@/authorized'

/*
 view is just for testing purposes, will be removed
*/

export default defineComponent({
  name: 'UsersView',
  setup () {
    const users = ref([])
    onMounted(async () => {
      users.value = await request('/api/users', 'GET')
    })
    return { users }
  }
})
</script>
