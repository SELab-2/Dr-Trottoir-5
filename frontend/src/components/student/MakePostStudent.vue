<template>
  <div style="height: 40%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <v-col align="center" style="height: 20%">
      <div v-if="imageUrl === ''" style="height: 100%; display: flex; justify-content: center; align-items: center;">
        <div @click="selectImage"
             style="border: 5px solid #E3e3e3; display: inline-block; padding: 10px; border-radius: 10px;">
          <v-avatar size="100px">
            <v-icon size="100px" dark>mdi-image</v-icon>
          </v-avatar>
          <p style="margin-top: 10px;">Klik voor een foto toe te voegen</p>
        </div>
      </div>
      <div v-else style="height: 100%">
        <div style="height: 90%; position: center;">
          <v-img :src="imageUrl"></v-img>
        </div>
        <div align="right" style="height: 10%">
          <v-btn style="margin-top: 10px" @click="removeImage">Remove</v-btn>
        </div>
      </div>
    </v-col>
  </div>
  <div style="height: 60%; justify-content: center;">
    <h1 align="center">{{ data.title }}</h1>
    <h3 align="center">{{ data.type }}</h3>
    <div align="center">
      <v-form>
        <v-container>
          <v-textarea label="Beschrijving" outlined rows="3"></v-textarea>
        </v-container>
      </v-form>
    </div>
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
      <v-checkbox color="#FFE600" v-model="checked" label="Opmerking"></v-checkbox>
      <div class="text-center" style="position: absolute; bottom: 10px; width: 100%;">
        <NormalButton style="width: 150px; height: 40px" text="Post"/>
      </div>
    </div>
  </div>
</template>

<script>

//TODO maak css inplaats van inline styling

import NormalButton from "@/components/NormalButton.vue";

export default {
  name: 'MakePostStudent',
  components: {NormalButton},
  props: {
    data: {
      type: Object,
      default: () => ({title: 'Resto s5', type: 'Aankomst', imageURL: 'Empty'})
    }
  },
  data() {
    return {
      imageUrl: '',
      checked: false,
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
    }
  },
}
</script>

<style scoped>

</style>
