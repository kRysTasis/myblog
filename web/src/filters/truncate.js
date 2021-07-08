import Vue from 'vue'

Vue.filter('truncate', function (value, num, end) {
    if (!value) return ''
    var e = (end != null) ? end : '...'
    if (value.length >= num) return value.substr(0, num) + e
    return value
})
