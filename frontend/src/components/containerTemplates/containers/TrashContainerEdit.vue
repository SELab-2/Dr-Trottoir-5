<template>
  <v-row class="justify-center my-10">
    <div class="text-h2">Pas de container aan</div>
  </v-row>
  <v-card class="my-10 py-5 mx-auto w-75">
    <v-form fast-fail @submit.prevent>
      <v-row class="justify-space-between mx-auto">
        <v-col cols='12' md='6' sm='6'>
          <v-select
            :error-messages="check_errors(this.errors, 'type')"
            v-model="type"
            :items="types.map(type => ContainerType[type])"
            label="type container"
          ></v-select>
        </v-col>
        <v-col cols='12' md='6' sm='6'>
          <v-select
            :error-messages="check_errors(this.errors, 'day')"
            v-model="day"
            :items="days.map(day => Weekday[day])"
            label="dag van de week"
          ></v-select>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field v-model='start_hour' label='Beginuur' :error-messages="check_errors(this.errors, 'start_hour')" required></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field v-model='end_hour' label='Einduur' :error-messages="check_errors(this.errors, 'end_hour')" required></v-text-field>
        </v-col>
      </v-row>
      <StateButtons :status="this.status" :eenmalig="() => editContainer(true)" :permanent="() => editContainer(false)" />
      </v-form>
  </v-card>
</template>

<script lang="ts">
import {RequestHandler} from "@/api/RequestHandler";
import TrashTemplateService from "@/api/services/TrashTemplateService";
import {container_from_api, container_to_api, ContainerType} from "@/api/models/ContainerType";
import {Weekday, weekday_from_api, weekday_to_api} from "@/api/models/Weekday";
import router from '@/router';
import StateButtons from "@/components/StateButtons.vue";
import {check_errors, get_errors} from "@/error_handling";

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
    id: Number,
    containerId: Number
  },
  data: () => {
    return {
      id_: null,
      type: '',
      day: '',
      start_hour: '',
      end_hour: '',
      status: "I",
      smallScreen: false,
      errors: null,
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
    this.id_ = this.$route.params.id
    RequestHandler.handle(
      TrashTemplateService.getTrashContainersOfTemplateByExtraId(this.id_, this.$route.params.containerId),
      {
        id: 'getContainerforeditError',
        style: 'SNACKBAR'
      }
    ).then(result => {
      this.type = ContainerType[container_from_api(result.trash_container.type)]
      this.day = Weekday[weekday_from_api(result.trash_container.collection_day.day)]
      this.start_hour = result.trash_container.collection_day.start_hour
      this.end_hour = result.trash_container.collection_day.end_hour
    })
    RequestHandler.handle(
      TrashTemplateService.getTrashTemplate(this.id_),
      {
        id: 'getTrashtemplateError',
        style: 'SNACKBAR'
      }
    ).then(result => {
      this.status = result.status
    })
  },
  methods: {
    check_errors,
    async editContainer(eenmalig) {
      if(eenmalig) {
        TrashTemplateService.updateContainerTemplateEenmalig(this.id_, this.$route.params.containerId, {
          type: container_to_api(this.type),
          collection_day: {
            day: weekday_to_api(this.day),
            start_hour: this.start_hour,
            end_hour: this.end_hour
          },
        }
      ).then(() =>{
        this.$store.dispatch("snackbar/open", {
          message: "De container is aangepast",
          color: "success"
        })
        router.replace({name: 'trashtemplates'})
      }).catch(async (error) => {this.errors = await get_errors(error)})
      } else {
        TrashTemplateService.updateContainerTemplate(this.id_, this.$route.params.containerId, {
          type: container_to_api(this.type),
          collection_day: {
            day: weekday_to_api(this.day),
            start_hour: this.start_hour,
            end_hour: this.end_hour
          },
        }
      ).then( () =>{
        this.$store.dispatch("snackbar/open", {
          message: "De container is aangepast",
          color: "success"
        })
        router.replace({name: 'trashtemplateContainers', params: {id: this.id_}})
      }).catch(async (error) => {this.errors = await get_errors(error)})
      }
    },
  }
}
</script>
