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
          <label>{{arg.substring(1, arg.length-1)}}</label>
          <v-text-field v-model="this.inputArguments[index]"></v-text-field>
        </div>
      </div>
      <h2>Bericht</h2>
      <v-container v-html="formattedText"  style="white-space: pre-wrap; font-size: 16px" class="container-border"/>
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
      {id: 1, name: 'Template 1', description: 'Beste #arg1#,\n\n#arg2#  #arg1#  dit is echt een mega lange text om te testen of het wel goed gaat, maar' +
      'maar blijkbaar\ntesten of het wel goed gaat, maar\n\nMet vriendelijke groeten #naam#'},
      {id: 2, name: 'Template 2', description: 'Template 2'},

    ],
    positionsArguments: [],
    inputArguments: []
  }),
  methods: {
    sendMail() {
      console.log(this.getDescriptionWithArguments());
    },
    updateArguments() {
      this.positionsArguments = [];

      const regex = /(#\w+#)/g;
      let match;

      while ((match = regex.exec(this.description)) !== null) {
        const argument = match[1];
        if (!this.positionsArguments.includes(argument)){
          this.positionsArguments.push(argument);
        }
      }
      if (this.positionsArguments.length !== 0) {
        this.inputArguments = new Array(this.positionsArguments.length).fill('');
      } else {
        this.inputArguments = [];
      }
    },
    getDescriptionWithArguments() {
      let description = this.description;
      for (let i = 0; i < this.positionsArguments.length; i++) {
        if (this.inputArguments[i] !== '') {
          description = description.replaceAll(this.positionsArguments[i], this.inputArguments[i]);
        }
      }
      return description;
    }
  },
  watch: {
    description(){
      this.updateArguments();
    }
  },
  computed: {
    formattedText() {
      return this.getDescriptionWithArguments().replace(/#([^#]*)#/g, '<b>$1</b>');
    }
  },
  mounted() {
    //TODO get templates from backend
  },
  components: {NormalButton, FotoCardSyndicus}
}
</script>

<style scoped>

</style>
