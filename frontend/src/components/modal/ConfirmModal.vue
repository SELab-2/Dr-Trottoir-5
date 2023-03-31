<template>
  <v-card>
    <v-card-title>
      Are you sure?

      <v-spacer/>

      <v-btn icon @click="close">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-card-title>

    <v-card-text v-html="payload.message"/>

    <v-card-actions>
      <v-spacer/>

      <!-- Cancel -->
      <v-btn color="error" text @click="close">
        Cancel
      </v-btn>

      <!-- Confirm -->
      <v-btn
        :disabled="loading"
        :loading="loading"
        color="primary"
        depressed
        @click="confirm"
      >
        Confirm
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

import Vue, { defineComponent } from "vue";

export default defineComponent({

  props: {
    /**
     * Payload, passed when opening the modal.
     */
    payload: {
      type: {
        action: Function,
        message: String
      }
    }
  },
  methods: {
    /**
     * Close the modal.
     */
    close() {
      this.$store.dispatch("modal/close");
    },
    /**
     * Execute the confirm action.
     */
    confirm() {
      this.payload.action(this);
    }
  },
  data() {
    /**
     * If the confirm model is loading.
     */
    return { loading: false }
  }
})
</script>
