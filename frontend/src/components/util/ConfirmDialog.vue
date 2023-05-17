<!--
  ConfirmDialog component.
  A component that stars a dialog to confirm if an action needs to be executed.
  To open the dialog you add a ref tag to the dialog component and
  add $refs.`value of ref`.open() as a method to an action component.
  For example:
   <btn @click="$refs.confirm.open()" ></btn>
   <ConfirmDialog ref="confirm" text="test" :confirm_function="() => console.log("test")"></ConfirmDialog>
-->
<template>
<v-dialog v-model="dialog" content-class="d-flex align-center justify-end">
    <v-card class="overflow-hidden h-50 w-50">
      <v-row>
        <v-col md="12" lg="12" class="d-flex align-center justify-center pt-10">
          <p>
            {{text}}
          </p>
        </v-col>
        <v-col md="6" lg="6" class="d-flex align-center justify-end pb-10">
          <v-btn data-test="confirm_button" @click="confirm_function">Ja</v-btn>
        </v-col>
        <v-col md="6" lg="6" class="d-flex align-center justify-start pb-10">
          <v-btn data-test="close_button" @click="dialog = false">Nee</v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: "ConfirmDialog.vue",
  props: {
    text: { type: String },
    confirm_function: { type: Function }
  },
  data: () => {
    return {
      dialog: false
    }
  },
  methods: {
    open() {
      this.dialog = true
    }
  }
}
</script>
