<template>
  <v-card>
    <v-card-title>
      {{ payload.title }}

      <v-spacer/>

      <v-btn icon @click="close">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-card-title>

    <v-card-text v-html="payload.message"/>

    <v-card-actions>
      <v-spacer/>

      <!-- Ok -->
      <v-btn color="primary" depressed @click="close">
        Ok
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    /**
     * Payload, passed when opening the modal.
     */
    payload: {
      type: {
        title: String,
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
    }
  }
})
</script>
