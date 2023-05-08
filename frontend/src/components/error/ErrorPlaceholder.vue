<template>
  <div>
    <!-- Fullpage error -->
    <v-container v-if="displayFullPage && renderError">
      <v-row justify="center">
        <v-col cols="12" md="6">
          <component
            :is="errorComponent"
            v-if="renderError"
            :payload="errorComponentPayload"
          />
        </v-col>
      </v-row>
    </v-container>

    <!-- Regular error -->
    <div v-else>
      <component
        :is="errorComponent"
        v-if="renderError"
        :payload="errorComponentPayload"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { EchoError } from 'echofetch'
import { CustomErrorOptions } from '@/api/error/types/CustomErrorOptions'
import { ErrorComponentPayload } from '@/api/error/types/component/ErrorComponentPayload'
import ErrorCard from '@/components/error/placeholders/ErrorCard.vue'
import ErrorSection from '@/components/error/placeholders/ErrorSection.vue'
import { ErrorHandler } from '@/api/error/ErrorHandler'
import { defineComponent } from 'vue'

const emitter = require('tiny-emitter/instance')

export default defineComponent({

  name: 'ErrorPlaceholder',
  props: {
    errorId: {
      /**
       * Identifier of the error that should be displayed.
       * All errors with the given identifier will be displayed.
       */
      type: String
    },
    displayFullPage: {
      /**
       * If the error should be displayed when "displayFullPage" is true.
       */
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    /**
     * Should the error component be rendered.
     */
    renderError: false,

    /**
     *  Component to display when an error occurs.
     */
    errorComponent: null,

    /**
     * Payload to pass to the error component.
     */
    errorComponentPayload: ErrorComponentPayload
  }),
  mounted () {
    // Create a listener that will show an error when it is spawned.
    emitter.$on(
      'error',
      (error: EchoError, options: CustomErrorOptions) => {
        // Check if the error should be rendered.
        if (options.id === this.errorId || (this.displayFullPage && options.displayFullpage)) {
          // Get the component to display for the error.
          if (options.style === 'CARD') {
            this.errorComponent = ErrorCard
          } else if (options.style === 'SECTION') {
            this.errorComponent = ErrorSection
          }

          // Apply the custom error messages to the error object.
          error.message = ErrorHandler.getCustomMessage(
            error,
            options
          )

          this.errorComponentPayload = {
            error,
            description: ErrorHandler.getCustomDescription(
              error,
              options
            ),
            options
          }

          this.renderError = true
        }
      }
    )

    // Clear the error when a "error-clear" event is send.
    emitter.$on('error-clear', () => {
      this.renderError = false
    })
  }
})
</script>
