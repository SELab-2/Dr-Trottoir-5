<template>
  <v-container align="center">
    <v-card max-width="750px">
      <div class="top-div-style">
        <div v-if="imageUrl === ''" class="if-div-style mt-3 mb-2">
          <div @click="selectImage" class="image-upload-placeholder">
            <v-avatar size="100px">
              <v-icon size="100px" dark>mdi-image</v-icon>
            </v-avatar>
            <p>Klik om een foto toe te voegen</p>
          </div>
        </div>
        <div v-else>
          <div class="image-div-style">
            <v-img :src="imageUrl"></v-img>
          </div>
          <div align="center" style="height: 15%">
            <v-btn icon tile class="icon-size" v-on:click="removeImage">
                  <DeleteIcon/>
            </v-btn>
          </div>
        </div>
      </div>
      <div class="bottom-div-style">
        <h1 align="center">{{ data.buildingName }}</h1>
        <h3 align="center">{{ data.type }}</h3>
        <div align="center">
          <v-form>
            <v-container>
              <v-textarea label="Beschrijving" outlined v-model="description" rows="4"></v-textarea>
            </v-container>
          </v-form>
        </div>
        <div align="center">
          <NormalButton v-if="!data.edit" class="own-button-style mb-4 mx-2" text="Uploaden" :parent-function="uploadData" />
          <NormalButton v-else class="own-button-style my-2 mx-2" text="Bevestig" :parent-function="editData"/>
        </div>
      </div>
    </v-card>
  </v-container>
</template>

<script>
/**
 * CreateEditPostStudent component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * edit: Boolean deze wordt gebruikt om te bepalen of de component gebruikt wordt om een post te maken of te bewerken.
 * Als edit true is dan wordt de data van de backend gehaald en ingevuld in de component.
 *
 * nameBuilding: String
 * type: String (Aankomst of Vertrek of Berging)
 * info: ID for infoPerBuilding
 *
 * Data (aangepaste) moet naar de backend worden gestuurd worden zie functie uploadData en editData.
 */

import NormalButton from "@/components/NormalButton.vue";
import DeleteIcon from "@/components/icons/DeleteIcon.vue";
import {RequestHandler} from "@/api/RequestHandler";
import PlanningService from "@/api/services/PlanningService";
import router from "@/router";
const emitter = require('tiny-emitter/instance');

export default {
  name: 'CreateEditPostStudent',
  components: {DeleteIcon, NormalButton},
  props: {
    data: {
      type: Object,
      default: () => ({nameBuilding: '', type: '', info: '', edit: false, id: '', planning: '', building_id: ''})
    }
  },
  data() {
    return {
      imageUrl: '',
      description: '',
      original: {}
    }
  },
  methods: {
    selectImage() {
      const input = document.createElement('input');
      input.style = 'display: none;';
      input.id = 'input';
      document.body.appendChild(input);
      input.type = 'file';
      // Alleen images accepteren
      input.accept = 'image/*';
      input.onchange = (event) => {
        // selecteert de eerste file die die de gebruiker heeft geselecteerd
        this.imageUrl = URL.createObjectURL(event.target.files[0]);
      }
      input.click();
    },
    removeImage() {
      this.imageUrl = '';
    },
    imageCheck() {
      if (this.imageUrl === '') {
        emitter.emit("error", {message: 'Voeg een foto toe.'}, {
          style: 'SNACKBAR',
          id: 'imageURLEmptyError'
        })
        router.afterEach(() => {
          emitter.emit("error-clear");
        });
        return false;
      }

      return true;
    },
    async uploadData() {
      if (!this.imageCheck()) return;
      const input = document.getElementById("input");
      const image = input.files[0];
      let time = new Date().toISOString()
      time = time.slice(0, time.lastIndexOf(':')).replace(/T/, ' ')
      await RequestHandler.handle(PlanningService.uploadPicture(
        image,
        this.data.info,
        this.data.type === 'Aankomst' ? 'AR' : this.data.type === 'Berging' ? 'ST' : this.data.type === 'Extra' ? 'EX' : 'DE',
        time,
        this.description
      ), {
        id: "uploadImageError",
        style: "SNACKBAR"
      }).then(b => b).catch(() => null);

      this.imageUrl = '';
      input.value = '';
      input.remove();

      router.go(-1);
    },
    async editData() {
      if (!this.imageCheck()) return;
      const input = document.getElementById("input");
      if (!input) {
        await RequestHandler.handle(PlanningService.patchPicture(
          this.data.id,
          this.data.info,
          this.data.type === 'Aankomst' ? 'AR' : this.data.type === 'Berging' ? 'ST' : this.data.type === 'Extra' ? 'EX' : 'DE',
          new Date().toISOString(),
          this.description
        ), {
          id: "patchImageError",
          style: "SNACKBAR"
        }).then(b => b).catch(() => null);
      } else {
        const image = input.files[0];
        await RequestHandler.handle(PlanningService.updatePicture(
          this.data.id,
          image,
          this.data.info,
          this.data.type === 'Aankomst' ? 'AR' : this.data.type === 'Berging' ? 'ST' : this.data.type === 'Extra' ? 'EX' : 'DE',
          new Date().toISOString(),
          this.description
        ), {
          id: "editImageError",
          style: "SNACKBAR"
        }).then(b => b).catch(() => null);
      }

      this.imageUrl = '';
      input.value = '';
      input.remove();
      router.go(-1);
    }
  },
  mounted() {
    if (this.data.edit){
      RequestHandler.handle(PlanningService.getPicture(this.data.id), {
        id: "getImageError",
        style: "SNACKBAR"
      }).then(b => {
        this.description = b.remark;
        this.imageUrl = b.image;
        this.original = b;
      }).catch(() => null);
    }
  }
}
</script>

<style scoped>
.top-div-style {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 2px;
}
.bottom-div-style{
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
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 100px;
  margin: 2px;
}
.own-button-style {
  width: 150px;
  height: 40px;
}
</style>
