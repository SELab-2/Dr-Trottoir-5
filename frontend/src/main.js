import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import './registerServiceWorker'
import VueCookies from 'vue-cookies'

const Emitter = require('tiny-emitter')
const emitter = new Emitter() //error bus

loadFonts().then(r => {
  //Noop
})

createApp(App)
  .use(router)
  .use(store)
  .use(vuetify)
  .use(VueCookies, {
    // options
  })
  .mount('#app')
