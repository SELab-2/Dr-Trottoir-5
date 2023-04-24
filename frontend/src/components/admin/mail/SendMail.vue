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
      v-on:slotchange="updateArguments"
    ></v-autocomplete>
    <div v-if="this.description !== null">
      <div v-if="this.inputArguments.length !== 0">
        <h2>Argumenten</h2>
        <div v-for="(arg, index) in this.positionsArguments">
          <label>{{getArgumentName(arg)}}</label>
          <v-text-field v-model="this.inputArguments[index]"></v-text-field>
        </div>
      </div>
      <h2>Bericht</h2>
      <v-container style="white-space: pre-wrap; font-size: 16px" class="container-border">
        <p> {{ this.description }} </p>
      </v-container>
    </div>
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
      default: () => ({
        post: {
          timeStamp: 'Empty',
          description: 'fghsljdfbglbsdljbgjlbflsbvjfbsvdblkfdsjgmfjsdgljlfkdjsgljdflgsljflgjldfv',
          imageURL: 'https://cdn.pixabay.com/photo/2022/08/31/13/05/sea-7423274__480.jpg'
        }
      })
    }
  },
  data: () => ({
    description: null,
    templates: [
      {id: 1, name: 'Template 1', description: 'Template 1#arg1#     #arg2#'},
      {id: 2, name: 'Template 2', description: 'Template 2'},

    ],
    positionsArguments: [],
    inputArguments: []
  }),
  methods: {
    sendMail() {
      console.log(this.description);
      console.log(this.inputArguments);
    },
    updateArguments() {
      this.positionsArguments = [];

      const regex = /#(\w+)#/g;
      let match;

      while ((match = regex.exec(this.description)) !== null) {
        this.positionsArguments.push({
          position: match.index,
          length: match[1].length
        });
      }
      if (this.positionsArguments.length !== 0) {
        this.inputArguments = new Array(this.positionsArguments.length).fill('');
      } else {
        this.inputArguments = [];
      }
    },
    getArgumentName(arg) {
      return this.description.substring(arg.position+1, arg.position + arg.length+1);
    }
  },
  watch: {
    description(){
      this.updateArguments();
    }
  },
  components: {NormalButton, FotoCardSyndicus}
}
</script>

<style scoped>

</style>
