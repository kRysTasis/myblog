<template>
    <div id="breadcrumbs">
        <v-breadcrumbs>
            <v-breadcrumbs-item
                href='/'
            >
                Home
            </v-breadcrumbs-item>

            <div
                v-for="(item, i) in breadItem"
                :key="i"
                class="breadcrumb_item"
            >
                <span class="bread_divider">></span>
                <v-breadcrumbs-item
                    @click="toPage(item)"
                    :disabled=item.disabled
                    class="ma-0 pa-0 link_btn"
                >{{ item.name }}</v-breadcrumbs-item>
            </div>
        </v-breadcrumbs>
    </div>
</template>
<script>
    export default {
        name: '',
        components: {
        },
        props: {
            breadItem: {
                type: Array,
                required: true,
                default: () => ([])
            }
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
            toPage (item) {
                console.log('item', item)
                this.$router.push({
                    path: '/category/',
                    query: {
                        name: item.slug
                    }
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #breadcrumbs {
        .breadcrumb_item {
            display: flex;
            .link_btn {
                color: #1976d2;
                cursor: pointer;
            }
        }
        .bread_divider {
            font-size: 12px;
            font-weight: normal;
            display: block;
            margin: 0 10px;
        }
    }
</style>
