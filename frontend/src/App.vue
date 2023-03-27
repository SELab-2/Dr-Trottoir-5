<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
    <NavigationBar/>
    <snackbar/>
  </v-app>
</template>

<script lang="ts">

import {EchoError} from './api/EchoFetch/src/types/EchoError'
import {CustomErrorOptions} from './api/error/types/CustomErrorOptions'
import {onMounted} from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'
import Snackbar from "@/components/util/Snackbar.vue";

const Emitter = require('tiny-emitter')
const emitter = new Emitter() //error bus


export default {
  name: 'App',

  beforeCreate() {
    // Fetch the session data.
    this.$store.dispatch("session/fetch");
  },

  setup() {
    onMounted(async () => {


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
    })
  },
  components: {
    Snackbar,
    NavigationBar
  },
  data: () => ({
    //
  })
}
</script>
