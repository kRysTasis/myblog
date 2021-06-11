<template>
    <div id="header_area_wrap">
        <v-card
            flat
            tile
            class="header_wrap"
        >
            <div id="header_top">
                <v-row>
                    <!-- <v-spacer/> -->
                    <v-col cols="3" class="header_top_left">
                        <v-btn
                            icon
                            class="header_top_grid"
                        ><i class='bx bx-menu-alt-left'></i>
                        </v-btn>
                    </v-col>
                    <v-col cols="6" class="header_top_title">
                        <v-card-title>krystasis</v-card-title>
                    </v-col>
                    <v-col cols="3" class="header_top_right">
                        <vs-input
                            class="header_top_search"
                            v-model="searchText"
                            placeholder="search..."
                        >
                            <template #icon>
                                <i class='bx bx-search'></i>
                            </template>
                        </vs-input>
                    </v-col>
                </v-row>
            </div>
            <div id="header_middle">
                <v-row>
                    <v-spacer/>
                    <v-col
                        cols="2"
                        class="sns_icon_area_wrap"
                    >
                        <i
                            class='bx bxl-github fa-lg github_icon mr-1'
                            @click.stop.prevent='openMyGithub()'
                        ></i>
                        <i
                            class="fab fa-twitter fa-lg twitter_icon"
                            @click.stop.prevent="openMyTwitter()"
                        ></i>
                    </v-col>
                </v-row>
            </div>
        </v-card>
        <div id="header_bottom">
            <HeaderBottom/>
        </div>
    </div>
</template>
<script>
    import HeaderBottom from '@/components/common/HeaderBottom'
    import { Const } from '@/assets/js/const'

    const Con = new Const()

    export default {
        name: 'Header',
        components: {
            HeaderBottom
        },
        props: {
        },
        data: () => ({
            searchText: '',
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
        },
        methods: {
            openMyGithub () {
                window.open(Con.MY_GITHUB_URL, '_blink')
            },
            openMyTwitter () {
                window.open(Con.MY_TWITTER_URL, '_blink')
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #header_area_wrap {
        width: 100%;
        height: 250px;
        .header_wrap {
            width: 1200px;
            margin: 0 auto;
            #header_top {
                width: 100%;
                height: 180px;
                .v-card__title::v-deep {
                    display: block;
                    text-align: center;
                    font-size: 40px;
                }
                padding-top: 20px;
                .header_top_title {
                    font-family: 'Kaushan Script', cursive;
                    padding-top: 45px;
                }
                .header_top_left {
                    .header_top_grid {
                    }
                }
                .header_top_right {
                    .header_top_search {
                        float: right;
                    }
                }
            }
            #header_middle {
                width: 100%;
                height: 40px;
                .sns_icon_area_wrap {
                    padding-left: 50px;
                    .github_icon{
                        cursor: pointer;
                    }
                    .twitter_icon {
                        cursor: pointer;
                        color: rgba(0,172,238,0.5);
                    }
                }
            }
            .vs-input-content {
                margin: 0 auto;
            }
        }
    }
</style>
