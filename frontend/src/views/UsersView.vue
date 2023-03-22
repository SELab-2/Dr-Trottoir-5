<template>
  <UsersList />
</template>

<script>
import { defineComponent } from 'vue'

// Components
import UsersList from '../components/UsersList.vue'

export default defineComponent({
  name: 'UsersView',

  components: {
    UsersList
  }
})
</script>
