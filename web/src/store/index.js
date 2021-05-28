import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

Vue.use(Vuex)

const initialState = {
}

export default new Vuex.Store({
  state: { ...{}, ...initialState },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
  plugins: [
      VuexPersistedstate({
          storage: window.localStorage
      })
  ]
})
