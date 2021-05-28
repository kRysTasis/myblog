import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import http from '@/plugins/http'
import vuetify from './plugins/vuetify'
import Vuesax from 'vuesax'
import VueSession from 'vue-session'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import myRules from '@/assets/js/rules'
import eventHub from '@/plugins/eventHub'
import truncate from '@/filters/truncate'

import 'vuesax/dist/vuesax.css'
import 'boxicons/css/boxicons.min.css'
require('@/assets/scss/main.scss')

Vue.config.productionTip = false

Vue.use(http)
Vue.use(Vuesax)
Vue.use(VueSession)
Vue.use(eventHub)

myRules()

Vue.component('ValidationProvider', ValidationProvider)
Vue.component('ValidationObserver', ValidationObserver)

Vue.config.productionTip = false

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')
