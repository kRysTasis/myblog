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
                    >
                        <v-row>
                            <v-col cols="7" class="px-0 mx-0">
                                <v-img
                                    :aspect-ratio="16/9"
                                    :lazy-src="topPost.lazySrc"
                                    :src="topPost.src"
                                ></v-img>
                            </v-col>
                            <v-col cols="5" class="px-0 mx-0">
                                <v-card-subtitle class="content_top_title">
                                    {{ topPost.title || truncate(20) }}
                                </v-card-subtitle>
                                <v-card-text class="content_top_text">
                                    {{ topPost.content || truncate(110) }}
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
                    >
                        <v-row>
                            <v-col cols="12" class="pb-0 mb-0">
                                <v-img
                                    :aspect-ratio="16/9"
                                    :lazy-src="pickupPost.lazySrc"
                                    :src="pickupPost.src"
                                ></v-img>
                            </v-col>
                            <v-col cols="12" class="pt-0 mt-0">
                                <v-card-subtitle class="pl-0 ml-0 content_main_title">
                                    {{ pickupPost.title || truncate(20) }}
                                </v-card-subtitle>
                                <v-card-text class="pa-0 ma-0 content_top_text">
                                    {{ pickupPost.content || truncate(110) }}
                                </v-card-text>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'ContentTop',
        components: {
        },
        props: {
            topPosts: {
                type: Array,
                required: true,
            },
            pickupPosts: {
                type: Array,
                required: true,
            }
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
        },
        methods: {
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #content_top_wrap {
        background-color: rgba(100, 100, 100, 0.1);
        #content_top {
            width: 1000px;
            margin: 10px auto 0 auto;
            padding-top: 30px;
            padding-bottom: 40px;
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
