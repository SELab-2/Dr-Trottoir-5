<template>
</template>

<script lang="ts">
import router from '@/router';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  async created() {
    const user = await this.$store.getters['session/currentUser'].catch(() => null);

    // Route user to a base based on his role
    switch (user.role) {
      case 'AA':
        return router.push({path: '/register_done'});
      case 'ST':
        return router.push({path: '/student_home'});
      case 'SY':
        return router.push({path: '/syndicus_home'});
      case 'AD':
      case 'SU':
        return router.push({path: '/admin_home'});
      case 'BE':
        return router.push({path: '/resident_home'});
    }

  }
});
</script>
