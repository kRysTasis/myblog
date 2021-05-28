<template>
    <div id="header_wrap">
        <v-card
            flat
            tile
        >
            <div id="header_top">
                <v-row>
                    <v-spacer/>
                    <v-col cols="6" class="header_top_title">
                        <v-card-title>krystasis</v-card-title>
                    </v-col>
                    <v-col cols="3" class="header_top_right">
                        <vs-input
                            v-model="searchText"
                            placeholder="search..."
                        >
                            <template #icon>
                                <i class='bx bx-search'></i>
                            </template>
                        </vs-input>
                    </v-col>
                </v-row>
            </div>
            <div id="header_middle">
                <v-row>
                    <v-spacer/>
                    <v-col
                        cols="2"
                        class="sns_icon_area_wrap"
                    >
                        <i class='bx bxl-github fa-lg github_icon mr-1'></i>
                        <i class="fab fa-twitter fa-lg twitter_icon"></i>
                    </v-col>
                </v-row>
            </div>
        </v-card>
        <div id="header_bottom">
            programming music category about work contact
        </div>
    </div>
</template>
<script>
    export default {
        name: 'Header',
        components: {
        },
        props: {
        },
        data: () => ({
            searchText: '',
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
    #header_wrap {
        width: 100%;
        height: 250px;
        #header_top {
            width: 100%;
            height: 180px;
            .v-card__title::v-deep {
                display: block;
                text-align: center;
                font-size: 40px;
            }
            padding-top: 20px;
            .header_top_title {
                font-family: 'Kaushan Script', cursive;
                padding-top: 45px;
            }
        }
        #header_middle {
            width: 100%;
            height: 40px;
            .twitter_icon {
                color: rgba(0,172,238,0.5);
            }
        }
        #header_bottom {
            font-family: 'Alegreya Sans SC', sans-serif;
            width: 1000px;
            height: 30px;
            margin: 0 auto;
            text-align: center;
        }
        .vs-input-content {
            margin: 0 auto;
        }
    }
</style>
