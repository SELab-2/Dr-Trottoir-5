<template>
  <div fluid>
    <v-card max-width="900px" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col align="left" cols="8">
            <p style="font-size: 16px; font-weight: bold;">{{ data.remark }}</p>
          </v-col>
          <v-col class="d-flex align-center" cols="4">
            <v-row justify="end" class="image-margin">
              <v-img :src="data.image" :max-width="300" :max-height="300" @click="overlay = !overlay"></v-img>
              <v-overlay v-model="overlay">
                <div>
                  <img :src="data.image" />
                </div>
              </v-overlay>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col align="left">
            <p style="font-size: 16px">{{ new Date(data.time).toLocaleString() }}</p>
          </v-col>
          <v-col v-if="!('admin' in data)">
            <v-row justify="end" class="row-margin">
              <v-icon class="row-margin" v-on:click="goToMailPage" dark size="30px">mdi-email-outline</v-icon>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>/**
 * FotoCardAdmin component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * time: String
 * remark: String
 * image: String
 */

import router from "@/router";
import {ErrorHandler} from "@/api/error/ErrorHandler";
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import BuildingService from "@/api/services/BuildingService";

export default {
  name: 'FotoCardAdmin',
  props: {
    data: {
      type: Object,
      default: () => ({
        id: 0,
        image: 'empty',
        infoPerBuilding: 0,
        pictureType: 'Empty',
        remark: 'Empty',
        time: 'Empty'
      })
    },
  },
  data: () => {
    return {
      building: 0,
      syndici: 0,
      overlay: false
    }
  },
  async beforeMount() {
    await RequestHandler.handle(PlanningService.getInfoById(this.data.infoPerBuilding)).then(async result => {
      this.building = result.building
      await RequestHandler.handle(BuildingService.getBuildingById(result.building)).then( building => {
        this.syndici = building.syndicus.length
      })
    })
  },
  methods: {
    goToMailPage: function () {
      if (this.syndici === 0) {
        this.$store.dispatch("snackbar/open", {
          message: "Er zijn geen syndici verbonden aan dit gebwouw",
          color: "error"
        })
        return
      }else{
        router.push({name: 'send_mail', params:{id: this.building,  postId:this.data.id}})
      }
    }
  },
  components: {}
}
</script>

<style scoped>

</style>
