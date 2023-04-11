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
import config from "@/config";
const emitter = require('tiny-emitter/instance')

export default defineComponent({
  name: 'App',
  async beforeCreate() {
    const noLogin = ['login', 'register', 'forgot'];  // Pages that can be accessed without logging in
    const router = useRouter();

    router.beforeEach( async (to, from, next) => {
      const needsLogin = !noLogin.includes(to.name.toString());
      // Authorize session
      await this.$store.dispatch("session/fetch", {
        needsLogin: needsLogin
      });
      // Check if user is logged in
      const user = await this.$store.getters['session/currentUser'].catch(() => null);

      if (needsLogin) {
        if (user === null) return next({path: '/login'});
        this.navbar = true;

        if (!(config.AUTHORIZED[user.role].includes(to.name.toString()))) {
         return next({path: '/unauthorized'});
        }
      } else {
        if (user !== null) {
          this.navbar = true;
          return next({path: '/'});
        }
        this.navbar = false;
      }

      next();
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
