import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

Vue.use(Vuex)

const initialState = {
    activeFixed: false,
    scrollBottom: false,
    scrollY: 0,
    loadingTopPosts: false,
    loadingMainPosts: false,
    loadingDetailPost: false,
}

export default new Vuex.Store({
    state: { ...{}, ...initialState },
    getters: {
        scrollY: state => state.scrollY,
        activeFixed: state => state.activeFixed,
        scrollBottom: state => state.scrollBottom,
        loadingTopPosts: state => state.loadingTopPosts,
        loadingMainPosts: state => state.loadingMainPosts,
        loadingDetailPost: state => state.loadingDetailPost,
    },
    mutations: {
        setScrollY (state, payload) {
            state.scrollY = payload
        },
        setActiveFixed (state, payload) {
            state.activeFixed = payload
        },
        setScrollBottom (state, payload) {
            state.scrollBottom = payload
        },
        setLoadingTopPosts (state, payload) {
            state.loadingTopPosts = payload
        },
        setLoadingMainPosts (state, payload) {
            state.loadingMainPosts = payload
        },
        setLoadingDetailPost (state, payload) {
            state.loadingDetailPost = payload
        }
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
