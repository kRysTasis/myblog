<template>
    <div id="sidebar">
        <v-card
            flat
        >
            <v-divider/>
            <v-card-title
                class="center"
            >
                Recommend
            </v-card-title>
            <v-divider/>
            <v-card-text>
                post1
            </v-card-text>
            <v-card-text>
                post2
            </v-card-text>
            <v-card-text>
                post3
            </v-card-text>
            <v-divider/>
            <v-card-title
                class="center"
            >
                Recommend
            </v-card-title>
            <v-divider/>
            <v-card-text>
                post1
            </v-card-text>
            <v-card-text>
                post2
            </v-card-text>
            <v-card-text>
                post3
            </v-card-text>
        </v-card>
    </div>
</template>
<script>
    export default {
        name: 'Sidebar',
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
    #sidebar {
        margin-top: 40px;
        // width: 350px;
        height: 700px;
        // background-color: rgba(150, 150, 150, 0.1);
        .center {
            text-align: center;
            margin: 0 auto;
            display: block;
        }
    }
</style>
