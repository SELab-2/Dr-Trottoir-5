<template>
  <v-dialog
    v-model="open"
    :fullscreen="modalData.fullscreen"
    :max-width="modalData.width"
    :transition="
            modalData.fullscreen
                ? 'dialog-bottom-transition'
                : 'dialog-transition'
        "
  >
    <!-- Other -->
    <v-card>
      <!-- Component -->
      <component
        :is="component"
        v-if="modalData.component"
        :action="modalData.action"
        :payload="modalData.componentPayload"
      />
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { mapActions, mapState } from 'vuex'
import { ModalData } from '@/store/modules/modal'
import LoadingModal from '../modal/LoadingModal.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'modalComponent',
  methods: {
    ...mapActions('modal', ['close'])
  },
  computed: {
    ...mapState('modal', ['data']),

    modalData: {
      /**
       * Get the data for the modal.
       */
      get (): ModalData {
        // Create a clone of the object to prevent Vue from mutating the data from store directly.
        return Object.assign({}, this.$store.state.modal.data)
      },
      /**
       * Set the data for the modal
       */
      set (value: ModalData) {
        this.$store.commit('modal/SET_DATA', value)
      }
    },
    open: {
      /**
       * Get if the snackbar should be open.
       */
      get (): boolean {
        return this.$store.state.modal.open
      },

      /**
       * Set if the snackbar should be open/closed.
       */
      set (value: boolean) {
        this.$store.commit('modal/SET_OPEN', value)
      }
    },
    component: {
      /**
       * Get the component.
       */
      get (): unknown | Function {
        if (this.$store.state.modal.data.component instanceof Promise) {
          return () => ({
            component: this.$store.state.modal.data.component(),
            loading: LoadingModal
          })
        } else {
          return this.$store.state.modal.data.component
        }
      },

      set (component: unknown | Function) {
        /* Needed but never used */
      }
    }
  }
})
</script>
