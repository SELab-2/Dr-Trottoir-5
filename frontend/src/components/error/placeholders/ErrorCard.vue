<template>
  <v-card
    :class="`error-card ${
            payload.options.displayFullpage ? 'text-center' : ''
        }`"
  >
    <!-- Image (only if fullscreen) -->
    <div v-if="payload.options.displayFullpage" class="error-card__image">
      <v-img height="100%" src="@/assets/img/error.svg" contain/>
    </div>

    <!-- Message -->
    <v-card-title class="error-card__message">
      {{ payload.error.message }}
    </v-card-title>

    <!-- Description -->
    <v-card-text class="error-card__description">
      {{ payload.description }}
    </v-card-text>

    <!-- Home button (only if fullscreen) -->
    <v-card-actions class="error-card__actions">
      <v-btn color="primary" depressed to="/">
        Home Page
        <v-icon right>mdi-home</v-icon>
      </v-btn>

      <v-btn depressed @click="reloadRoute($router)">
        Refresh
        <v-icon right>mdi-refresh</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import {RouterUtil} from "@/util/RouterUtil";
import {ErrorComponentPayload} from "@/api/error/types/component/ErrorComponentPayload";
import { defineComponent } from 'vue'

export default defineComponent({

  name: 'ErrorCard',
  props: {
    payload: {
      /**
       * Payload of the error.
       */
      type: ErrorComponentPayload
    }
  },

  methods: {
    /**
     * Reload the current route.
     */
    reloadRoute() {
      RouterUtil.reload(this.$router);
    }
  }

})
</script>

<style lang="scss" scoped>
.error-card {
  padding: 20px;

  &__image {
    height: 150px;
    width: 100%;
    margin-bottom: 50px;
  }

  &__actions {
    display: flex;
    justify-content: center;
    margin-top: 50px;
  }

  &__message {
    font-size: 1.9em;
    padding-bottom: 20px;
    text-wrap: normal;
  }

  &__description {
    font-size: 1.1em;
  }
}
</style>
