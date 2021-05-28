<template>
    <div id="content_wrap">
        <v-card
            flat
            tile
            class="content_top"
        >
            <ContentTop
                :topPosts=topPosts
                :pickupPosts=pickupPosts
            />
        </v-card>
        <v-card
            flat
            tile
            class="content_middle"
        >
            <ContentMain
                :posts=posts
            />
        </v-card>
    </div>
</template>
<script>
    import ContentTop from '@/components/parts/ContentTop'
    import ContentMain from '@/components/parts/ContentMain'

    export default {
        name: 'Content',
        components: {
            ContentTop,
            ContentMain,
        },
        props: {
        },
        data: () => ({
            topPosts: [
                {
                    title: 'post1',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/11/500/300',
                },
                {
                    title: 'post2',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/10/300/300',
                },
            ],
            pickupPosts: [
                {
                    title: 'post3',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/14/500/300',
                },
                {
                    title: 'post4',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/12/300/300',
                },
                {
                    title: 'post5',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/17/300/200',
                },
            ],
            posts: [
                {
                    title: 'post1',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/11/500/300',
                },
                {
                    title: 'post2',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/10/300/300',
                },
                {
                    title: 'post3',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/14/500/300',
                },
                {
                    title: 'post4',
                    content: 'contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontentconte...',
                    lazySrc: 'https://picsum.photos/id/11/10/6',
                    src: 'https://picsum.photos/id/12/300/300',
                },
            ]
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
    #content_wrap {
        width: 100%;
        margin: 0 auto;
    }
</style>
