import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

import auth from "./auth"
import admin from "./admin"
import ticket from "./ticket"
import checkTicket from "./checkTicket"
import recommendation from "./recommendation"

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
    admin,
    ticket,
    checkTicket,
    recommendation,
  },
})
