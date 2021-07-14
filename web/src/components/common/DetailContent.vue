<template>
    <div id="detail_content">
        <v-card
            flat
        >
            <BreadCrumbs
                :breadItem=breadItem
            />
            <div class="detail_post_top">

                <v-card-title
                    class="detail_post_title"
                >
                    {{ post.title }}
                </v-card-title>

                <v-card-text
                    class="detail_post_created_at pb-0"
                >
                    {{ post.created_at }}
                </v-card-text>

                <v-card-text
                    class="detail_post_tags"
                >
                    <v-card-actions>
                        <v-chip
                            v-for="(tag, i) in post.tags"
                            :key="i"
                            class="ma-2 post_tag_btn"
                            label
                            text-color="white"
                            color="grey"
                            @click="toPage(tag)"
                        >
                            <i class='bx bxs-tag post_tag_image'></i>
                                {{ tag.name }}
                        </v-chip>
                    </v-card-actions>
                </v-card-text>

                <v-card-text>
                    <v-img
                        :aspect-ratio="16/9"
                        :lazy-src=lazySrc
                        :src="post.thumbnail"
                        class="detail_post_image"
                        height="350"
                        width="750"
                    ></v-img>
                </v-card-text>
            </div>

            <div class="detail_post_middle">
                <v-card-text
                    class="detail_post_content"
                    v-html="post.content"
                ></v-card-text>
            </div>
        </v-card>
    </div>
</template>
<script>
    import BreadCrumbs from '@/components/parts/BreadCrumbs'
    import { Const } from '@/assets/js/const'
    import hljs from 'highlight.js'
    const Con = new Const()

    export default {
        name: 'DetailContent',
        components: {
            BreadCrumbs
        },
        props: {
            post: {
                type: Object,
                required: true,
                default: () => ({})
            }
        },
        data: () => ({
            lazySrc: Con.LAZYSRC,
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            hljs.configure({
                languages: ['python', 'javascript', 'yml', 'sh', 'text']
            })
            hljs.initHighlightingOnLoad()
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
            breadItem () {
                return [
                    {
                        name: this.post.category.name,
                        slug: this.post.category.slug,
                        disabled: false,
                    },
                    {
                        name: this.post.title,
                        slug: '',
                        disabled: true,
                    }
                ]
            }
        },
        methods: {
            toPage (tag) {
                this.$router.push({
                    path: '/search',
                    query: {
                        tag: tag.name
                    }
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss">
    #detail_content {

        font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;
        // width: 850px;
        // width: 1200px;
        height: auto;
        // margin: 0 auto;

        .detail_post_top {
            margin-top: 38px;
            margin-bottom: 60px;

            .detail_post_title {
                font-size: 26px;
                margin-bottom: 0px;
            }

            .detail_post_image {
                margin-bottom: 40px;
            }

            .detail_post_created_at {
                font-size: 10px;
            }

            .detail_post_tags {
                margin: 0;
                padding-top: 10px;
                padding-left: 5px;
                .post_tag_btn {
                    cursor: pointer;
                    font-size: 10px;
                    .post_tag_image {
                        padding-right: 0.7px;
                    }
                }
            }
        }

        .detail_post_middle {
            .detail_post_content {
                .toc {
                    font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;

                    color: rgba(60, 60, 60, 1);
                    .toctitle {
                        font-size: 20px;
                        display: inline-block;
                        left: 290px;
                        text-align: center;
                        width: 100px;
                        position: relative;
                        top: -20px;
                        z-index: 9999;
                        background-color: white;
                        font-family: "Lato", "Noto Sans JP";
                    }
                    width: 700px;
                    border: solid 1px rgba(30, 30, 30, 0.3);

                    font-weight: 100;

                    a {
                        color: black;
                        text-decoration: none;
                    }
                    padding: 10px 0 10px 0;
                    // background-color: rgba(150, 150, 150, 0.3);
                    ul, li {
                        // list-style: none;
                        margin: 0;
                        padding: 0;
                        margin-left: 13px;
                    }
                    li {
                        font-size: 13px;
                        margin-top: 6px !important;
                        margin-left: 20px !important;
                        margin-bottom: 20px;
                    }
                    li > ul li {
                        border: none;
                        margin-bottom: 0px;
                        font-size: 12px;
                        li > ul li {
                            font-size: 10px;
                        }
                    }
                    li:last-child {
                        margin-bottom: 20px !important;
                    }
                }
                .codehilite {
                    padding: 10px 0 10px 16px;
                    background-color: rgba(60, 60, 60, 1);
                    font-size: 16px;
                    color: rgba(250, 250, 250, 0.9);
                    max-width: 800px;
                }
                font-size: 10px;
                h1, h2, h3, h4, h5, h6 {
                }
                h1 {
                    font-family: "Lato", "Noto Sans JP";
                    font-size: 25px;
                    margin-bottom: 40px;
                    margin-top: 60px;
                    display: block;
                    padding-bottom: 4px;
                    border-bottom: 1px solid rgba(50, 50, 50, 0.5);
                }
                h1::before {
                    content: '';
                    background-color: rgba(30,10,250,0.3);
                    width: 3px;
                    height: 26px;
                    position: relative;
                    top: 6px;
                    display: inline-block;
                    margin-right: 5px;
                }
                h2 {
                    font-size: 18px;
                    margin-bottom: 40px;
                    margin-top: 60px;
                    margin-left: 10px;
                }
                h2::before {
                    content: '-';
                    margin-right: 5px;
                }
                h3 {
                    font-size: 17px;
                    margin-bottom: 30px;
                    margin-top: 40px;
                    margin-left: 18px;
                }
                h4 {
                    font-size: 16px;
                    margin-bottom: 30px;
                    margin-top: 30px;
                    margin-left: 20px;
                }
                h5 {
                    font-size: 15px;
                    margin-bottom: 30px;
                    margin-top: 30px;
                    margin-left: 22px;
                }
                h6 {
                    font-size: 14px;
                    margin-bottom: 30px;
                    margin-top: 30px;
                    margin-left: 24px;
                }
                p {
                    font-size: 14px;
                    margin-bottom: 10px;
                    margin-top: 14px;
                    margin-left: 26px;
                }
                ul, ol {
                    margin-bottom: 10px;
                    margin-top: 30px;
                    margin-left: 28px;
                }
                .codehilite {
                    margin-bottom: 10px;
                    margin-top: 17px;
                    margin-left: 34px;
                }
                table {
                    // background-color: rgba(150, 150, 155, 0.1);
                    border-spacing: 0;
                    border-collapse: collapse;
                    // border: 1px solid rgba(10, 10, 10, 0.5);
                    margin-bottom: 10px;
                    margin-top: 20px;
                    margin-left: 10px;
                    th {
                        font-size: 12px;
                        padding: 0 5px;
                        color: white;
                        background-color: rgba(50, 50, 55, 0.4);
                        border: 1px solid rgba(60, 60, 60, 0.5);
                        min-width: 50px !important;
                    }
                    tr {
                        td {
                            font-size: 13px;
                            border: 1px solid rgba(60, 60, 60, 0.5);
                            padding: 8px 7px;
                            margin: 0;
                        }
                        td:first_child {
                            background-color: rgba(20, 20, 255, 0.1);
                        }
                    }
                    tr:nth-child(2n) {
                        background-color: rgba(200, 200, 200, 0.5);
                    }
                }
            }
        }
    }
</style>
