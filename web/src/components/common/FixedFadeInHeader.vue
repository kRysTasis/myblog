<template>
    <div
        class="fixed_header_area_wrap"
        :class="{activeFixed: activeFixed, noDisplay: !activeFixed}"
    >
        <v-container fluid class="fixed_header_area">
            <v-row>
                <v-col cols="3">
                    <p
                        class="fixed_header_icon"
                        @click="toTop"
                    >krystasis</p>
                </v-col>
                <v-spacer/>
                <v-col cols="6" class="fixed_header_menu_area">
                    <HeaderBottom/>
                </v-col>
                <v-col cols="1">
                    <i
                        class='bx bx-search fixed_header_search_btn'
                        @click="showSearchArea"
                    ></i>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>
<script>
    import { mapGetters, mapMutations } from 'vuex'
    import HeaderBottom from '@/components/parts/HeaderBottom'

    export default {
        name: 'FixedHeader',
        components: {
            HeaderBottom
        },
        props: {
        },
        data: () => ({
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
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
        },
        computed: {
            ...mapGetters([
                'activeFixed',
            ])
        },
        methods: {
            ...mapMutations([
                'setScrollBottom'
            ]),
            showSearchArea () {
                this.activeFixedSearchArea = true
            },
            hideSearchArea () {
                this.activeFixedSearchArea = false
            },
            toTop () {
                if (this.$route.name === 'Home') {
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    })
                } else {
                    this.setScrollBottom(false)
                    this.$router.push('/')
                }
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
    @keyframes slideTopIn {
        0% {
            opacity: 0;
            transform: translateY(-30px);
        }
        50% {
            opacity: 0.4;
            transform: translateY(-10px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes slideLeftIn {
        0% {
            opacity: 0;
            transform: translateX(-30px);
        }
        10% {
            opacity: 0.1;
            transform: translateX(-22px);
        }
        20% {
            opacity: 0.2;
            transform: translateX(-16px);
        }
        30% {
            opacity: 0.3;
            transform: translateX(-10px);
        }
        40% {
            opacity: 0.4;
            transform: translateX(-3px);
        }
        50% {
            opacity: 0.6;
            transform: translateX(2px);
        }
        60% {
            opacity: 0.7;
            transform: translateX(10px);
        }
        70% {
            opacity: 0.8;
            transform: translateX(4px);
        }
        80% {
            opacity: 0.9;
            transform: translateX(-3px);
        }
        90% {
            opacity: 1;
            transform: translateX(-1px);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }
    @keyframes slideRightIn {
        0% {
            opacity: 0;
            transform: translateX(30px);
        }
        50% {
            opacity: 0.4;
            transform: translateX(10px);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .fixed_header_area_wrap {
        background-color: rgba(100,100,100,0.2);
        padding-top: 10px;

        .fixed_header_area {
            max-width: 100%;
            padding-left: 0;
            .fixed_header_icon {
                cursor: pointer;
                font-family: 'Kaushan Script', cursive;
                font-size: 25px;
                opacity: 0;
                animation: slideLeftIn 0.4s ease-out 0.2s 1 normal forwards running;
                padding-left: 125px;
            }

            .fixed_header_grid {
                position: relative;
                top: -5px;
                left: 10px;
                opacity: 0;
                animation: slideLeftIn 0.3s ease-out 0.2s 1 normal forwards running;
            }

            .fixed_header_menu_area {
                opacity: 0;
                animation: slideTopIn 0.3s ease-out 0.2s 1 normal forwards running;
            }

            .fixed_header_search_btn {
                opacity: 0;
                position: relative;
                top: 4px;
                left: 5px;
                text-align: center;
                display: block;
                cursor: pointer;
                animation: slideRightIn 0.3s ease-out 0.2s 1 normal forwards running;
            }
        }
    }
</style>
