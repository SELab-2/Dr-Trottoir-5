<template>
  <v-row justify="center" align="center" class="pt-10">
    <h1>Nieuw gebouw aanmaken</h1>
  </v-row>
  <v-card color="white" :class="`mx-auto my-16 ${smallScreen ? 'w-100' : 'w-75'}`">
    <v-row align="center" justify="center" class="xs-flex-column">
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Naam</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field class="text_field" variant="outlined" v-model:model-value="name"></v-text-field>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Adres</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field class="text_field" variant="outlined" v-model:model-value="name"></v-text-field>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-end align-center pt-10">
        <h2>Klanten nummer</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field class="text_field" variant="outlined" v-model:model-value="klant_nr"></v-text-field>
      </v-col>
      <v-col col="12" lg="12" class="d-flex justify-center align-center pt-10">
        <h2>Handleiding</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-end" v-cloak @drop.prevent="addDropFile"
             @dragover.prevent>
        <v-img class="drag_image" :width="150" :max-height="150" aspect-ratio="1"
               src="../assets/upload_file.png"></v-img>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-start align-center">
        <v-file-input v-model="file" prepend-icon="mdi-file-upload-outline" class="text_field"
                      variant="outlined"></v-file-input>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-end align-center pt-10">
        <h2>Geschatte tijd</h2>
      </v-col>
      <v-col col="12" lg="6" class="d-flex justify-lg-start align-center">
        <v-text-field placeholder="In minuten" class="text_field" variant="outlined"
                      v-model:model-value="time"></v-text-field>
      </v-col>
      <v-col col="12" lg="12" class="d-flex justify-center align-center">
        <normal-button text="Maak gebouw aan" :parent-function="createBuilding"></normal-button>
      </v-col>
      <v-col class="pt-5"></v-col>
    </v-row>
  </v-card>
</template>

<script>
import NormalButton from '@/components/NormalButton'
import {RequestHandler} from "@/api/RequestHandler";
import BuildingService from "@/api/services/BuildingService";

export default {
  name: 'CreateBuildingView',
  components: {NormalButton},
  data: () => {
    return {
      name: '',
      adres: '',
      klant_nr: null,
      file: null,
      time: null,
      smallScreen: false
    }
  },
  methods: {
    addDropFile(e) {
      this.file = e.dataTransfer.files[0];
    },
    createBuilding() {
      const test = this.createManual();
      console.log(test)
    },
    async createManual() {
      if (this.file === null) {
        return "Error"
      }
      let formData = new FormData()
      formData.append('file', this.file[0])
      return RequestHandler.handle(BuildingService.createManual({
        file: formData,
        fileType: this.file[0].name.split('.').pop(),
        manaulStatus: "klaar"
      }, 'multipart/form-data'), {
        id: 'createManualError',
        style: "SNACKBAR"
      });
    }
  }
}
</script>
<style>
.text_field {
  height: 40px;
  max-width: 350px;
  padding-left: 5px;
  padding-top: 5px;
}

.drag_image {
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
</style>
