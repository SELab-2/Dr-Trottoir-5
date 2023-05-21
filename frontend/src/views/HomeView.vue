<template>
  <v-card align="center">
    <v-card-text>
      <h3 class="text-h3">U wordt doorverwezen..</h3>
    </v-card-text>
  </v-card>
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
        return router.push({name: 'register_done'});
      case 'ST':
        return router.push({name: 'student_home'});
      case 'SY':
        return router.push({name: 'syndicus_home'});
      case 'AD':
      case 'SU':
        return router.push({name: 'admin_home'});
      case 'BE':
        return router.push({name: 'resident_home'});
    }

  }
});
</script>
