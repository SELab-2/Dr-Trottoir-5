<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Maak een nieuwe container aan</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="type"
            :items="types.map(type => ContainerType[type])"
            label="type container"
          ></v-select>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            v-model="day"
            :items="days.map(day => Weekday[day])"
            label="Dag van de week"
          ></v-select>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field v-model='start_hour' label='Beginuur' required></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field v-model='end_hour' label='Einduur' required></v-text-field>
        </v-col>
      </v-row>
      <v-row v-if="status !== 'V'" class="px-5 justify-center mx-auto">
        <v-col class="d-flex justify-center ml-auto mx-auto" cols="12" md="3" sm="3">
          <v-btn class="overflow-hidden" @click="createContainer()">Aanmaken</v-btn>
        </v-col>
      </v-row>
        <div v-if="status === 'V'" class="px-3 text-caption">Om deze template aan te passen moeten eerst de eenmalige aanpassingen ongedaan worden.</div>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import {container_to_api, ContainerType} from "@/api/models/ContainerType";
import {Weekday, weekday_to_api} from "@/api/models/Weekday";
import router from "@/router";
import StateButtons from "@/components/StateButtons.vue";

export default {
  name: 'CreateTrashContainerView',
  components: {StateButtons},
  computed: {
    Weekday() {
      return Weekday
    },
    ContainerType() {
      return ContainerType
    }
  },
  props: {
    id: Number
  },
  data: () => {
    return {
      type: '',
      day: '',
      start_hour: '',
      end_hour: '',
      smallScreen: false,
      status: "I",
      types: [
        ContainerType.GFT,
        ContainerType.PMD,
        ContainerType.PK,
        ContainerType.GLAS,
        ContainerType.REST,
      ],
      days: [
        Weekday.Zondag,
        Weekday.Maandag,
        Weekday.Dinsdag,
        Weekday.Woensdag,
        Weekday.Donderdag,
        Weekday.Vrijdag,
        Weekday.Zaterdag,
      ]
    }
  },
  beforeMount() {
    RequestHandler.handle(
      TrashTemplateService.getTrashTemplate(this.id),
      {
        id: 'getTrashtemplateError',
        style: 'SNACKBAR'
      }
    ).then(result => {
      this.status = result.status
    })
  },
  methods: {
    createContainer() {

      RequestHandler.handle(
        TrashTemplateService.newContainerToTemplate(this.id, {
          type: container_to_api(this.type),
          collection_day: {
            day: weekday_to_api(this.day),
            start_hour: this.start_hour,
            end_hour: this.end_hour
          },
        }), {
          id: 'createContainerTemplateError',
          style: 'SNACKBAR'
        }
      ).then(() => {
          this.$store.dispatch("snackbar/open", {
            message: "De container is aangemaakt",
            color: "success"
          })
          router.push({name: 'trashtemplateContainers', params: {id: this.id}})
        }
      )
    },
  }
}
</script>
