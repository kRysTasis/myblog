<template>
    <div id="search_area_wrap">
        <vs-input
            class="header_top_search"
            v-model="searchText"
            placeholder="search..."
            @keyup.enter="checkSearchText"
            @keypress="activeSearchTextValue"
        >
            <template #icon>
                <i class='bx bx-search'></i>
            </template>
        </vs-input>
    </div>
</template>
<script>
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        name: 'SearchArea',
        components: {
        },
        props: {
        },
        data: () => ({
            searchText: '',
            searchTextValue: false,
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
            ...mapGetters([
                'searchResult',
            ]),
        },
        methods: {
            ...mapMutations([
                'setSearchResult',
                'setLoadingMainPosts',
            ]),
            activeSearchTextValue () {
                this.searchTextValue = true
            },
            checkSearchText () {
                const length = this.searchText.length
                if (length === 0 || length > 40 || !this.searchTextValue) return
                this.$router.push({
                    path: '/search',
                    query: {
                        text: this.searchText
                    }
                })
                this.init()
                this.$emit('close')
            },
            init () {
                this.searchText = ''
                this.searchTextValue = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .vs-input-parent::v-deep {
        width: 100%;
        .vs-input {
            width: 100%;
        }
    }
</style>
