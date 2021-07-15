<template>
    <div id="detail_post_wrap">
        <FixedHeader/>
        <div id="detail_content_wrap">
            <v-container fluid>
                <div v-if="loading">
                    <v-row>
                        <v-col cols="12" class="px-0 mx-0">
                            <v-skeleton-loader
                                v-bind="attrs"
                                type="card"
                            ></v-skeleton-loader>
                        </v-col>
                    </v-row>
                </div>
                <div v-else>
                    <v-row>
                        <v-col cols="12">
                            <DetailContent
                                :post=post
                            />
                        </v-col>
                        <!-- <v-col cols="3">
                            <Sidebar/>
                        </v-col> -->
                    </v-row>
                </div>
            </v-container>
        </div>
        <FontSidebar/>
        <Footer/>
    </div>
</template>
<script>
    import FixedHeader from '@/components/common/FixedHeader'
    import DetailContent from '@/components/common/DetailContent'
    import Footer from '@/components/common/Footer'
    import FontSidebar from '@/components/common/FontSidebar'
    import Sidebar from '@/components/common/Sidebar'

    export default {
        name: 'DetailPost',
        components: {
            FixedHeader,
            DetailContent,
            Footer,
            FontSidebar,
            Sidebar
        },
        props: {
        },
        data: () => ({
            post: {},
            loading: true,
            attrs: {
                class: 'mb-100',
                boilerplace: false,
                elevation: 2,
            }
        }),
        beforeCreate () {
        },
        created () {
            const id = this.$route.params.id
            this.$axios({
                url: `/api/posts/${id}/`,
                method: 'GET'
            })
            .then(res => {
                // console.log(res.data)
                this.post = res.data
                this.loading = false
            })
            .catch(e => {
                console.log(e)
            })
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
    #detail_post_wrap {
        #detail_content_wrap {
            width: 1200px;
            margin: 0 auto;
        }
    }
</style>
