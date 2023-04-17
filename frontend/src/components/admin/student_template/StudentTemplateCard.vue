<template>
<v-card
    class="mx-auto w-75 my-10"
    variant="outlined"
    :to="`/studenttemplates/${data.id}`"
  >
    <v-card-item>
      <div>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-overline">
            {{ data.location }}
          </div>
          <div class="text-overline">
            {{ data.even ? "even" : "oneven" }}
          </div>
        </v-row>
        <v-row class="px-3 my-1 justify-space-between">
          <div class="text-h6">
            {{ data.name }}
          </div>
        </v-row>
      </div>
    </v-card-item>

    <v-card-actions class="px-3 my-1 justify-space-between">
      <div class="text-caption">{{ data.status }}</div>
      <v-btn variant="outlined" to="/unauthorized">
        Aanpassen
      </v-btn>
    </v-card-actions>
  </v-card>

</template>

<script>
export default {
  name: "StudentTemplateCard",
  props: {
    data: {
      type: Object,
      default: () => ({
        id: '1',
        name: 'Template Rondes Gent',
        location: 'Gent',
        even: true,
        status: 'actief'
      })
    }
  },
}
</script>

<style scoped>

</style>
