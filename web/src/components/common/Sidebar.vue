<template>
    <div id="sidebar_wrap">
        <div id="sidebar_left" :class="{active: active}">
            <!-- <div class="box_1" :class="{noDisplay: !active}"></div> -->
            <p :class="{noDisplay: active}">krystasis's blog</p>
            <p :class="{noDisplay: !active, noDisplayTwo: activeTwo}">krystasis's post</p>
            <p :class="{noDisplay: !activeTwo}">krystasis's profile</p>
        </div>
        <div id="sidebar_left_under">
        </div>
        <!-- <div id="sidebar_right" :class="{active: active}">
        </div> -->
    </div>
</template>
<script>
    export default {
        name: 'Sidebar',
        components: {
        },
        props: {
        },
        data: () => ({
            scrollY: 0,
            active: false,
            activeTwo: false,
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            window.removeEventListener('scroll', this.handleScroll)
            window.addEventListener('scroll', this.handleScroll)
        },
        beforeUpdate () {
        },
        update () {
        },
        beforeDestroy () {
        },
        destoryd () {
        },
        watch: {
            scrollY: function (newValue, oldValue) {
                if (newValue > 300 && !this.active) {
                    this.active = true
                } else if (newValue <= 300) {
                    this.active = false
                }
                if (newValue > 3300) {
                    this.activeTwo = true
                } else if (newValue <= 3300) {
                    this.activeTwo = false
                }
            }
        },
        computed: {
        },
        methods: {
            handleScroll () {
                this.scrollY = window.scrollY
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #sidebar_wrap {
        height: 100%;
        width: 100%;
        // .active {
        //     background-color: rgba(100, 100, 100, 0.2);
        // }
        #sidebar_left {
            .noDisplay {
                display: none !important;
            }
            .noDisplayTwo {
                display: none;
            }
            .box_1 {
                position: absolute;
                top: 20%;
                width: 100%;
                background-color: rgba(20, 40, 10, 0.2);
                height: 1px;
            }
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 90px;
            p {
                position: relative;
                top: 34%;
                left: 30%;
                font-family: 'Quicksand', sans-serif;
                -ms-writing-mode: tb-rl;
                writing-mode: vertical-rl;
            }
        }
        #sidebar_left_under {
            position: fixed;
            top: 10%;
            left: 0;
            height: 100%;
            width: 90px;
            // border-right: 1px solid rgba(0, 0, 0, 0.1);
        }
        #sidebar_right {
            position: fixed;
            top: 0;
            right: 0;
            height: 100%;
            width: 90px;
            p {
                position: relative;
                top: 42%;
                left: 30%;
                font-family: 'Quicksand', sans-serif;
                -ms-writing-mode: tb-rl;
                writing-mode: vertical-rl;
            }
        }
    }
</style>
