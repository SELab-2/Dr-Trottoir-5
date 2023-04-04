<template>
  <div style="height: 40%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <v-col align="center" style="height: 20%; justify-content: center">
      <div v-if="imageUrl === ''">
        <v-avatar @click="selectImage" size="200px" >
          <v-icon size="200px" dark>mdi-image</v-icon>
        </v-avatar>
        <p>Klik voor een foto toe te voegen</p>
      </div>
      <div v-else style="height: 100%">
        <div style="height: 90%; position: relative;">
          <v-img :src="imageUrl"></v-img>
        </div>
        <div align="right">
          <v-btn style="margin-top: 10px" @click="removeImage">Remove</v-btn>
        </div>
      </div>
    </v-col>
  </div>
  <v-card-text>
    <v-checkbox v-model="checked" label="Remark"></v-checkbox>
  </v-card-text>
</template>

<script>
export default {
  name: 'MakePostStudent',
  data() {
    return {
      imageUrl: '',
      title: '',
      checked: false,
    }
  },
  methods: {
    selectImage() {
      const input = document.createElement('input')
      input.type = 'file'
      input.accept = 'image/*'
      input.onchange = (event) => {
        const file = event.target.files[0]
        const reader = new FileReader()
        reader.onload = (e) => {
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
