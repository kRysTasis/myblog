<template>
    <div id="content_main_wrap">
        <div id="content_main">
            <v-card-title
                class="content_main_category_title"
            >
                記事一覧
            </v-card-title>
            <v-row>
                <v-col
                    v-for="(post, i) in posts"
                    :key="i"
                    cols="6"
                >
                    <v-row>
                        <v-col cols="12">
                            <v-img
                                :aspect-ratio="16/9"
                                :lazy-src="post.lazySrc"
                                :src="post.src"
                            ></v-img>
                        </v-col>
                        <v-col cols="12" class="px-0 mx-0">
                            <v-card-subtitle class="pt-0 mt-0 content_main_title">
                                {{ post.title || truncate(20) }}
                            </v-card-subtitle>
                            <v-card-text class="content_main_text">
                                {{ post.content || truncate(110) }}
                            </v-card-text>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'ContentMain',
        components: {
        },
        props: {
            posts: {
                type: Array,
                required: true,
            },
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
    #content_main_wrap {
        #content_main {
            width: 1000px;
            margin: 80px auto 0 auto;
            .content_main_category_title {
                display: block;
                // text-align: center;
                height: 80px;
                font-family: 'Vollkorn', serif;
            }
            .content_main_title {
                font-family: 'Quicksand', sans-serif;
            }
            .content_main_text {
                font-family: 'Quicksand', sans-serif;
            }
        }
    }
</style>
