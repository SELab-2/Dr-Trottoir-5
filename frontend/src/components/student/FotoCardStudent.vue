<template>
  <v-container fluid>
    <v-card max-width="800px" min-width="250px" class="container-border">
      <v-card-text>
        <v-row align-end>
          <v-col align="left" cols="8">
            <p data-test="remark" style="font-size: 12px">{{ data.remark }}</p>
          </v-col>
          <v-col class="d-flex align-center" cols="4">
            <v-row justify="end" class="image-margin">
              <v-img data-test="image" :src="data.image" :max-width="'150px'" :max-height="'150px'"></v-img>
            </v-row>
          </v-col>
        </v-row>
        <v-row align="end">
          <v-col align="left">
            <p data-test="time" style="font-size: 10px">{{ new Date(data.time).toLocaleString() }}</p>
          </v-col>
          <v-col>
            <v-row justify="end" class="row-margin">
              <v-btn data-test="edit-button" icon tile class="button-margin" style="max-height: 35px; max-width: 35px;"
                     v-on:click="goToEditPage">
                <EditIcon/>
              </v-btn>
              <v-btn data-test="delete-button" icon tile style="max-height: 35px; max-width: 35px;" v-on:click="deletePost">
                <DeleteIcon/>
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import EditIcon from '../icons/EditIcon.vue'
import DeleteIcon from '../icons/DeleteIcon.vue'
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import router from "@/router";

/**
 * FotoCardStudent component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * timeStamp: String
 * description: String
 * imageURL: String
 */

export default {
  name: 'FotoCardStudent',
  props: {
    data: {
      type: Object,
      default: () => ({ time: 'Empty', remark: 'Empty', image: 'Empty', id: '' })
    },
    buildingName: {type: String, default: ''},
    type: {type: String, default: ''},
    info: {type: String, default: ''}
  },
  methods: {
    goToEditPage() {
      router.push({name: 'student_post_edit', query: {building: this.buildingName, type: this.type, info: this.info, id: this.data.id}});
    },
    deletePost() {
      RequestHandler.handle(PlanningService.deletePicture(this.data.id), {
        id: "getPicturesError",
        style: "NONE"
      }).catch(() => null).finally(() => {
        this.$el.parentNode.removeChild(this.$el);
      });
    }
  },
  components: {
    EditIcon,
    DeleteIcon
  }
}
</script>

<style scoped>

</style>
