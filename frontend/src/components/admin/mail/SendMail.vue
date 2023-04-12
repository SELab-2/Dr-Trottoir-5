<template>
<v-container>
  <h1 align="center">Mail versturen</h1>
  <FotoCardSyndicus align="center" :data="data.post"/>
   <label class="black-text">Template</label>
      <v-autocomplete
        clearable
        outlined
        :items="this.templates"
        item-title="name"
        item-value="description"
        v-model="this.description"
      ></v-autocomplete>
  <v-container v-if="this.description !== null" style="white-space: pre-wrap; font-size: 16px" class="container-border">
    <p> {{this.description}} </p>
  </v-container>
  <v-container align="center">
<NormalButton text="Stuur email" :parent-function="sendMail"/>
    </v-container>
</v-container>
</template>

<script>
import FotoCardSyndicus from "@/components/syndicus/FotoCardSyndicus.vue";
import NormalButton from "@/components/NormalButton.vue";

export default {
  name: 'SendMail',
  props: {
    data: {
      type: Object,
      default: () => ({post:{ timeStamp: 'Empty', description: 'fghsljdfbglbsdljbgjlbflsbvjfbsvdblkfdsjgmfjsdgljlfkdjsgljdflgsljflgjldfv', imageURL: 'https://cdn.pixabay.com/photo/2022/08/31/13/05/sea-7423274__480.jpg' }})
    }
  },
  data: () => ({
    description: null,
    templates: [
      { id: 1, name: 'Template 1', description: 'Template 1' },
      { id: 2, name: 'Template 2', description: 'Template 2' },

    ],
  }),
  methods: {
    sendMail() {
      console.log(this.description);
    }
  },
  components: {NormalButton, FotoCardSyndicus}
}
</script>

<style scoped>

</style>
