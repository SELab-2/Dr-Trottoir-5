<!--
Need to use the component as following.
Define a function in the methods of the parent component
and call it in the v-bind:parent-function argument.
The button also takes a text with the text that you want to show.
You also can use parentFunction instead of parent-function.

In following example inc is a function defined in methods.
<NormalButton text="This is a button" v-bind:parent-function="inc"/>

!!! Don't put end brackets because then it will work with the return value. So not inc() !!!!
-->

<template>
  <v-btn
    @click='parentFunction()'
    rounded="pill"
    color="primary"
  >
    <div
      class="text-center text-secondary"
      :class="[{'text-h6': /[a-z0-9]/i.test(text)}, 'text-h5']"
    >
      <p >{{ text }}</p>
    </div>
    <div v-if="this.dropdown">
      <v-icon right color="secondary">mdi-menu-down</v-icon>
    </div>
  </v-btn>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'NormalButton',
  props: {
    text: { type: String },
    dropdown: { type: Boolean, default: false },
    parentFunction: { type: Function, default: () => null }
  }
})
</script>

<style scoped>

</style>
