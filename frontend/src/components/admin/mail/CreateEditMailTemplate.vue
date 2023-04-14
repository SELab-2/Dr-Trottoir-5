<template>
  <v-container>
    <h1 v-if="!edit" align="center">Mail template aanmaken</h1>
    <h1 v-else align="center">Mail template aanpassen</h1>
    <p>Naam</p>
    <v-text-field v-model="this.template.name"></v-text-field>
    <p>Tekst
      <v-avatar class="button-style" size="25px" style="border: 1px solid #E3e3e3;border-radius: 25px;">
        <v-icon size="25px" dark color="gray" @click="showDialog = true">mdi-information-variant</v-icon>
      </v-avatar>
    </p>
    <v-card style="margin-top: 5px">
      <v-tabs
        v-model="tab"
      >
        <v-tab value="one">Pas aan</v-tab>
        <v-tab value="two">Previeuw</v-tab>
      </v-tabs>

      <v-card-text>
        <v-window v-model="tab">
          <v-window-item value="one">
            <v-textarea v-html="formattedText" v-model="this.template.text" auto-grow
                        ></v-textarea>
          </v-window-item>

          <v-window-item value="two" >
            <v-container v-html="formattedText" style="white-space: pre-wrap; font-size: 16px"></v-container>
          </v-window-item>
        </v-window>
      </v-card-text>
    </v-card>
  </v-container>
  <v-container align="center">
    <NormalButton v-if="!edit" text="Maak template aan" :parent-function="createTemplate"/>
    <NormalButton v-else text="Pas template aan" :parent-function="editTemplate"/>
  </v-container>

  <v-dialog v-model="showDialog">
    <v-card class="container-border">
      <v-card-title>Info argumenten</v-card-title>
      <v-card-text>
        Argumenten worden aangeduid door twee <span class="arg-placeholder">#</span> te gebruiken rond het argument.
        <br/>
        Bijvoorbeeld voor syndicus en naam:
        <br/>
        <v-container class="container-border">
          Beste <span class="arg-placeholder">#syndicus#</span>,
          <br/><br/>
          ...
          <br/><br/>
          Met vriendelijke groeten,
          <br/>
          <span class="arg-placeholder">#naam#</span>
        </v-container>
      </v-card-text>
      <div align="right">
        <NormalButton class="close-button-margin" text="Close" :parent-function="closeDialog"/>
      </div>
    </v-card>
  </v-dialog>

</template>

<script>
import {RequestHandler} from "@/api/RequestHandler";
import MailTemplateService from "@/api/services/MailTemplateService";

/**
 * CreateEditMailTemplate component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * edit: Boolean als je een mail template wilt bewerken of aanmaken
 */

import NormalButton from "@/components/NormalButton.vue";

export default {
  name: 'CreateEditMailTemplate',
  props: {
    edit: {
      type: Boolean,
      default: false
    },
  },
  components: {NormalButton},
  data: () => ({
    template: {
      name: '',
      text: ''
    },
    showDialog: false,
    tab: null
  }),
  methods: {
    async createTemplate () {
      if (this.template.name === '' || this.template.text === '') {
        return "Error"
      }
      return RequestHandler.handle(

        MailTemplateService.createMailTemplate(
          {
            name: this.template.name,
            content: this.template.text
          }
        ),
        {
        id: 'createMailTemplateError',
        style: "SNACKBAR",
      });
    },
    editTemplate: function () {
      // TODO object aanpassen in de backend + error handling
      console.log(this.template)
    },
    closeDialog: function () {
      this.showDialog = false
    }

  }, computed: {
    formattedText() {
      return this.template.text.replace(/#([^#]*)#/g, '<b>$1</b>');
    }
  },
  mounted() {
    if (this.edit) {
      // TODO data halen van de template die aangepast moet worden
      this.template.name = 'TODO data uitlezen van de backend'
      this.template.text = 'TODO data #uitlezen# van de backend'
    }
  }
}
</script>

<style scoped>
.arg-placeholder {
  font-weight: bold;
}

.close-button-margin {
  margin-right: 10px;
  margin-bottom: 10px;
}
</style>
