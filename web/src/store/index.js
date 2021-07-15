import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

Vue.use(Vuex)

const initialState = {
    activeFixed: false,
    activeToTop: false,
    noDisplayActiveToTop: false,
    scrollBottom: false,
    scrollY: 0,
    loadingTopPosts: false,
    loadingMainPosts: false,
    loadingDetailPost: false,
    userInfo: {},
    tags: [],
}

export default new Vuex.Store({
    state: { ...{}, ...initialState },
    getters: {
        activeFixed: state => state.activeFixed,
        activeToTop: state => state.activeToTop,
        noDisplayActiveToTop: state => state.noDisplayActiveToTop,
        scrollBottom: state => state.scrollBottom,
        scrollY: state => state.scrollY,
        loadingTopPosts: state => state.loadingTopPosts,
        loadingMainPosts: state => state.loadingMainPosts,
        loadingDetailPost: state => state.loadingDetailPost,
        userInfo: state => state.userInfo,
        tags: state => state.tags,
    },
    mutations: {
        setActiveFixed (state, payload) {
            state.activeFixed = payload
        },
        setActiveToTop (state, payload) {
            state.activeToTop = payload
        },
        setNoDisplayActiveToTop (state, payload) {
            state.noDisplayActiveToTop = payload
        },
        setScrollBottom (state, payload) {
            state.scrollBottom = payload
        },
        setScrollY (state, payload) {
            state.scrollY = payload
        },
        setLoadingTopPosts (state, payload) {
            state.loadingTopPosts = payload
        },
        setLoadingMainPosts (state, payload) {
            state.loadingMainPosts = payload
        },
        setLoadingDetailPost (state, payload) {
            state.loadingDetailPost = payload
        },
        setUserInfo (state, payload) {
            state.userInfo = payload
        },
        setTags (state, payload) {
            state.tags = payload
        }
    },
    actions: {
        getUserInfoAction (ctx, kwargs) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    url: '/api/users/',
                    method: 'GET',
                })
                .then(res => {
                    console.log(res.data)
                    this.commit('setUserInfo', res.data[0])
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    reject(e)
                })
            })
        },
        getTagsAction (ctx, kwargs) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    url: '/api/tags/',
                    method: 'GET',
                })
                .then(res => {
                    console.log(res.data)
                    this.commit('setTags', res.data)
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    reject(e)
                })
            })
        }
    },
    modules: {
    },
    plugins: [
        VuexPersistedstate({
            storage: window.localStorage
        })
    ]
})
