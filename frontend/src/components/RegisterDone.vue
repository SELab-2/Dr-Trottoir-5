<!--
Component to be shown after a successful account registration.
This card component will display a clear success message with
additional information for the user that just registered.
-->

<template>
  <v-container align="center">
    <v-col cols="12" sm="6" md="6">
      <v-card class='px-4'>
        <v-card-title class="text-center">
          <v-icon
            color="success"
            icon="mdi-check-circle"
            size="x-large"
          ></v-icon>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-text>
          <v-row class="mx-auto justify-center">
            <div data-test="succes" class="mx-1">Registratie is gelukt!</div>
          </v-row>
          <v-row class="my-4 justify-center">
            <div data-test="thank-you" class="mx-1">Bedankt voor het registreren bij Dr. Trottoir.</div>
          </v-row>
          <v-row class="mb-4 justify-center">
            <div data-test="waiting" class="mx-1">Als uw aanmelding is verwerkt, zal de applicatie hier beschikbaar zijn.</div>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'RegisterDone'
})
</script>
