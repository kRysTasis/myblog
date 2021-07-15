<template>
    <div id="work_wrap">
        <FixedHeader
        />
        <div class="work">
            <v-container fluid class="ma-0 pa-0">
                <v-row>
                    <v-col cols="12">
                        <!-- <BreadCrumbs
                            :breadItem=breadItem
                        /> -->
                        <div class="work_top">
                            <v-card
                                flat
                            >
                                <v-card-title
                                    class="work_top_title"
                                >Work</v-card-title>
                            </v-card>
                        </div>
                        <div class="work_content_wrap">
                            <v-container class="work_content">
                                    <v-row>
                                        <v-col
                                            v-for="(item, i) in items"
                                            :key="i"
                                            cols="3"
                                            class="mb-1 work_content_item"
                                        >
                                            <v-img
                                                :src="item.url"
                                                width="100%"
                                                class="my_image"
                                            ></v-img>
                                        </v-col>
                                    </v-row>
                            </v-container>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <Footer/>
        <FontSidebar/>
    </div>
</template>

<script>
    import BreadCrumbs from '@/components/parts/BreadCrumbs'
    import FontSidebar from '@/components/common/FontSidebar'
    import FixedHeader from '@/components/common/FixedHeader'
    import Footer from '@/components/common/Footer'
    import Sidebar from '@/components/common/Sidebar'

    export default {
        name: 'Work',
        components: {
            BreadCrumbs,
            FontSidebar,
            FixedHeader,
            Footer,
            Sidebar
        },
        data: () => ({
            items: [
                {
                    title: 1,
                    url: require('@/assets/img/coopy3.png'),
                    web: true
                },
                {
                    title: 2,
                    url: require('@/assets/img/bandue3.png'),
                    web: true
                },
                {
                    title: 3,
                    url: require('@/assets/img/bandue1.png'),
                    web: true
                },
            ]
        }),
        created () {
        },
        mounted () {
        },
        computed: {
            pageObj () {
                return {
                    title: 'Work',
                    bread: 'Work',
                }
            },
            breadItem () {
                return [{
                    name: 'Work',
                    slug: '',
                    disabled: true,
                }]
            }
        },
        methods: {
        },
    }
</script>
<style lang="scss" scoped>
    #work_wrap::v-deep {
        width: 100%;
        .work {
            margin-bottom: 100px;

            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;
            .work_top {
                margin-top: 68px;
                margin-bottom: 50px;
                .work_top_title {
                    font-size: 28px;
                    display: block;
                    text-align: center;
                }
            }
            .work_content_wrap {
                .work_content {
                    .work_content_item {
                        cursor: pointer;
                        height: auto;
                        width: 100%;
                        margin: 4%;
                        box-shadow: 1px 2px 2px rgba(100, 100, 100, 0.2);
                        border-collapse: collapse;
                    }
                }
            }
        }
    }
</style>
