<template>
    <div id="detail_post">
        detailPost
    </div>
</template>
<script>
    export default {
        name: 'DetailPost',
        components: {
        },
        props: {
        },
        data: () => ({
            postData: {}
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            const id = this.$route.params.id
            this.$axios({
                url: `/api/posts/${id}/`,
                method: 'GET'
            })
            .then(res => {
                console.log(res.data)
                this.postData = res.data
            })
            .catch(e => {
                console.log(e)
            })
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
</style>
