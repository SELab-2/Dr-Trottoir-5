<template>
  <h3>wtfffff</h3>
  <h3>{{JSON.stringify(users)}}</h3>
</template>

<script>
import { request } from '@/authorized'
import { onMounted, ref } from 'vue'

export default {
  name: 'UsersList',
  setup () {
    const users = ref([])
    onMounted(async () => {
      users.value = await request('/api/users', 'GET')
      console.log(users.value)
    })
    return { users }
  }
}
</script>

<style scoped>

</style>
