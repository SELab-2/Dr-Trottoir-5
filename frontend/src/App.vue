<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
    <NavigationBar v-if="navbar" />
    <snackbar/>
  </v-app>
</template>

<script lang="ts">

import {EchoError} from './api/EchoFetch/src/types/EchoError'
import {CustomErrorOptions} from './api/error/types/CustomErrorOptions'
import {defineComponent} from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'
import Snackbar from '@/components/util/Snackbar.vue'
import { useRouter } from 'vue-router'
const emitter = require('tiny-emitter/instance')

export default defineComponent({
  name: 'App',
  async beforeCreate() {
    const noLogin = ['login', 'register', 'register_done']; // Pages that can be accessed without logging in
    const router = useRouter();

    router.beforeEach(to => {
      console.log('Routing to:', to)
      if (!noLogin.includes(to.name.toString())) {
        this.navbar = true;

        // Authorize session
        this.$store.dispatch("session/fetch");
      } else this.navbar = false;
    });
  },
  mounted() {
    emitter.on(
      "error",
      (error: EchoError, options: CustomErrorOptions) => {
        if (options.style === "SNACKBAR") {
          this.$store.dispatch("snackbar/open", {
            message: error.message,
            color: "error"
          });
        }
      }
    )
  },
  components: {
    Snackbar,
    NavigationBar
  },
  data: () => ({
    navbar: false
  })
})
</script>
