<template>
    <div id="contact_wrap">
        <FixedHeader/>
        <div class="contact">
            <v-container fluid>
                <v-row>
                    <v-col cols="12">
                        contact
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
        name: 'Contact',
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
                    title: 'Contact',
                    bread: 'Contact',
                }
            }
        },
        methods: {
        },
    }
</script>
<style lang="scss" scoped>
    .contact {
        width: 1200px;
        margin: 0 auto;
    }
</style>
