<template>
    <div id="font_sidebar_wrap">
        <div id="font_sidebar_left" :class="{active: activeFixed}">
            <!-- <div class="box_1" :class="{noDisplay: !active}"></div> -->
            <p :class="{noDisplay: activeFixed}">krystasis's blog</p>
            <p :class="{noDisplay: !activeFixed, noDisplayTwo: scrollBottom}">krystasis's post</p>
            <p :class="{noDisplay: !scrollBottom}">krystasis's profile</p>
        </div>
        <div id="font_sidebar_left_under">
        </div>
        <!-- <div id="font_sidebar_right" :class="{active: activeFixed}"></div> -->
        <div v-if="!mounting" id="font_sidebar_right_bottom">
            <v-btn
                fab
                @click="toTop"
                class="font_sidebar_right_bottom_btn"
                :class="{activeToTop: activeToTop, noDisplay: (noDisplayActiveToTop && !mounting)}"
            >
                <i class='bx bxs-chevron-up font_sidebar_right_bottom_icon'></i>
            </v-btn>
        </div>
    </div>
</template>
<script>
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        name: 'FontSidebar',
        components: {
        },
        props: {
        },
        data: () => ({
            mounting: true,
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            this.mounting = false
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
            activeToTop: function (newVal, oldVal) {
                if (!newVal && oldVal) {
                    this.setNoDisplayActiveToTop(true)
                }
            },
            noDisplayActiveToTop: function (newVal, oldVal) {
            }
        },
        computed: {
            ...mapGetters([
                'activeFixed',
                'activeToTop',
                'noDisplayActiveToTop',
                'scrollBottom',
                'scrollY',
            ])
        },
        methods: {
            ...mapMutations([
                'setNoDisplayActiveToTop'
            ]),
            toTop () {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        50% {
            opacity: 0.4;
        }
        100% {
            opacity: 1;
        }
    }
    @keyframes fadeOut {
        0% {
            opacity: 1;
        }
        50% {
            opacity: 0.6;
        }
        100% {
            opacity: 0;
        }
    }
    #font_sidebar_wrap {
        height: 100%;
        width: 100%;
        // .active {
        //     background-color: rgba(100, 100, 100, 0.2);
        // }
        #font_sidebar_left {
            background-color: rgba(60,60,60,0.8);
            color: white;
            z-index: 10000;
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
                // font-family: 'Kaushan Script', cursive !important;
	            // font-family: 'Bangers', cursive;
                // font-family: 'Kaushan Script', cursive;
                // font-family: 'Vollkorn', serif;
                // font-family: 'Teko', sans-serif;
                // font-family: 'Roboto Condensed', sans-serif;
                // font-family: 'Londrina Shadow', cursive;
                font-family: 'IM Fell DW Pica SC', serif;
                // font-family: 'Economica', sans-serif;
                // font-family: 'Quicksand', sans-serif;
                -ms-writing-mode: tb-rl;
                writing-mode: vertical-rl;
            }
        }
        #font_sidebar_left_under {
            position: fixed;
            top: 10%;
            left: 0;
            height: 100%;
            width: 90px;
            // border-right: 1px solid rgba(0, 0, 0, 0.1);
        }
        #font_sidebar_right {
            background-color: rgba(20,20,20,0.8);
            color: white;
            z-index: 1;
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
        #font_sidebar_right_bottom {
            position: fixed;
            right: 60px;
            bottom: 60px;
            .font_sidebar_right_bottom_btn {
                opacity: 0;
            }
            .activeToTop {
                display: block;
                opacity: 0;
                animation: fadeIn 0.4s ease-out 0s 1 normal forwards;
            }
            .noDisplay {
                display: none;
                animation: fadeOut 0.4s ease-out 0s 1 normal forwards;
            }
            .font_sidebar_right_bottom_icon {
                font-size: 30px;
                color: rgba(50, 50, 50, 0.6);
            }
        }
    }
</style>
