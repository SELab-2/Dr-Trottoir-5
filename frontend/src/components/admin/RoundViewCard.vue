<!--
This component is used in the admin and superstudent dashboard view,
it displays the information of one round so that a list of round views can easily be made
-->
<template>
  <v-container align="center" style="width: 80%;">
    <v-card>
      <v-row>
        <v-col align="left" class="ml-4 my-2" md="2" xs="12">
          <h5 class="text-h5 text-wrap font-weight-bold">Ronde {{data.round.ronde.name}}</h5>
        </v-col>
        <v-col align="left" md="2" class="my-3" xs="12">
          <p class="text-subtitle-1 font-weight-bold">{{data.date}}</p>
        </v-col>
        <v-col align="left" md="3" xs="10">
          <v-progress-linear color="green" :model-value="percentage" :height="20" class="my-4 mx-2" rounded="xl"
          style="width: 35vw; max-width: 100%;">
          </v-progress-linear>
        </v-col>
        <v-col align="left" md="1" xs="1" class="my-3 ml-4">
          <v-icon v-if="percentage === 100" icon="mdi-check" color="green" size="x-large"></v-icon>
        </v-col>
        <v-col align="center" md="2" xs="6" class="ml-3">
          <v-list>
            <v-list-group value="Student(en)">
              <template v-slot:activator="{ props }">
                <v-list-item rounded
                             v-bind="props"
                ><p class="text-wrap">Student(en)</p></v-list-item>
              </template>
              <v-list-item v-for="(student, i) in data.round.students" :key="i"
              ><p class="text-wrap">{{student.first_name}} {{student.last_name}}</p></v-list-item>
            </v-list-group>
          </v-list>
        </v-col>
        <v-col align="right" md="1" xs="2" class="my-3 mx-2">
          <v-icon icon="mdi-information-outline" size="x-large" @click="info"></v-icon>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "RoundViewCard",
  data: () => ({
    percentage: 100,
    users: []
  }),
  created() {
    this.percentage = this.data.round.status.filter(s => s === 'FI') / this.data.round.ronde.buildings.length;
  },
  props: {
    data: {
      type: Object,
      default: () => ({
        round: {ronde: {name: ''}},
        date: ''
      })
    }
  },
  methods: {
    info() {
      // TODO
    }
  }
}
</script>
