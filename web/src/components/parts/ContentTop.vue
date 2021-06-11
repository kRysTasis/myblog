<template>
    <div id="content_top_wrap">
        <div id="content_top">
            <div class="content_top_top_post">
                <v-card-title
                    class="content_top_category_title"
                >
                    Top
                </v-card-title>
                <v-row>
                    <v-col
                        v-for="(topPost, i) in topPosts"
                        :key="i"
                        cols="6"
                        class="post_area"
                        @click="showPostDetail(topPost)"
                    >
                        <div v-if="loading">
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
                                <v-col cols="12" class="px-3 mx-0">
                                    <v-img
                                    :aspect-ratio="16/9"
                                    :lazy-src=lazySrc
                                    :src="topPost.thumbnail"
                                    ></v-img>
                                </v-col>
                            </v-row>
                        </div>
                        <v-row>
                            <v-col cols="12" class="px-0 mx-0">
                                <v-card-subtitle class="content_top_title">
                                    <!-- {{ topPost.title || truncate(20) }} -->
                                    {{ topPost.title }}
                                </v-card-subtitle>
                                <v-card-text class="content_top_text">
                                    <!-- {{ topPost.content || truncate(110) }} -->
                                    {{ topPost.content }}
                                </v-card-text>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </div>

            <div class="content_top_pickup_post">
                <v-card-title
                    class="content_top_category_title"
                >
                    Pickup
                </v-card-title>
                <v-row>
                    <v-col
                        v-for="(pickupPost, i) in pickupPosts"
                        :key="i"
                        cols="4"
                        class="post_area"
                        @click="showPostDetail(pickupPost)"
                    >
                        <div v-if="loading">
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
                                <v-col cols="12" class="pb-0 mb-0">
                                    <v-img
                                    :aspect-ratio="16/9"
                                    :lazy-src=lazySrc
                                    :src="pickupPost.thumbnail"
                                    ></v-img>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12" class="pt-0 mt-0">
                                    <v-card-subtitle class="pl-0 ml-0 content_main_title">
                                        <!-- {{ pickupPost.title || truncate(20) }} -->
                                        {{ pickupPost.title }}
                                    </v-card-subtitle>
                                    <v-card-text class="pa-0 ma-0 content_top_text">
                                        <!-- {{ pickupPost.content || truncate(20) }} -->
                                        {{ pickupPost.content }}
                                    </v-card-text>
                                </v-col>
                            </v-row>
                        </div>
                    </v-col>
                </v-row>
            </div>
        </div>
    </div>
</template>
<script>
    import { Const } from '@/assets/js/const'
    const Con = new Const()

    export default {
        name: 'ContentTop',
        components: {
        },
        props: {
        },
        data: () => ({
            attrs: {
                class: 'mb-6',
                boilerplace: false,
                elevation: 2,
            },
            loading: true,
            lazySrc: Con.LAZYSRC,
            topPosts: [{}, {}],
            pickupPosts: [{}, {}, {}],
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            this.getTopPosts()
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
            getTopPosts () {
                this.$axios({
                    url: '/api/posts/top/',
                    method: 'GET',
                })
                .then(res => {
                    this.loading = false
                    console.log(res.data)
                    this.topPosts = res.data.topPosts
                    this.pickupPosts = res.data.pickupPosts
                })
                .catch(e => {
                    console.log(e)
                })
            },
            showPostDetail (post) {
                console.log('post', post)
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #content_top_wrap {
        background-color: rgba(100, 100, 100, 0.1);
        #content_top {
            width: 1200px;
            margin: 10px auto 0 auto;
            padding-top: 30px;
            padding-bottom: 40px;
            .post_area {
                cursor: pointer;
            }
            .content_top_category_title {
                display: block;
                text-align: center;
                height: 80px;
                font-family: 'Vollkorn', serif;
                // font-family: 'Caveat', cursive;
                // font-family: 'Economica', sans-serif;
            }
            .content_top_title {
                // font-family: 'Caveat', cursive;
                font-family: 'Quicksand', sans-serif;
                // font-family: 'Economica', sans-serif;
            }
            .content_top_text {
                font-family: 'Quicksand', sans-serif;
            }
            .content_top_top_post {
                margin-top: 20px;
            }
            .content_top_pickup_post {
                margin-top: 65px;
            }
        }
    }
</style>
