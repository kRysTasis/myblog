<template>
    <v-card
        flat
        tile
        class="content_top"
    >
        <div id="content_top_wrap">
            <div id="content_top">
                <v-container fluid class="content_top_top_post">
                    <v-card-title
                        class="content_top_category_title"
                    >
                        pickup posts
                    </v-card-title>
                    <v-row>
                        <v-col
                            v-for="(topPost, i) in topPosts"
                            :key="i"
                            cols="6"
                            class="post_area"
                            @click="showDetailPost(topPost)"
                        >
                                <div v-if="loadingTopPosts">
                                    <v-row>
                                        <v-col cols="12" class="px-3 mx-0">
                                            <v-skeleton-loader
                                                v-bind="attrs"
                                                type="card"
                                                height="300px"
                                            ></v-skeleton-loader>
                                        </v-col>
                                    </v-row>
                                </div>
                                <div v-else>
                                    <v-row>
                                        <v-col cols="12" class="px-1">
                                            <v-img
                                                :aspect-ratio="16/9"
                                                :lazy-src=lazySrc
                                                :src="topPost.thumbnail"
                                                class="topPost_img"
                                            ></v-img>
                                        </v-col>
                                        <div
                                            v-if="i == 0"
                                            class="content_top_category_title_on_img"
                                        >pickup posts</div>
                                    </v-row>
                                </div>
                                <v-row>
                                    <v-col cols="12" class="px-0 topPost_title">
                                        <v-card-subtitle class="content_top_title">
                                            <h1>{{ topPost.title | truncate(30) }}</h1>
                                        </v-card-subtitle>
                                    </v-col>
                                </v-row>
                        </v-col>
                    </v-row>
                </v-container>

                <v-container fluid class="content_top_pickup_post">
                    <v-row>
                        <v-col
                            v-for="(pickupPost, i) in pickupPosts"
                            :key="i"
                            cols="4"
                            class="post_area"
                            @click="showDetailPost(pickupPost)"
                        >
                            <div v-if="loadingTopPosts">
                                <v-row>
                                    <v-col cols="12" class="px-3 mx-0">
                                        <v-skeleton-loader
                                            v-bind="attrs"
                                            type="card"
                                            height="200px"
                                        ></v-skeleton-loader>
                                    </v-col>
                                </v-row>
                            </div>
                            <div v-else>
                                <v-row>
                                    <v-col cols="12" class="px-1 mx-0">
                                        <v-img
                                            :aspect-ratio="16/9"
                                            :lazy-src=lazySrc
                                            :src="pickupPost.thumbnail"
                                            class="pickupPost_img"
                                        ></v-img>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12" class="px-1 pickupPost_title">
                                        <v-card-subtitle class="pl-0 ml-0 content_top_title">
                                            <h1>{{ pickupPost.title | truncate(30) }}</h1>
                                        </v-card-subtitle>
                                    </v-col>
                                </v-row>
                            </div>
                        </v-col>
                    </v-row>
                </v-container>
            </div>
        </div>
    </v-card>
</template>
<script>
    import { Const } from '@/assets/js/const'
    import { mapGetters } from 'vuex'
    import pageMixin from '@/mixins/page'
    const Con = new Const()

    export default {
        name: 'ContentTop',
        components: {
        },
        props: {
            topPosts: {
                type: Array,
                required: true,
                default: () => [{}, {}]
            },
            pickupPosts: {
                type: Array,
                required: true,
                default: () => [{}, {}, {}]
            }
        },
        data: () => ({
            attrs: {
                class: 'mb-6',
                boilerplace: false,
                elevation: 2,
            },
            lazySrc: Con.LAZYSRC,
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
                'loadingTopPosts',
            ])
        },
        methods: {
            showDetailPost (post) {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                })
                setTimeout(this.toDetailPost, 200, post)
            },
            toDetailPost (post) {
                this.$router.push({
                    name: 'DetailPost',
                    params: {
                        id: post.id
                    }
                })
            },
        },
        mixins: [pageMixin],
    }
</script>
<style lang="scss" scoped>
    @keyframes hoverUp {
        0% {
            box-shadow: 1px 2px 2px rgba(60, 60, 60, 0.7);
            transform: translateY(0);
        }
        50% {
            box-shadow: 4px 3px 4px 1px rgba(80, 80, 80, 0.4);
            transform: translateY(-1px);
        }
        100% {
            box-shadow: 4px 3px 5px 2px rgba(100, 100, 100, 0.3);
            transform: translateY(-2px);
        }
    }
    #content_top_wrap {
        // background-color: rgba(232,237,205,0.4);
        #content_top {
            width: 1200px;
            margin: 40px auto 0 auto;
            // padding-top: 30px;
            padding-bottom: 10px;

            .post_area {
                box-shadow: 1px 2px 3px rgba(110, 100, 100, 0.3);
                cursor: pointer;
                position: relative;
                // box-shadow: 2px 3px 2px 2px rgba(100, 100, 100, 0.1);
                .topPost_title{
                    position: absolute;
                    bottom: 10px;
                    left: 0;
                }

                .pickupPost_title{
                    position: absolute;
                    bottom: 0;
                    left: 20px;
                }

                .content_top_title {
                    color: white;
                    // font-family: 'Quicksand', sans-serif;
                    // font-family: 'Caveat', cursive;
                    font-family: 'Homemade Apple', cursive;
                    h1 {
                        font-size: 17px;
                    }
                }
            }

            .post_area:hover {
                animation: hoverUp 0.3s ease-out 0.1s 1 normal forwards running;
            }

            .content_top_category_title {
                display: block;
                height: 80px;
                font-size: 45px;
                font-family: 'Caveat', cursive;
                position: relative;
                top: 36px;
                z-index: 9999;
            }

            .content_top_category_title_on_img {
                height: 80px;
                font-size: 47px;
                font-family: 'Caveat', cursive;
                position: absolute;
                color: rgba(240, 240, 240, 1);
                top: -33px;
                left: 17px;
                z-index: 9998;
            }

            .content_top_top_post {
                margin-top: 0px;
                position: relative;
            }

            .content_top_pickup_post {
                padding-top: 6px;
            }
        }
    }
</style>
