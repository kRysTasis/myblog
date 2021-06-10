<template>
    <div id="content_wrap">
        <v-card
            flat
            tile
            class="content_top"
        >
            <ContentTop/>
        </v-card>
        <v-card
            flat
            tile
            class="content_middle"
        >
            <ContentMain/>
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
