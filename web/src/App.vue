<template>
    <v-app>
        <router-view/>
    </v-app>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        name: 'App',
        data: () => ({
        }),
        created () {
            window.removeEventListener('scroll', this.handleScroll)
            window.addEventListener('scroll', this.handleScroll)
        },
        watch: {
            scrollY: function (newValue, oldValue) {
                if (newValue > 300 && !this.activeFixed) {
                    this.setActiveFixed(true)
                } else if (newValue <= 300) {
                    this.setActiveFixed(false)
                }

                const clientHeight = document.getElementsByTagName('body')[0].clientHeight
                const footerHeight = document.getElementById('footer_wrap').clientHeight
                const targetHeight = clientHeight - footerHeight - 400

                if (newValue > targetHeight) {
                    this.setScrollBottom(true)
                } else if (newValue <= targetHeight) {
                    this.setScrollBottom(false)
                }
            }
        },
        computed: {
            ...mapGetters([
                'scrollY',
                'activeFixed',
                'scrollBottom'
            ]),
        },
        methods: {
            ...mapMutations([
                'setScrollY',
                'setActiveFixed',
                'setScrollBottom'
            ]),
            handleScroll () {
                this.setScrollY(window.scrollY)
            }
        }
    }
</script>

<style lang="scss">
</style>
