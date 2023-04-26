<template>
  <v-container class="container-border">
    <v-row class="text-center">
      <v-col cols="2">
        <p @click="goToBuildingPage" class="text-style-building" style="word-wrap: break-word;">
          {{ this.data.building.name }}</p>
      </v-col>
      <v-col cols="2">
        <p style="word-wrap: break-word;">{{ this.state }}</p>
      </v-col>
      <v-col cols="2">
        <v-expansion-panels style="width: 90%;">
          <v-expansion-panel :title="this.remarks.length + ' opmerkingen'" :disabled="this.remarks.length === 0">
            <v-expansion-panel-text v-if="this.remarks.length > 0">
              <p style="word-wrap: break-word;" v-for="remark in this.remarks">{{ remark }}</p>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
      <v-col cols="1">
        <p :style="{ color: durationColor }" style="word-wrap: break-word;">{{ durationText }}</p>
      </v-col>
      <v-col cols="5">
        <p style="word-wrap: break-word;">{{ this.data.building.adres }}</p>
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
        building: {},
        pictures: [],
        optimalDuration: 15 * 60
      })
    }
  },
  data: () => ({
    optimalDuration: 0,
    state: 'Niet voltooid',
    remarks: [],
    duration: 0
  }),
  computed: {
    durationText () {
      const minutes = Math.floor(this.duration / 60);
      const seconds = Math.round(this.duration - minutes * 60);
      if (this.duration === 0) {
        return '-';
      } else if (this.duration < this.optimalDuration) {
        return minutes + 'min ' + seconds + 's';
      } else {
        return minutes + 'min ' + seconds + 's';
      }
    },
    durationColor() {
      if (this.duration === 0) {
        return 'black';
      } else if (this.duration > this.optimalDuration) {
        return '#FF1F00';
      } else {
        return '#39AE68';
      }
    }
  },
  methods: {
    goToBuildingPage: function () {
      // TODO
    }
  },
  async mounted() {
    this.optimalDuration = this.data.optimalDuration;
    this.remarks = this.data.pictures.map(pic => pic.remark).filter(remark => remark !== '');

    if (this.data.pictures.filter(pic => pic.pictureType === 'DE').length > 0) {
      const last = this.data.pictures.sort((p1, p2) => new Date(p1.time) < new Date(p2.time) ? -1 : 1);
      this.state = `Voltooid om ${new Date(last[last.length - 1].time).toLocaleTimeString([], {timeStyle: 'short'})}`;
      this.duration = (new Date(last[last.length - 1].time).getTime() - new Date(last[0].time).getTime()) / 1000;
    } else if (this.data.pictures.length > 0) {
      const first = this.data.pictures.sort((p1, p2) => new Date(p1.time) < new Date(p2.time) ? -1 : 1)[0];
      this.state = `Bezig sinds ${new Date(first.time).toLocaleTimeString([], {timeStyle: 'short'})}`;
    }
  }
}
</script>

<style scoped>
.text-style-building {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
