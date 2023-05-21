<template>
  <v-container class="border" resizable="true">
    <v-row>
      <v-col cols="9">
        <v-row>
          <v-col>
            <p>Voornaam</p>
          </v-col>
          <v-col>
            <p>Achternaam</p>
          </v-col>
          <v-col>
            <p>GSM</p>
          </v-col>
          <v-col>
            <p>Stad</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <p>email</p>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="3" class="d-flex align-center justify-end">
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'PersonHeader'
}
</script>

<style scoped>
  .border {
      border: 1px solid #E3e3e3;
  }
</style>
