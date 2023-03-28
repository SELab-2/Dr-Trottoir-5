<!--
  Een component die een een overzicht geeft hoe ver een ronde al in proces is. Als input verwachten we
  een data object die alle nodige informatie bevat.
    Name: String
    Datum: String
    Progress: Int range: 0-100
    plannend: Bool
    students: [String]
-->

<template>
  <v-container :class="`container-border ${!data.planned ? 'container-height d-flex align-center justify-center'  : ''}`">
    <v-row>
      <v-col cols="3" class="d-flex align-center justify-start">
        <b>Ronde {{ data.name }}</b>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <b>{{ data.datum }}</b>
      </v-col>
      <v-col v-if="data.planned" cols="2" class="d-flex align-center">
        <v-progress-linear height="7" rounded color="info" :model-value="data.progress"></v-progress-linear>
      </v-col>
      <v-col v-if="data.planned" cols="1" class="d-flex align-center">
       <v-icon v-if="data.progress === 100" class="ml-8" color="success">mdi-check-bold</v-icon>
      </v-col>
      <v-col v-else cols="3" class="d-flex align-center justify-start">
        <b>Nog in te plannen ronde</b>
      </v-col>
      <v-col v-if="data.planned" cols="2" class="d-flex align-center justify-center">
        <v-list>
          <v-list-group value="Student(en)">
            <template v-slot:activator="{ props }">
              <v-list-item rounded
                           v-bind="props"
                           title="Student(en)"
              ></v-list-item>
            </template>
            <v-list-item v-for="(student, i) in data.students" :key="i" :title="student"
            ></v-list-item>
          </v-list-group>
        </v-list>
      </v-col>
      <v-col v-else cols="2"></v-col>
      <v-col v-if="data.planned" cols="1" class="d-flex align-center justify-center">
        <v-btn @click="editRonde" density="comfortable" icon="mdi-information-outline"></v-btn>
      </v-col>
      <v-col v-else cols="1" class="d-flex align-center justify-center">
        <normal-button :parent-function="goToRonde" text="+"></normal-button>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NormalButton from '@/components/NormalButton'
export default {
  name: 'DashboardRoundCard',
  components: { NormalButton },
  props: {
    data: {
      type: Object,
      default: () => ({
        name: 'Empty',
        datum: 'Empty',
        progress: 0,
        planned: false,
        students: ['Test', 'Test2']
      })
    }
  },
  methods: {
    editRonde () {
      // TODO Go to Ronde to edit
    },
    goToRonde () {
      // TODO Go to the Ronde page
    }
  }
}
</script>
<style>
.container-border {
  border: 1px solid #E3e3e3;
  border-radius: 25px;
}
.container-height {
  height: 100px
}
</style>
