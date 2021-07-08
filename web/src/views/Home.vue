<template>
    <div id="home">
        <Header/>
        <Content/>
        <Sidebar/>
        <Footer/>
    </div>
</template>

<script>
    import Header from '@/components/common/Header'
    import Content from '@/components/common/Content'
    import Footer from '@/components/common/Footer'
    import Sidebar from '@/components/common/Sidebar'

    export default {
        name: 'Home',
        components: {
            Header,
            Content,
            Footer,
            Sidebar
        },
        data: () => ({
        }),
        created () {
        },
        computed: {
        },
        methods: {
        },
    }
</script>
<style lang="scss" scoped>
</style>
