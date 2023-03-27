import { snackbar } from './modules/snackbar'
import { modal } from './modules/modal'
import { session } from './modules/session'
import { createStore } from 'vuex'

export let store
store = createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    snackbar,
    modal,
    session
  }
})
