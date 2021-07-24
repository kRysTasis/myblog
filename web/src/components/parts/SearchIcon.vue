<template>
    <div id="search_icon">
        <i
            class='bx bx-search header_search_btn'
            @click="searchDialog=!searchDialog"
        ></i>
        <SearchDialog
            @update="searchDialog = $event"
            :searchDialog="searchDialog"
        />
    </div>
</template>
<script>
    import SearchDialog from '@/components/parts/SearchDialog'

    export default {
        name: 'SearchIcon',
        components: {
            SearchDialog
        },
        props: {
        },
        data: () => ({
            searchDialog: false,
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
    #search_icon::v-deep {
        .header_search_btn {
            cursor: pointer;
        }
    }
</style>
