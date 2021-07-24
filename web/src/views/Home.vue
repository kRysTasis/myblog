<template>
    <div id="home">
        <Header/>
        <ContentTop
            :topPosts=topPosts
            :pickupPosts=pickupPosts
        />
        <ContentMain
            :postsData=postsData
            @update='postsData = $event'
        />
        <FontSidebar/>
        <Footer/>
    </div>
</template>

<script>
    import Header from '@/components/common/Header'
    import Footer from '@/components/common/Footer'
    import FontSidebar from '@/components/common/FontSidebar'
    import ContentTop from '@/components/parts/ContentTop'
    import ContentMain from '@/components/parts/ContentMain'
    import { mapMutations } from 'vuex'

    export default {
        name: 'Home',
        components: {
            Header,
            Footer,
            FontSidebar,
            ContentTop,
            ContentMain
        },
        data: () => ({
            postsData: {
                results: [{}, {}, {}, {}, {}, {}],
                count: 0,
                next: '',
                previous: '',
            },
            topPosts: [{}, {}],
            pickupPosts: [{}, {}, {}],
        }),
        created () {
            this.getPosts()
            this.getTopPosts()
        },
        computed: {
        },
        methods: {
            ...mapMutations([
                'setLoadingTopPosts',
                'setLoadingMainPosts'
            ]),
            getPosts () {
                this.setLoadingMainPosts(true)
                this.$axios({
                    url: '/api/posts/',
                    method: 'GET',
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
            getTopPosts () {
                this.setLoadingTopPosts(true)
                this.$axios({
                    url: '/api/posts/top/',
                    method: 'GET',
                })
                .then(res => {
                    this.setLoadingTopPosts(false)
                    console.log(res.data)
                    this.topPosts = res.data.topPosts
                    this.pickupPosts = res.data.pickupPosts
                })
                .catch(e => {
                    console.log(e)
                })
            },
        },
    }
</script>
<style lang="scss" scoped>
</style>
