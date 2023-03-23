<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <NavigationBar/>
      </v-col>
      <v-col cols="12">
        <v-row align="start" class="pa-5">
            <h1>{{ title }}</h1>
          <v-row></v-row>
            <NormalButton text="+"/>
        </v-row>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import NormalButton from '@/components/NormalButton'
export default {
  name: 'ListPage',
  components: { NormalButton },
  props: {
    title: { type: String, default: '' }
  }
}
</script>

<style scoped>

</style>
