<template>
    <div id="footer_wrap">
        <div
            id="footer_top"
        >
            <v-row>
                <v-col
                    cols="6"
                >
                    <v-card-subtitle class="footer_subtitle">
                        ABOUT
                    </v-card-subtitle>
                    <v-img
                        :aspect-ratio="16/9"
                        lazy-src="https://picsum.photos/id/11/10/6"
                        src="https://picsum.photos/id/11/500/300"
                    ></v-img>
                    <v-card-text class="footer_text">
                        texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext
                    </v-card-text>
                </v-col>
                <v-spacer/>
                <v-col
                    cols="4"
                >
                    <v-card-subtitle class="footer_subtitle">
                        TAG
                    </v-card-subtitle>
                    <v-card-text class="ml-4 footer_text">
                        tag, tag, tag, tag, tag, tag, tag, tag, tag, tag
                    </v-card-text>

                    <v-card-subtitle class="footer_subtitle">
                        LINK
                    </v-card-subtitle>
                    <v-card-text class="ml-4 footer_text">
                        Google
                    </v-card-text>
                    <v-card-text class="ml-4 footer_text">
                        Yahoo
                    </v-card-text>
                </v-col>
            </v-row>
        </div>
        <v-divider/>
        <div
            id="footer_bottom"
        >
            <v-row>
                <v-col cols="12">
                    <v-card-text>
                        ©krystasis.inc
                    </v-card-text>
                </v-col>
            </v-row>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'Footer',
        components: {
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
    #footer_wrap {
        padding-top: 80px;
        background-color: rgba(100, 100, 100, 0.1);
        width: 100%;
        height: 600px;
        .footer_subtitle {
            font-family: 'Vollkorn', serif;
            font-size: 25px;
        }
        .footer_text {
            font-family: 'Quicksand', sans-serif;
        }
        #footer_top {
            width: 1000px;
            margin: 0 auto 30px auto;
            .v-card__text {
                word-break: break-all;
            }
        }
        #footer_bottom {
            width: 100%;
            height: 80px;
            margin-top: 10px;
            text-align: center;
            font-family: 'Alegreya Sans SC', sans-serif;
        }
    }
</style>
