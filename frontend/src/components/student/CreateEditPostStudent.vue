<template>
  <div class="top-div-style">
    <v-col align="center" style="overflow: hidden;">
      <div v-if="imageUrl === ''" class="if-div-style">
        <div @click="selectImage" class="image-upload-placeholder">
          <v-avatar size="100px">
            <v-icon size="100px" dark>mdi-image</v-icon>
          </v-avatar>
          <p>Klik voor een foto toe te voegen</p>
        </div>
      </div>
      <div v-else style="height: 100%">
        <div class="image-div-style">
          <v-img :src="imageUrl"></v-img>
        </div>
        <div align="right" style="height: 15%">
          <v-btn icon tile class="icon-size" v-on:click="removeImage">
                <DeleteIcon/>
          </v-btn>
        </div>
      </div>
    </v-col>
  </div>
  <div class="bottom-div-style">
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
    <div v-if="!this.data.edit" class="text-center button-positioning-div">
      <NormalButton class="own-button-style" text="Post" :parent-function="uploadData"/>
    </div>
    <div v-else class="text-center button-positioning-div">
      <NormalButton class="own-button-style" text="Bevestig" :parent-function="editData"/>
    </div>
  </div>
</template>

<script>
//TODO popup als nog niet alles is ingevuld
/**
 * CreateEditPostStudent component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * edit: Boolean deze wordt gebruikt om te bepalen of de component gebruikt wordt om een post te maken of te bewerken.
 * Als edit true is dan wordt de data van de backend gehaald en ingevuld in de component.
 *
 * nameBuilding: String
 * type: String (Aankomst of Vertrek of Berging)
 *
 * Data (aangepaste) moet naar de backend worden gestuurd worden zie functie uploadData en editData.
 */

import NormalButton from "@/components/NormalButton.vue";
import DeleteIcon from "@/components/icons/DeleteIcon.vue";

export default {
  name: 'CreateEditPostStudent',
  components: {DeleteIcon, NormalButton},
  props: {
    data: {
      type: Object,
      default: () => ({nameBuilding: 'Resto s5', type: 'Aankomst', edit: false})
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
      console.log(this.imageUrl); // deze is in base64
      console.log(this.description);
      //TODO data versturen naar backend
    },
    editData() {
      //TODO deze data verwerken + terug gaan naar het overview scherm
      console.log(this.checked);
      console.log(this.imageUrl); // deze is in base64
      console.log(this.description);
      //TODO aangepaste data versturen naar backend
    }
  },
  mounted() {
    if (this.data.edit){
      //TODO data ophalen van backend aan de hand van de ID (image, description, checked)
    }
  }
}
</script>

<style scoped>
.top-div-style {
  height: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
.bottom-div-style{
  height: 60%;
  justify-content: center;
}

.if-div-style {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.image-upload-placeholder {
  border: 5px solid #E3e3e3;
  display: inline-block;
  padding: 10px;
  border-radius: 10px;
}
.image-div-style {
  height: 85%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.own-button-style {
  width: 150px;
  height: 40px;
}
.button-positioning-div {
  position: absolute;
  bottom: 10px;
  width: 100%;
}
</style>
