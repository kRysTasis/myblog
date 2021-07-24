<template>
    <!-- 将来的にカテゴリ詳細とデザイン変えると思うからコンポーネントは敢えて分ける -->
    <div id="tag_search_result_wrap">
        <FixedHeader/>
        <div id="tag_search_result">
            <v-container
                fluid
            >
                <v-row>
                    <v-col cols="12">
                        <v-card
                            flat
                        >
                        <BreadCrumbs
                            :breadItem=breadItem
                        />
                        <div class="tag_search_result_top">
                            <v-card-title
                                class="py-1 mt-1 tag_search_result_title"
                            >{{ title }}</v-card-title>
                            <v-card-text
                                v-if="!loadingMainPosts"
                                class="post_cnt"
                            >
                                {{ postsData.count }} posts
                            </v-card-text>
                        </div>
                        </v-card>
                    </v-col>
                </v-row>
                <ContentMain
                    :postsData=postsData
                    @update='postsData = $event'
                />
            </v-container>
        </div>
        <FontSidebar/>
        <Footer/>
    </div>
</template>
<script>
    import BreadCrumbs from '@/components/parts/BreadCrumbs'
    import ContentMain from '@/components/parts/ContentMain'
    import FontSidebar from '@/components/common/FontSidebar'
    import FixedHeader from '@/components/common/FixedHeader'
    import Footer from '@/components/common/Footer'
    import { mapGetters, mapMutations } from 'vuex'
    import { Const } from '@/assets/js/const'
    const Con = new Const()

    export default {
        name: 'TagSearchResult',
        components: {
            BreadCrumbs,
            ContentMain,
            FixedHeader,
            FontSidebar,
            Footer
        },
        props: {
        },
        data: () => ({
            postsData: {
                results: [{}, {}, {}, {}, {}, {}],
                count: 0,
                next: '',
                previous: '',
            }
        }),
        beforeCreate () {
        },
        created () {
            this.getPosts()
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
        beforeRouteUpdate (to, from, next) {
            // タグ検索を連続でするとコンポーネントが再利用されるため、
            // next()でURL切り替えてからそのクエリーの値で記事を絞る
            next()
            this.getPosts()
        },
        computed: {
            ...mapGetters([
                'loadingMainPosts'
            ]),
            title () {
                return this.$route.query.name
            },
            breadItem () {
                return [
                    {
                        name: 'タグ',
                        slug: '',
                        disabled: true,
                    },
                    {
                        name: this.title,
                        slug: '',
                        disabled: true,
                    }
                ]
            },
        },
        methods: {
            ...mapMutations([
                'setLoadingMainPosts',
            ]),
            getPosts () {
                this.setLoadingMainPosts(true)
                this.init()
                this.$axios({
                    url: '/api/posts/',
                    method: 'GET',
                    params: {
                        tags: this.title
                    }
                })
                .then(res => {
                    this.setLoadingMainPosts(false)
                    console.log(res.data)
                    this.postsData = res.data
                })
                .catch(e => {
                    console.log(e)
                })
            },
            init () {
                this.postsData = {
                    results: [{}, {}, {}, {}, {}, {}],
                    count: 0,
                    next: '',
                    previous: '',
                }
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #tag_search_result_wrap {
        #tag_search_result {
            width: 1200px;
            margin: 0 auto 60px auto;

            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;

            .tag_search_result_top {
                margin-top: 38px;
                margin-bottom: 0;
                text-align: center;

                .tag_search_result_title {
                    // font-family: 'Quicksand', sans-serif;
                    font-family: 'Alegreya Sans SC', sans-serif;
                    // font-family: 'Caveat', cursive;
                    font-size: 35px;
                    text-align: center;
                    display: inline-block;
                }

                .post_cnt {
                    padding-top: 20px;
                }
            }
        }
    }
</style>
