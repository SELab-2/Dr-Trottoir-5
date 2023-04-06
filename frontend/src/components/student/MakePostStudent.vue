<template>
  <div style="height: 40%; display: flex; flex-direction: column; justify-content: center; align-items: center; overflow: hidden;">
    <v-col align="center" style="height: 20%; overflow: hidden;">
      <div v-if="imageUrl === ''" style="height: 100%; display: flex; justify-content: center; align-items: center;">
        <div @click="selectImage" style="border: 5px solid #E3e3e3; display: inline-block; padding: 10px; border-radius: 10px;">
          <v-avatar size="100px">
            <v-icon size="100px" dark>mdi-image</v-icon>
          </v-avatar>
          <p style="margin-top: 10px;">Klik voor een foto toe te voegen</p>
        </div>
      </div>
      <div v-else style="height: 100%">
        <div style="height: 85%; display: flex; justify-content: center; align-items: center;">
          <v-img :src="imageUrl"></v-img>
        </div>
        <div align="right" style="height: 15%">
          <v-btn icon tile style="max-height: 35px; max-width: 35px;" v-on:click="removeImage">
                <DeleteIcon/>
          </v-btn>
        </div>
      </div>
    </v-col>
  </div>
  <div style="height: 60%; justify-content: center;">
    <h1 align="center">{{ data.nameBuilding }}</h1>
    <h3 align="center">{{ data.type }}</h3>
    <div align="center">
      <v-form>
        <v-container>
          <v-textarea label="Beschrijving" outlined v-model="description" rows="4"></v-textarea>
          <v-checkbox color="#FFE600" v-model="checked" label="Opmerking"></v-checkbox>
        </v-container>
      </v-form>
    </div>
      <div class="text-center" style="position: absolute; bottom: 10px; width: 100%;">
        <NormalButton style="width: 150px; height: 40px" text="Post" :parent-function="uploadData"/>
    </div>
  </div>
</template>

<script>
//TODO popup als nog niet alles is ingevuld
/**
 * MakePostStudent component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * nameBuilding: String
 * type: String (Aankomst of Vertrek of Berging)
 *
 * Data moet naar de backend worden gestuurd worden zie functie uploadData.
 */

import NormalButton from "@/components/NormalButton.vue";
import DeleteIcon from "@/components/icons/DeleteIcon.vue";
import {description} from "@/api/EchoFetch/docs/.vuepress/config";

export default {
  name: 'MakePostStudent',
  components: {DeleteIcon, NormalButton},
  props: {
    data: {
      type: Object,
      default: () => ({nameBuilding: 'Resto s5', type: 'Aankomst'})
    }
  },
  data() {
    return {
      imageUrl: '',
      checked: false,
      description: '',
    }
  },
  methods: {
    selectImage() {
      const input = document.createElement('input')
      input.type = 'file'
      // Alleen images accepteren
      input.accept = 'image/*'
      input.onchange = (event) => {
        // selecteert de eerste file die die de gebruiker heeft geselecteerd
        const file = event.target.files[0]
        const reader = new FileReader()
        reader.onload = (e) => {
          // zet de result van de reader om naar een base64 string
          this.imageUrl = e.target.result
        }
        reader.readAsDataURL(file)
      }
      input.click()
    },
    removeImage() {
      this.imageUrl = '';
    },
    uploadData() {
      //TODO deze data verwerken + terug gaan naar het overview scherm
      console.log(this.checked);
      console.log(this.imageUrl);
      console.log(this.description);
      //TODO data versturen naar backend
    }
  },
}
</script>

<style scoped>

</style>
