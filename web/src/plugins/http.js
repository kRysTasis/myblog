import Vue from 'vue'
import axios from 'axios'

const http = {
    install: function (Vue, options) {
        Vue.prototype.$axios = axios.create({
            baseURL: 'http://localhost:8000',
            xsrfCookieName: 'csrftoken',
            xsrfHeaderName: 'X-CSRFTOKEN',
            timeout: 10000,
            headers: {
				common: {
					'Content-Type': 'application/json;charset=utf-8',
					'Access-Control-Allow-Origin': `${process.env.VUE_APP_AUTH_REDIRECT_URI}:8000`,
					'X-Requested-With': 'XMLHttpRequest',
					'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, X-HTTP-Method-Override, Accept',
					'Access-Control-Allow-Methods': 'PUT, DELETE, OPTIONS, POST, GET'
				}
			}
        })
    }
}

export default http
