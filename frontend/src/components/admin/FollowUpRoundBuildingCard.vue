<template>
  <v-container class="container-border">
    <v-row class="text-center">
      <v-col>
        <p @click="goToBuildingPage" class="text-style-building">{{ this.data.gebouw }}</p>
      </v-col>
      <v-col>
        <p>{{ this.data.state }}</p>
      </v-col>
      <v-col>
        <p>{{ this.data.remark }}</p>
      </v-col>
      <v-col>
        <p :style="{ color: durationColor }">{{ durationText }}</p>
      </v-col>
      <v-col>
        <p>{{ this.data.location }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

/**
 * FollowUpRoundBuildingCard component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * gebouw: String
 * state: String
 * remark: String
 * duration: Number
 * location: String
 * optimalDuration: Number (is de optimale tijd voor een gebouw)
 */

export default {
  name: 'FollowUpRoundBuildingCard',
  props: {
    data: {
      type: Object,
      default: () => ({
        gebouw: 'Empty',
        state: 'Empty',
        remark: 'Empty',
        duration: 0,
        location: 'Empty',
        optimalDuration: 15 * 60
      })
    }
  },
  data: () => ({
    optimalDuration: Number
  }),
  computed: {
    durationText () {
      const minutes = Math.floor(this.data.duration / 60)
      const seconds = this.data.duration - minutes * 60
      if (this.data.duration === 0) {
        return '-'
      } else if (this.data.duration < this.data.optimalDuration) {
        return minutes + 'min ' + seconds + 's'
      } else {
        return minutes + 'min ' + seconds + 's'
      }
    },
    durationColor () {
      if (this.data.duration === 0) {
        return 'black'
      } else if (this.data.duration < this.data.optimalDuration) {
        return '#FF1F00'
      } else {
        return '#39AE68'
      }
    }
  },
  methods: {
    goToBuildingPage: function () {
      // TODO
    }
  },
  async mounted () {
    this.optimalDuration = this.data.optimalDuration
  }
}
</script>

<style scoped>
.text-style-building {
  text-decoration-line: underline;
  cursor: pointer;
}
.container-test {
  display: inline-block;
  width: 80%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
