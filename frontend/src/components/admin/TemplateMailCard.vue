<template>
  <v-container class="container-border">
    <v-row>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ data.name }}</p>
      </v-col>
      <v-col cols="3" class="d-flex align-center">
        <p>{{ this.argsCount }}</p>
      </v-col>
      <v-col/>
      <v-col cols="3" class="d-flex align-center justify-end">
        <v-btn icon tile class="button-margin" style="max-height: 35px; max-width: 35px;" v-on:click="goToEditPage">
          <EditIcon/>
        </v-btn>
        <v-btn icon tile class="button-style" v-on:click="deletePost">
          <DeleteIcon/>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import EditIcon from '../icons/EditIcon.vue'
import DeleteIcon from '../icons/DeleteIcon.vue'
import MailTemplate from "@/api/models/MailTemplate";
import {RequestHandler} from "@/api/RequestHandler";
import router from "@/router";
import EmailTemplateService from "@/api/services/EmailTemplateService";

/**
 * TemplateMailCard component wordt gebruikt door als props een Object met de volgende keys mee te geven:
 * name: String
 * argsCount: Number
 */

export default {
  name: 'TemplateMailCard',
  props: {
    data: {
      type: MailTemplate,
      required: true
    }
  },
  data: () => ({
    argsCount: 0
  }),
  methods: {
    goToEditPage: function () {
      router.push({name: 'mail-template-edit', params: {id: this.data.id}})
    },
    deletePost: async function () {
      await RequestHandler.handle(EmailTemplateService.deleteEmailTemplateById(this.data.id))
        .then( () => window.location.reload())
    }
  },
  components: {
    EditIcon,
    DeleteIcon
  },
  mounted() {
    const count = this.data.content.match(/#([^#]*)#/g)
    if (count !== null) {
      this.argsCount = count.length
    }
  }
}
</script>

<style scoped>

</style>
