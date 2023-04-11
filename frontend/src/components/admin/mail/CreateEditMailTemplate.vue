<template>
  <v-container>
    <h1 align="center">Template aanmaken</h1>
    <v-form>
      <p>Naam</p>
      <v-text-field v-model="this.template.name"></v-text-field>
      <p>Tekst
        <v-avatar class="button-style" size="25px" style="border: 1px solid #E3e3e3;border-radius: 25px;">
          <v-icon size="25px" dark color="gray" @click="showDialog = true">mdi-information-variant</v-icon>
        </v-avatar>
      </p>
      <v-textarea v-model="this.template.text" auto-grow style="margin-top: 5px"></v-textarea>
    </v-form>
    <div align="center">
      <NormalButton text="Maak template aan" :parent-function="createTemplate"/>
    </div>

    <v-dialog v-model="showDialog">
      <v-card class="container-border">
        <v-card-title>Info argumenten</v-card-title>
        <v-card-text>
          Argumenten worden altijd aangeduid door twee <span class="arg-placeholder">#</span> te gebruiken rond het argument:
          <br/><br/>
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

  </v-container>
</template>

<script>
import NormalButton from "@/components/NormalButton.vue";

export default {
  name: 'CreateEditMailTemplate',
  components: {NormalButton},
  data: () => ({
    template: {
      name: '',
      text: ''
    },
    showDialog: false
  }),
  methods: {
    createTemplate: function () {
      // TODO
      console.log(this.template)
    },
    closeDialog: function () {
      this.showDialog = false
    }
  }
}
</script>

<style scoped>
.arg-placeholder {
  font-weight: bold;
}
.close-button-margin{
  margin-right: 10px;
  margin-bottom: 10px;
}
</style>
