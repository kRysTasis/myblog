<template>
    <v-card
        flat
        tile
        class="content_middle"
    >
        <div id="content_main_wrap">
            <div id="content_main">
                <v-container
                    fluid
                    class="content_main_post"
                    ref="contentMainPost"
                >
                    <v-card-title
                        v-if="!loadingMainPosts && postsData.count != 0"
                        class="content_main_category_title"
                    >posts</v-card-title>
                    <v-row class="content_main_post_row">
                        <v-col
                            v-for="(post, i) in postsData.results"
                            :key="i"
                            cols="12"
                            class="post_area"
                            @click="showPostDetail(post)"
                        >
                            <div v-if="loadingMainPosts">
                                <v-row>
                                    <v-col cols="12" class="px-3 mx-0">
                                        <v-skeleton-loader
                                            v-bind="attrs"
                                            type="card"
                                        ></v-skeleton-loader>
                                    </v-col>
                                </v-row>
                            </div>
                            <div v-else>
                                <v-row class="content_main_post_area">
                                    <v-col cols="7">
                                        <v-img
                                            :aspect-ratio="16/9"
                                            :lazy-src=lazySrc
                                            :src="post.thumbnail"
                                            class="content_main_image"
                                            height="350"
                                            width="700"
                                        ></v-img>
                                    </v-col>
                                    <v-col cols="5" class="px-0 mx-0 content_main_text_area">
                                        <v-card-title
                                            class="content_main_title pb-0 mb-6"
                                            :inner-html.prop="post.title | truncate(30)">
                                        >
                                        </v-card-title>
                                        <!-- <v-card-text
                                            class="content_main_category"
                                        >
                                            {{ post.category.name }}
                                        </v-card-text> -->
                                        <v-spacer/>
                                        <v-card-text
                                            class="content_main_created_at"
                                        >
                                            {{ post.created_at }}
                                        </v-card-text>
                                        <!-- <v-card-text
                                            class="content_main_text"
                                            :inner-html.prop="post.content | truncate(200)">
                                        </v-card-text> -->
                                    </v-col>
                                    <div
                                        v-if="i == 0"
                                        class="content_main_category_title_on_img"
                                    >posts</div>
                                </v-row>
                            </div>
                        </v-col>
                        <div v-if="!loadingMainPosts && postsData.count != 0" class="pagination">
                            <vs-pagination
                                v-model="page"
                                :length=pageNum
                                @input="getPageNumber"
                            ></vs-pagination>
                        </div>
                    </v-row>
                </v-container>
            </div>
        </div>
    </v-card>
</template>
<script>
    import { Const } from '@/assets/js/const'
    import { mapGetters, mapMutations } from 'vuex'
    import pageMixin from '@/mixins/page'
    import _ from 'lodash'
    const Con = new Const()

    export default {
        name: 'ContentMain',
        components: {
        },
        props: {
            postsData: {
                type: Object,
                required: true,
                default: () => ({
                    results: [{}, {}, {}, {}, {}, {}],
                    count: 0,
                    next: '',
                    previous: '',
                })
            }
        },
        data: () => ({
            attrs: {
                class: 'mb-100',
                boilerplace: false,
                elevation: 2,
            },
            lazySrc: Con.LAZYSRC,
            page: 1,
            next: '',
            previous: '',
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
            pageNum: function () {
                return Math.ceil(this.postsData.count / 6)
            },
            ...mapGetters([
                'loadingMainPosts'
            ]),
        },
        methods: {
            ...mapMutations([
                'setLoadingMainPosts'
            ]),
            showPostDetail (post) {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                })
                setTimeout(this.toDetailPost, 300, post)
            },
            getPageNumber (pageNumber) {
                console.log('pageNumber', pageNumber)
                console.log(this.$route)
                console.log(this.$route.name)
                console.log(this.$route.query)
                // メイン記事の一番上に戻る
                const targetRect = this.$refs.contentMainPost.getBoundingClientRect()
                const target = targetRect.top + window.pageYOffset
                window.scrollTo({
                    top: target,
                    behavior: 'smooth'
                })
                setTimeout(this.getPageDetail, 100, pageNumber)
            },
            getPageDetail (pageNumber) {
                this.setLoadingMainPosts(true)
                const name = this.$route.name
                let url = ''
                const page = '?page=' + pageNumber
                if (name === 'Home') {
                    url = '/api/posts/' + page
                } else if (name === 'DetailCategory' || name === 'TagSearchResult') {
                    // TODO カテゴリはcategory=に、タグはtag=にする。
                    const pre = (name === 'DetailCategory') ? 'category=' : 'tags='
                    url = '/api/posts/' + page + '&' + pre + this.$route.query.name
                } else if (name === 'SearchResult') {
                    url = '/api/search/' + page + '&' + this.joinObj(this.$route.query)
                }
                console.log(this.$route.name)
                console.log(this.$route.query)
                console.log(url)

                this.$axios({
                    url: url,
                    method: 'GET',
                    // params: {
                    //     page: pageNumber
                    // }
                })
                .then(res => {
                    console.log(res.data)
                    this.$emit('update', res.data)
                    this.setLoadingMainPosts(false)
                })
                .catch(e => {
                    console.log(e)
                })
            },
            joinObj (obj) {
                let res = ''
                for (const i in obj) {
                    res += i + '=' + obj[i]
                }
                return res
            }
        },
        mixins: [pageMixin],
    }
</script>
<style lang="scss" scoped>
    @keyframes hoverUp {
        0% {
            box-shadow: 1px 2px 2px rgba(50, 50, 50, 0.7);
            transform: translateY(0);
        }
        50% {
            box-shadow: 4px 3px 4px 1px rgba(80, 80, 80, 0.4);
            transform: translateY(-0.4px);
        }
        100% {
            box-shadow: 4px 3px 5px 2px rgba(100, 100, 100, 0.3);
            transform: translateY(-0.8px);
        }
    }

    #content_main_wrap::v-deep {

        #content_main {

            .content_main_post {
                width: 1200px;
                padding: 0;
                margin: 30px auto 60px auto;

                .post_area {
                    cursor: pointer;
                    position: relative;
                }

                .content_main_post_row {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 0;
                }

                .content_main_category_title {
                    display: block;
                    height: 80px;
                    // font-family: 'Quicksand', sans-serif;
                    // font-family: 'Noto Sans JP', sans-serif;
                    // font-family: 'Alegreya Sans SC', sans-serif;
                    font-family: 'Caveat', cursive;
                    font-size: 45px;
                    position: relative;
                    top: 46px;
                    left: 13px;
                    z-index: 9999;
                }

                .content_main_text_area {

                    .content_main_title {
                        // font-family: 'Quicksand', sans-serif;
                        // font-family: 'Noto Sans JP', sans-serif;
                        // font-family: 'Alegreya Sans SC', sans-serif;
                        // font-family: 'Caveat', cursive;
                        font-family: 'Homemade Apple', cursive;
                        font-size: 17px;
                        margin-top: 15px;
                    }

                    .content_main_category {
                        font-family: 'Noto Sans JP', sans-serif;
                        font-size: 13px;
                    }

                    .content_main_created_at {
                        font-family: 'Noto Sans JP', sans-serif;
                        font-size: 12px;
                        margin-top: -30px;
                    }

                    .content_main_text {
                        h1, h2, h3, h4, h5, h6 {
                            font-weight: normal;
                        }
                        padding-top: 30px;
                        // font-family: 'Quicksand', sans-serif;
                        font-family: 'Noto Sans JP', sans-serif;
                        h1 {
                            font-size: 15px;
                        }
                        h2 {
                            font-size: 14px;
                        }
                        h3 {
                            font-size: 13px;
                        }
                        h4 {
                            font-size: 12px;
                        }
                        h5 {
                            font-size: 11px;
                        }
                        h6 {
                            font-size: 10px;
                        }
                        p {
                            font-size: 9px;
                        }
                    }
                }

                .content_main_post_area {
                    margin-bottom: 20px;
                    box-shadow: 1px 1px 1px 1px rgba(200, 200, 200, 0.3);

                    .content_main_category_title_on_img {
                        z-index: 9998;
                        color: rgba(240, 240, 240, 1);
                        position: absolute;
                        top: -33px;
                        left: 20px;
                        font-family: 'Caveat', cursive;
                        height: 80px;
                        font-size: 45px;
                    }
                }

                .content_main_post_area:hover {
                    animation: hoverUp 0.3s ease-out 0.1s 1 normal forwards running;
                }

                .pagination {
                    margin: 45px auto 0px auto;
                }
            }
        }
    }
</style>
