<template>
  <v-row>
    <v-btn icon="mdi-delete"></v-btn>
    <v-btn icon="mdi-pencil" ></v-btn>
    <v-col>
      {{data.name}}
    </v-col>
    <v-col>
      <h1>Adres</h1>
    </v-col>
    <v-col>
      {{data.adres}}
    </v-col>
    <v-col>
      <h1>Klanten nummer</h1>
    </v-col>
    <v-col>
      <h1>
        {{data.ivago_klantnr}}
      </h1>
    </v-col>
    <v-col>
      <h1>Vuilnis planning {{data.name}}</h1>
    </v-col>
    <!-- Add list of planning cards -->
    <v-col>
      <normal-button text="Nieuwe ophaling" :parent-function="() => {}"></normal-button>
    </v-col>
  </v-row>
</template>

<script>
import NormalButton from "@/components/NormalButton";
export default {
  name: "AdminBuildingView",
  components: {NormalButton},
  props: {
    data: {
      type: Object,
      default: () => ({
        name: 'Empty',
        adres: 'Empty',
        manual: null,
        ivago_klantnr: 0,
        planningen: []
      })
    }
  },
}
</script>

