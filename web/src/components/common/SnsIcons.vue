<template>
    <div id="sns_icon_area">
        <i
            class='bx bxl-github fa-lg github_icon mr-1'
            @click.stop.prevent='openMyGithub()'
        ></i>
        <i
            class="fab fa-twitter fa-lg twitter_icon"
            @click.stop.prevent="openMyTwitter()"
        ></i>
        <i
            @click='toQiita'
        >
            <v-img
                src="@/assets/img/qiita_icon_circle.png"
                class="qiita_icon"
                width="21"
                height="21"
            ></v-img>
        </i>
    </div>
</template>
<script>
    import { Const } from '@/assets/js/const'

    const Con = new Const()

    export default {
        name: '',
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
            openMyGithub () {
                window.open(Con.MY_GITHUB_URL, '_blink')
            },
            openMyTwitter () {
                window.open(Con.MY_TWITTER_URL, '_blink')
            },
            toQiita () {
                window.open(Con.MY_QIITA_URL, '_blink')
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #sns_icon_area {
        padding-left: 50px;
        .github_icon{
            cursor: pointer;
        }
        .twitter_icon {
            cursor: pointer;
            color: rgba(0,172,238,0.5);
        }
        .qiita_icon {
            display: inline-block;
            position: relative;
            left: 5px;
            top: 5.5px;
            cursor: pointer;
        }
    }
</style>
