<template>
  <v-btn
    @click='parentFunction()'
    rounded="pill"
    color="black">
    <div class="text-center text-yellow">
      <h4>{{ text }}</h4>
    </div>
  </v-btn>
</template>

<script>
export default {
  name: 'NormalButton',
  props: {
    text: { type: String },
    parentFunction: { type: Function }
  }
}
</script>

<style scoped>

</style>
