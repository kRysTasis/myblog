<template>
    <!-- 検索結果も将来的にデザイン変える思うためコンポーネントは敢えて分ける -->
    <div id="search_result_wrap">
        <FixedHeader/>
        <div id="search_result">
            <v-container
                fluid
            >
                <v-row>
                    <v-col cols="12">
                        <v-card
                            flat
                        >
                        <div class="search_result_top">
                            <v-card-title
                                class="py-1 mt-1 search_result_title"
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
    import { mapGetters, mapMutations } from 'vuex'
    import BreadCrumbs from '@/components/parts/BreadCrumbs'
    import ContentMain from '@/components/parts/ContentMain'
    import FontSidebar from '@/components/common/FontSidebar'
    import FixedHeader from '@/components/common/FixedHeader'
    import Footer from '@/components/common/Footer'
    import { Const } from '@/assets/js/const'
    const Con = new Const()

    export default {
        name: 'SearchResult',
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
            },
        }),
        beforeCreate () {
        },
        created () {
            this.searchPost()
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
            next()
            this.searchPost()
        },
        computed: {
            ...mapGetters([
                'searchResult',
                'loadingMainPosts'
            ]),
            title () {
                return this.$route.query.text
            },
        },
        methods: {
            ...mapMutations([
                'setLoadingMainPosts',
            ]),
            searchPost () {
                this.setLoadingMainPosts(true)
                this.$axios({
                    url: '/api/search/',
                    method: 'GET',
                    params: {
                        text: this.title
                    }
                })
                .then(res => {
                    console.log(res.data)
                    this.postsData = res.data
                    this.setLoadingMainPosts(false)
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
    #search_result_wrap {
        #search_result {
            width: 1200px;
            margin: 0 auto 60px auto;

            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;

            .search_result_top {
                margin-top: 38px;
                margin-bottom: 0;
                text-align: center;

                .search_result_title {
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
