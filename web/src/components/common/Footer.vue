<template>
    <div id="footer_wrap">
        <div
            id="footer_top"
        >
            <v-container fluid class="footer_top_container">
                <v-row>
                    <v-col
                        cols="7"
                    >
                        <v-row>
                            <v-col cols="4">
                                <v-card-subtitle class="footer_subtitle">
                                    ABOUT
                                </v-card-subtitle>
                                <div v-if="loading">
                                    <v-skeleton-loader
                                        v-bind="attrs"
                                        type="image"
                                    ></v-skeleton-loader>
                                </div>
                                <div v-else>
                                    <v-img
                                        lazy-src="https://picsum.photos/id/11/10/6"
                                        src="@/assets/img/krystasis.png"
                                        width="200"
                                        height="200"
                                        class="my_image"
                                    ></v-img>
                                </div>
                            </v-col>
                            <v-col cols="8" class="pl-0 ml-0">
                                <div class="profile_area">
                                    <v-card-subtitle class="myname footer_text">
                                        krystasis
                                    </v-card-subtitle>
                                    <v-card-text
                                        class="description footer_text"
                                        style="white-space:pre-wrap;"
                                    >
                                        {{ user.description }}
                                    </v-card-text>
                                </div>
                            </v-col>
                        </v-row>
                    </v-col>
                    <v-col
                        cols="4"
                    >
                        <v-card-subtitle class="footer_subtitle">
                            TAG
                        </v-card-subtitle>
                        <div class="tag_name_area">
                            <span
                                v-for="(tag, i) in tags"
                                :key="i"
                                @click="searchTag(tag)"
                                class="tag_name footer_text"
                            >
                                {{ tag.name }}
                            </span>
                        </div>
                        <v-card-subtitle class="footer_subtitle">
                            SNS
                        </v-card-subtitle>
                        <div
                            class="sns_icon_area_wrap"
                        >
                            <SnsIcons/>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <v-divider/>
        <div
            id="footer_bottom"
        >
            <v-card-text class="px-0 mx-0">
                ©krystasis.inc
            </v-card-text>
        </div>
    </div>
</template>
<script>
    import SnsIcons from '@/components/common/SnsIcons'

    export default {
        name: 'Footer',
        components: {
            SnsIcons
        },
        props: {
        },
        data: () => ({
            loading: true,
            attrs: {
                class: 'mb-6',
                boilerplace: true,
                elevation: 2,
            },
            tags: [],
            user: {}
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            this.getTags()
            this.getUser()
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
            searchTag (tag) {
                this.$router.push({
                    path: `/tag/${tag.slug}`
                })
            },
            getTags () {
                this.$axios({
                    url: '/api/tags/',
                    method: 'GET',
                })
                .then(res => {
                    this.loading = false
                    console.log(res.data)
                    this.tags = res.data
                })
                .catch(e => {
                    console.log(e)
                })
            },
            getUser () {
                this.$axios({
                    url: '/api/users/',
                    method: 'GET',
                })
                .then(res => {
                    this.loading = false
                    console.log(res.data)
                    this.user = res.data[0]
                })
                .catch(e => {
                    console.log(e)
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #footer_wrap {
        // border: 1px solid black;
        margin-top: 60px;
        padding-top: 30px;
        background-color: rgba(100, 100, 100, 0.1);
        width: 100%;
        height: auto;
        .footer_subtitle {
            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;
            // font-family: 'Vollkorn', serif;
            font-size: 25px;
        }
        .footer_text {
            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;
        }
        #footer_top {
            width: 1200px;
            margin: 0 auto;
            padding-bottom: 45px;
            .v-card__text {
                word-break: break-all;
            }
            .footer_top_container {
                padding: 0;
                .my_image {
                    margin-top: 10px;
                    margin-left: 10px;
                }
                .profile_area {
                    padding-top: 10px;
                    margin-left: 10px;
                    .myname {
                    }
                    .description {
                    }
                }
                .tag_name_area {
                    padding-left: 30px;
                    height: 100px;
                    font-size: 13px;
                    .tag_name {
                        cursor: pointer;
                    }
                }
            }
        }
        #footer_bottom {
            background-color: rgba(200, 200, 200, 0.3);
            width: 100%;
            height: 60px;
            text-align: center;
            font-family: 'Alegreya Sans SC', sans-serif;
        }
    }
</style>
