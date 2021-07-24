<template>
    <div id="contact_wrap">
        <FixedHeader/>
        <div class="contact">
            <v-container fluid>
                <v-row>
                    <v-col cols="12">
                        <BreadCrumbs
                            :breadItem=breadItem
                        />
                        <div class="contact_top">
                            <v-card
                                flat
                                class="contact_top_msg"
                            >
                                <v-card-title
                                    class="contact_top_title"
                                >Contact</v-card-title>
                                <!-- <v-card-subtitle
                                    class="contact_top_subtitle"
                                >
                                    お問い合わせ、お仕事のご依頼など、こちらからよろしくお願いします。
                                </v-card-subtitle> -->
                            </v-card>
                        </div>
                        <div class="contact_form_wrap">
                            <div class="contact_form">
                                <v-form
                                    v-model="valid"
                                >
                                    <v-text-field
                                        v-model="name"
                                        :counter="20"
                                        label="お名前"
                                        required
                                    ></v-text-field>
                                    <v-text-field
                                        v-model="email"
                                        :counter="40"
                                        label="メールアドレス"
                                        required
                                    ></v-text-field>
                                    <v-textarea
                                        counter
                                        v-model="content"
                                        label="お問い合わせ内容"
                                    ></v-textarea>
                                    <!-- <v-text-field
                                        v-model="content"
                                        :counter="200"
                                        label="content"
                                        required
                                    ></v-text-field> -->
                                    <!-- <vs-button>
                                        Send
                                        <template #animate>
                                            <i class='bx bx-mail-send'></i>
                                        </template>
                                    </vs-button> -->
                                    <v-btn
                                        class="mt-7"
                                        @click="submit"
                                    >
                                        submit
                                    </v-btn>
                                <!-- <vs-input v-model="name" placeholder="お名前">
                                    <template #icon>
                                        <i class='bx bx-user'></i>
                                    </template>
                                </vs-input>
                                <vs-input v-model="email" placeholder="メールアドレス">
                                    <template #icon>
                                        @
                                    </template>
                                </vs-input>
                                <vs-input v-model="content" placeholder="お問い合わせ内容">
                                    <template #icon>
                                        <i class='bx bx-message-rounded'></i>
                                    </template>
                                </vs-input> -->
                                </v-form>
                            </div>
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
        name: 'Contact',
        components: {
            BreadCrumbs,
            FontSidebar,
            FixedHeader,
            Footer,
            Sidebar
        },
        data: () => ({
            valid: false,
            name: '',
            email: '',
            content: '',
        }),
        created () {
        },
        computed: {
            pageObj () {
                return {
                    title: 'Contact',
                    bread: 'Contact',
                }
            },
            breadItem () {
                return [{
                    name: 'Contact',
                    slug: '',
                    disabled: true,
                }]
            }
        },
        methods: {
            submit () {
            }
        },
    }
</script>
<style lang="scss" scoped>
    .contact {
        width: 1200px;
        margin: 0 auto 80px auto;

        font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;
        .contact_top {
            margin-top: 38px;
            .contact_top_msg {
                width: 850px;
                margin: 0 auto;
                .contact_top_title {
                    font-size: 28px;
                    display: block;
                    text-align: center;
                }
                .contact_top_subtitle {
                    display: block;
                    text-align: center;
                    padding-top: 70px;
                }
            }
        }

        .contact_form_wrap {
            width: 850px;
            margin: 0 auto;
            padding: 50px 30px 30px 30px;
            // border: 1px solid rgba(100, 100, 100, 0.4);
        }
    }
</style>
