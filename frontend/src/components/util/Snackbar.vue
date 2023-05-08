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
    <div class="mb-3">
      {{ data.message }}
    </div>

    <v-spacer/>

    <NormalButton :text="'sluiten'" :parent-function="close"/>
  </v-snackbar>
</template>

<script lang="ts">
import { mapActions, mapState } from 'vuex'
import { defineComponent } from 'vue'
import NormalButton from '@/components/NormalButton.vue'

export default defineComponent({
  name: 'snackbarComponent',
  components: { NormalButton },
  methods: {
    ...mapActions('snackbar', ['close'])
  },
  computed: {
    ...mapState('snackbar', ['data']),
    open: {
      /**
       * Get if the snackbar should be open.
       */
      get (): boolean {
        return this.$store.state.snackbar.open
      },
      /**
       * Set if the snackbar should be open/closed.
       */
      set (value: boolean) {
        this.$store.commit('snackbar/SET_OPEN', value)
      }
    }
  }
})
</script>
