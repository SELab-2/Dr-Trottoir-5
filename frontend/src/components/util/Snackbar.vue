<template>
  <v-snackbar
    v-model="open"
    :bottom="data.y === 'bottom'"
    :color="data.color"
    :left="data.x === 'left'"
    :multi-line="data.mode === 'multi-line'"
    :right="data.x === 'right'"
    :timeout="data.timeout"
    :top="data.y === 'top'"
    :vertical="data.mode === 'vertical'"
  >
    {{ data.message }}

    <v-spacer/>

    <v-btn text @click="close">
      close
    </v-btn>
  </v-snackbar>
</template>

<script lang="ts">
import {mapActions, mapState} from "vuex";
import {defineComponent} from "vue";

export default defineComponent({

  methods: {
    ...mapActions("snackbar", ["close"]),
  },
  computed: {
    ...mapState("snackbar", ["data"]),
    open: {
      /**
       * Get if the snackbar should be open.
       */
      get(): boolean {
        return this.$store.state.snackbar.open;
      },
      /**
       * Set if the snackbar should be open/closed.
       */
      set(value: boolean) {
        this.$store.commit("snackbar/SET_OPEN", value);
      }
    }
  }
})
</script>
