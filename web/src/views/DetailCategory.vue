<template>
    <div id="detail_category_wrap">
        <FixedHeader/>
        <div id="detail_category">
            <v-card
                flat
            >
            <BreadCrumbs
                :breadItem=breadItem
            />
            <div class="detail_category_top">
                <v-card-title
                class="detail_category_title"
                >{{ title }}</v-card-title>
            </div>
            <ContentMain
                :posts=posts
                :postCnt=postCnt
            />
            </v-card>
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
    import { mapMutations } from 'vuex'

    export default {
        name: '',
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
            posts: [],
            postCnt: 0,
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
            // カテゴリ間の移動はコンポーネントが再利用されるため、
            // next()でURL切り替えてからそのクエリーの値で記事を絞る
            next()
            this.getPosts()
        },
        computed: {
            title () {
                return this.$route.query.name
            },
            breadItem () {
                return [{
                    name: this.$route.query.name,
                    slug: '',
                    disabled: true,
                }]
            },
        },
        methods: {
            ...mapMutations([
                'setLoadingMainPosts',
            ]),
            getPosts () {
                this.setLoadingMainPosts(true)
                this.$axios({
                    url: '/api/posts/',
                    method: 'GET',
                    params: {
                        category: this.title
                    }
                })
                .then(res => {
                    this.setLoadingMainPosts(false)
                    console.log(res.data)
                    this.posts = res.data.results
                    this.postCnt = res.data.count
                })
                .catch(e => {
                    console.log('error')
                    console.log(e)
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #detail_category_wrap {

        #detail_category {
            width: 1200px;
            margin: 0 auto;

            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;

            .detail_category_top {
                margin-top: 38px;
                margin-bottom: 60px;

                .detail_category_title {
                    font-size: 26px;
                    margin: 0 auto;
                }
            }
        }
    }
</style>
