<!--
Needs to get a data object with a name and then three int values as time in minutes
The time automatically will shown as the "hh:mm" format
-->

<template>
  <v-container class="container-border align-center">
    <v-row align="stretch">
      <v-col cols="3"  class="column" >
        <p>{{ this.args.name }}</p>
      </v-col>
      <v-col cols="3" class="column">
        <p>{{ time1 }}</p>
      </v-col>
      <v-col cols="3" class="column">
        <p>{{ time2 }}</p>
      </v-col>
      <v-col cols="3" class="column">
        <p>{{ time3 }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import { toTimeString } from '@/util/TimeUtil.ts'

export default {
  name: 'StudentReviewCard',
  props: {
    args: {
      default: {
        name: 'name',
        first: 0,
        second: 0,
        third: 0
      }
    }
  },
  computed: {
    time1 () {
      return toTimeString(this.args.first)
    },
    time2 () {
      return toTimeString(this.args.second)
    },
    time3 () {
      return toTimeString(this.args.third)
    }
  }
}
</script>

<style scoped>
.container-border{
  border: 1px solid #E3e3e3;
  border-radius: 25px;
}

.column{
  display: flex;
  align-content: center;
  justify-content: center;
  text-align: center;
}

</style>
