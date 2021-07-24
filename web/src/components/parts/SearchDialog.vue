<template>
    <div id="search_dialog_wrap">
        <vs-dialog v-model="localSearchDialog" width="400px">
            <v-container
                fluid
                id="search_dialog"
            >
                <v-card
                    flat
                >
                    <v-card-subtitle
                        class="search_dialog_title"
                    >
                        記事を検索
                    </v-card-subtitle>
                    <SearchArea
                        @close='closeDialog'
                    />
                </v-card>
            </v-container>
        </vs-dialog>
    </div>
</template>
<script>
    import SearchArea from '@/components/parts/SearchArea'

    export default {
        name: 'SearchDialog',
        components: {
            SearchArea
        },
        props: {
            searchDialog: {
                type: Boolean,
                required: true,
            }
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
            localSearchDialog: {
                get: function () {
                    return this.searchDialog
                },
                set: function (value) {
                    this.$emit('update', value)
                }
            }
        },
        methods: {
            closeDialog () {
                this.$emit('update', false)
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .search_dialog_title {
        text-align: center;
        font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro", "Yu Gothic Medium", "游ゴシック Medium", YuGothic, "游ゴシック体", "メイリオ", sans-serif;
    }
</style>
