<template>
  <v-card class='px-4'>
    <h1>Should be the navbar</h1>
    <v-spacer></v-spacer>
  </v-card>
  <v-container fluid class="bg-background">
    <v-row col="6" class="pl-md-16">
      <v-col>
        <h1>Voornaam</h1>
      </v-col>
      <v-col>
        <h1>Achternaam</h1>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <v-card height="40px" width="450px" style="padding-left: 5px; padding-top: 5px">
          {{ voornaam }}
        </v-card>
      </v-col>
      <v-col>
        <v-card height="40px" width="450px" style="padding-left: 5px; padding-top: 5px">
          {{ achternaam }}
        </v-card>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <h1>E-mail</h1>
      </v-col>
      <v-col>
        <h1>Wachtwoord</h1>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <v-card height="40px" width="450px" style="padding-left: 5px; padding-top: 5px">
          {{ email }}
        </v-card>
      </v-col>
      <v-col>
        <v-text-field hide-details
                      :readonly="edit === false"
                      v-model="password"
                      :type="show ?'text': 'password'"
                      style="padding-left: 5px; padding-top: 5px; width: 450px; height:40px"
                      :append-icon="show ? 'mdi-eye':'mdi-eye-off'" @click:append="show=!show">
        </v-text-field>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <h1>GSM</h1>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <v-card height="40px" width="450px" style="padding-left: 5px; padding-top: 5px">
          {{ gsm }}
        </v-card>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <h1>Rollen</h1>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <template v-for="rol in ['Student', 'Superstudent', 'Admin']" :key="rol">
        <v-checkbox :model-value="rol in roles" :readonly="edit === false && !('AD' in roles)" value='true'
                    :label="rol"></v-checkbox>
      </template>
    </v-row>
    <v-row col="6" class="pl-16">
      <v-col>
        <h1>Rondes</h1>
      </v-col>
    </v-row>
    <v-row col="6" class="pl-16">
      <template v-for="ronde in ['Ronde 1']" :key="ronde">
        <v-checkbox :model-value="ronde in rondes" readonly :label="ronde"></v-checkbox>
      </template>
    </v-row>
    <v-row>
      <v-col class="d-flex justify-center align-center" col="12">
        <v-btn>Pas aan</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => {
    return {
      voornaam: 'Kai',
      achternaam: 'Hozée',
      email: 'kaihozee@test.com',
      password: 'test',
      gsm: '+324',
      show: false,
      roles: [],
      rondes: [],
      edit: false
    }
  }
}
</script>
