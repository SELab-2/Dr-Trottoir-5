<template>
  <v-container align="center">
     <v-card>
       <v-card-title class="mt-2">
        <v-row>
          <v-col md="6" sm="6">
            <DatePicker v-model.string="date" color="white" :is-dark="true" :is-required="true" show-iso-weeknumbers
                        :first-day-of-week="1" :masks="masks" :attributes="attrs" view="weekly" v-on:dayclick="changed" />
          </v-col>
          <v-col sm="6" align="left" class="text-wrap">
            <h4 class="text-h4">
              Opmerkingen voor {{building !== null ? building.name : ''}} op
              {{new Date(date).toLocaleDateString('nl-BE', {weekday: 'long', day: 'numeric', month: 'long'})}}
            </h4>
            <v-autocomplete
              label="Gebouw" :items="buildings" class="mt-4" style="width: 50%;"
              v-model="building" item-title="name" return-object
              variant="outlined" v-on:update:modelValue="changed"
            ></v-autocomplete>
          </v-col>
        </v-row>

         <v-card v-if="building !== null" elevation="0">
           <h6 class="text-h6 mb-1">QR-code voor gebouw {{building.name}}</h6>
           <QRCodeVue3
            :value="`https://sel2-5.ugent.be/gebouw/${building.buildingID}`"
            :width="200"
            :height="200"
            :qrOptions="{ typeNumber: 0, mode: 'Byte', errorCorrectionLevel: 'H' }"
            :dotsOptions="{ color: 'black', type: 'square' }"
            :cornersSquareOptions="{ type: 'square' }"
            imgclass="qr"
            :key="building.id"
           />
           <normal-button text="Reset QR-Code" :parent-function="() => dialog = true"></normal-button><br>
           <normal-button text="QR-Code uitprinten" :parent-function="printQR" class="mt-2"></normal-button>

           <v-dialog
            v-model="dialog"
            width="auto"
           >
            <v-card>
              <v-card-text>
                Weet u zeker dat u de QR-Code wilt resetten?<br>
                De vorige QR-Codes zullen hierdoor niet langer werken.
              </v-card-text>
              <v-card-actions>
                <v-btn color="primary" @click="dialog = false">Annuleren</v-btn>
                <v-btn color="warning" @click="() => { dialog = false; resetQR() }">Resetten</v-btn>
              </v-card-actions>
            </v-card>
           </v-dialog>
         </v-card>
      </v-card-title>
      <v-divider style="width: 90%;" class="mt-4"></v-divider>
       <v-card-text class="mt-3">
        <v-row justify="center">
          <v-col cols="4">
            <v-row justify="center" class="text-center">
              <v-col cols="12"><h1>Aankomst</h1></v-col>
              <br>
              <ul>
                <li v-for="(el) in this.arrivals" :key="el">
                  <v-col cols="12">
                    <FotoCardAdmin v-bind:data="el"/>
                  </v-col>
                </li>
              </ul>
              <p class="text-subtitle-1" v-if="this.arrivals.length === 0">Geen berichten beschikbaar.</p>
            </v-row>
          </v-col>

          <v-col cols="4">
            <v-row justify="center" class="text-center">
              <v-col cols="12"><h1>Berging</h1></v-col>
              <br>
              <ul>
                <li v-for="(el) in this.storages" :key="el">
                  <v-col cols="12">
                    <FotoCardAdmin v-bind:data="el"/>
                  </v-col>
                </li>
              </ul>
              <p class="text-subtitle-1" v-if="this.storages.length === 0">Geen berichten beschikbaar.</p>
            </v-row>
          </v-col>

          <v-col cols="4">
            <v-row justify="center" class="text-center">
              <v-col cols="12"><h1>Vertrek</h1></v-col>
              <br>
              <ul>
                <li v-for="(el) in this.departs" :key="el">
                  <v-col cols="12">
                    <FotoCardAdmin v-bind:data="el"/>
                  </v-col>
                </li>
              </ul>
              <p class="text-subtitle-1" v-if="this.departs.length === 0">Geen berichten beschikbaar.</p>
            </v-row>
          </v-col>
        </v-row>
       </v-card-text>
     </v-card>
  </v-container>
</template>

<script>
import { DatePicker } from 'v-calendar';
import 'v-calendar/dist/style.css';
import {RequestHandler} from "@/api/RequestHandler";
import RoundService from "@/api/services/RoundService";
import FotoCardAdmin from "@/components/admin/FotoCardAdmin.vue";
import { getWeek } from "@/api/DateUtil";
import PlanningService from "@/api/services/PlanningService";
import QRCodeVue3 from "qrcode-vue3";
import NormalButton from "@/components/NormalButton.vue";

export default {
  name: "SyndicusHome",
  components: {NormalButton, FotoCardAdmin, DatePicker, QRCodeVue3},
  data: () => ({
    date: new Date().toISOString().split('T')[0],
    buildings: [],
    arrivals: [],
    departs: [],
    storages: [],
    building: null,
    dialog: false,
    masks: { modelValue: 'YYYY-MM-DD' },
    attrs: [
      {
        dates: new Date(),
        popover: {
          label: 'Glas'
        },
        dot: 'yellow'
      },
      {
        dates: new Date(),
        popover: {
          label: 'GFT'
        },
        dot: 'green'
      }
    ]
  }),
  beforeMount() {
    RequestHandler.handle(RoundService.getBuildingsForSyndicus(), {
      id: "getBuildingsError",
      style: "NONE"
    }).then(buildings => {
      this.buildings = buildings;
      if (buildings.length > 0) this.building = buildings[0];
      this.changed();
    }).catch(() => null);
  },
  methods: {
    changed() {
      this.getStudentPosts();
    },
    resetQR() {
      RequestHandler.handle(RoundService.resetBuilding(this.building.buildingID), {
        id: 'resetBuildingError',
        style: 'NONE'
      }).then(() => {
        location.reload();
      }).catch(() => null)
    },
    printQR() {
      const iframe = document.createElement('iframe');
      iframe.style.height = 0;
      iframe.style.visibility = 'hidden';
      iframe.style.width = 0;
      iframe.setAttribute('srcdoc', '<html><body></body></html>');
      document.body.appendChild(iframe);

      iframe.addEventListener('load', function () {
          // Clone the image
          const image = document.getElementsByClassName('qr')[0].cloneNode();
          image.style.width = '80vw';

          // Add text to page
          const text = document.createElement('h1');
          text.innerHTML = 'Scan deze QR-Code om berichten over de afvalophaling te bekijken.';

          // Append the image to the iframe's body
          const body = iframe.contentDocument.body;
          body.style.textAlign = 'center';
          body.appendChild(image);
          body.appendChild(text);

          image.addEventListener('load', function() {
              // Invoke the print when the image is ready
              iframe.contentWindow.print();
          });
      });

      iframe.contentWindow.addEventListener('afterprint', function () {
          iframe.parentNode.removeChild(iframe);
      });
    },
    async getStudentPosts(){
      const date = new Date(this.date)
      let week = getWeek(date)
      if (date.getUTCDay() === 0) week -= 1;
      await RequestHandler.handle(PlanningService.getRounds(date.getFullYear(), week, date.getUTCDay(), this.building.location), {
        id: 'getRoundsError',
        style: 'NONE'
      }).then(async rounds => {
        for(const round of rounds){
          if(round.ronde.buildings.map(building => building.id).includes(this.building.id)){
            await RequestHandler.handle(PlanningService.getInfoOfBuilding(round.id, this.building.id), {
              id: 'getInfoOfBuildingError',
              style: 'NONE'
            }).then(async info => {
              await RequestHandler.handle(PlanningService.getPictures(info[0].id, date.getFullYear(), week), {
                id: 'getPicturesError',
                style: 'NONE'
              }).then(async pictures => {
                this.arrivals = []
                this.departs = []
                this.storages = []
                for(const picture of pictures){
                  if(picture.pictureType === "AR"){
                    this.arrivals.push(picture)
                  } else if(picture.pictureType === "DE"){
                    this.departs.push(picture)
                  } else if(picture.pictureType === "ST"){
                    this.storages.push(picture)
                  }
                }
              }).catch(() => {
                this.arrivals = []
                this.departs = []
                this.storages = []
              })
            }).catch(() => {
              this.arrivals = []
              this.departs = []
              this.storages = []
            })
          }
        }
      }).catch(() => {
        this.arrivals = []
        this.departs = []
        this.storages = []
      });
    }
  }
}
</script>
