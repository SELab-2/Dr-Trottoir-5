<template>
  <v-container align="center">
    <v-col cols="12" sm="6" md="6">
      <v-card class='px-4'>
        <v-card-title class="text-center">
          <v-icon
            color="error"
            icon="mdi-cancel"
            size="x-large"
          ></v-icon>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-text>
          <v-row class="mx-auto justify-center">
            <div class="mx-1">Geen toegang!</div>
          </v-row>
          <v-row class="my-4 justify-center">
            <div class="mx-1">U heeft onvoldoende rechten om deze pagina te bezoeken.</div>
          </v-row>
          <v-row class="my-4 justify-center">
            <normal-button text="Ga terug" v-bind:parent-function="goBack" block class="mt-2"></normal-button>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import NormalButton from '@/components/NormalButton'
import router from '@/router'

export default {
  name: 'UnauthorizedComponent',
  components: { NormalButton },
  methods: {
    goBack () {
      router.back()
    }
  }
}
</script>
