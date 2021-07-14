<template>
    <div id="work_wrap">
        <FixedHeader/>
        <div class="work">
            <v-container fluid>
                <v-row>
                    <v-col cols="12">
                        work
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <Footer/>
        <FontSidebar/>
    </div>
</template>

<script>
    import FontSidebar from '@/components/common/FontSidebar'
    import FixedHeader from '@/components/common/FixedHeader'
    import Footer from '@/components/common/Footer'
    import Sidebar from '@/components/common/Sidebar'

    export default {
        name: 'Work',
        components: {
            FontSidebar,
            FixedHeader,
            Footer,
            Sidebar
        },
        data: () => ({
        }),
        created () {
        },
        computed: {
            pageObj () {
                return {
                    title: 'Work',
                    bread: 'Work',
                }
            }
        },
        methods: {
        },
    }
</script>
<style lang="scss" scoped>
    .work {
        width: 1200px;
        margin: 0 auto;
    }
</style>
