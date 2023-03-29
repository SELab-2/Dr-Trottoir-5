<template>
  <v-container class="container-border align-center">
    <v-row align="stretch">
      <v-col cols="3"  class="column" >
        <p>{{ this.args.name }}</p>
      </v-col>
      <v-col cols="3" class="column">
        <p>{{ this.args.first }}</p>
      </v-col>
      <v-col cols="3" class="column">
        <p>{{ this.args.second }}</p>
      </v-col>
      <v-col cols="3" class="column">
        <p>{{ this.args.third }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'TrashPickupCard',
  props: {
    args: {
      default: {
        name: 'name',
        first: 'Own time',
        second: 'Average time',
        third: 'Last time'
      }
    }
  }
}
</script>

<style scoped>
.container-border{
  border: 1px solid #E3e3e3;
}

.column{
  display: flex;
  align-content: center;
  justify-content: center;
  text-align: center;
  margin-top:5px;
  margin-bottom: 5px;
}

</style>
