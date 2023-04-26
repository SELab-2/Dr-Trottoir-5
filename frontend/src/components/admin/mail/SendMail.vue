<template>
  <v-container>
    <h1 align="center">Mail versturen</h1>
    <FotoCardSyndicus align="center" :data="data.post"/>
    <label class="black-text">Aan</label>
    <v-text-field class="black-text" readonly >{{ data.syndicusEmail }}</v-text-field>
    <label class="black-text">Template</label>
    <v-autocomplete
      clearable
      outlined
      :items="this.templates"
      item-title="name"
      item-value="content"
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
      <h2>Onderwerp</h2>
      <v-text-field v-model="this.subject"></v-text-field>
      <h2>Bericht</h2>
      <v-container v-html="formattedText"  style="white-space: pre-wrap; font-size: 16px" class="container-border"/>
    </div>
    <v-container align="center">
      <NormalButton text="Stuur email" :parent-function="sendMail"/>
    </v-container>
  </v-container>
<a :href="'mailto:'+ data.syndicusEmail +'?subject=' +  this.subject +'&body=' + getMailBody()">Send Email</a>

</template>

<script>

/**
 * SendMail component wordt gebruikt door als props een post object met de volgende keys mee te geven:
 *    timeStamp: String
 *    description: String
 *    imageURL: String
 * Dit komt overeen met de velden van een post die de student gemaakt heeft.
 */

import FotoCardSyndicus from "@/components/syndicus/FotoCardSyndicus.vue";
import NormalButton from "@/components/NormalButton.vue";
import {RequestHandler} from "@/api/RequestHandler";
import MailTemplateService from "@/api/services/MailTemplateService";

export default {
  name: 'SendMail',
  props: {
    data: {
      default: () => ({
        syndicusEmail: 'test@test.be',
        post: {
          timeStamp: new Date(),
          description: 'fghsljdfbglbsdljbgjlbflsbvjfbsvdblkfdsjgmfjsdgljlfkdjsgljdflgsljflgjldfv',
          imageURL: 'https://cdn.pixabay.com/photo/2022/08/31/13/05/sea-7423274__480.jpg'
        }
      })
    }
  },
  data: () => ({
    description: null,
    templates: [],
    positionsArguments: [],
    inputArguments: [],
    subject: ''
  }),
  methods: {
    sendMail() {
      console.log("send mail")
    },
    getMailBody() {
      return encodeURIComponent(this.getDescriptionWithArguments()).replace(/%0A/g, '%0D%0A')+
        encodeURIComponent("\n\nStudent:\nOpmerking student: " + this.$props.data.post.description + "\nTijdstip: " + this.$props.data.post.timeStamp.toString()+"\nZie bijlage voor foto.\n\n").replace(/%0A/g, '%0D%0A');
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
  async mounted() {
    await RequestHandler.handle(
      MailTemplateService.getMailTemplates(),
      {
        id: 'getMailTemplateError',
        style: "SNACKBAR",
      }).then((response) => {
      this.templates = response
    })
  },
  components: {NormalButton, FotoCardSyndicus}
}
</script>

<style scoped>

</style>
