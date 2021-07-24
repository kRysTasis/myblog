<template>
    <div
        id="header_bottom"
    >
        <span
            v-for="(btn, i) in btnList"
            :key="i"
        >
            <v-btn
                text
                @click="toPage(btn)"
            >
                <i
                    :class=btn.iconClass
                    :style=btn.style
                ></i>
                {{ btn.text }}
            </v-btn>
        </span>
    </div>
</template>
<script>
    export default {
        name: 'HeaderBottom',
        props: {
        },
        data: () => ({
            btnList: [
                {
                    iconClass: 'bx bx-desktop',
                    style: 'color:rgba(255,37,88,0.8)',
                    // iconClass: 'bx bxl-python',
                    // iconClass: 'bx bxl-django',
                    text: 'programming',
                    slug: 'programming',
                    isCategory: true,
                },
                {
                    // iconClass: 'bx bxs-music',
                    iconClass: 'bx bx-music',
                    style: 'color:rgba(5,255,147,0.8)',
                    text: 'music',
                    slug: 'music',
                    isCategory: true,
                },
                {
                    // iconClass: 'bx bxs-category-alt',
                    iconClass: 'bx bx-category-alt',
                    // style: 'color:rgba(5,138,255,0.3)',
                    style: 'color:rgba(111,111,111,0.6)',
                    text: 'other',
                    slug: 'other',
                    isCategory: true,
                },
                {
                    // iconClass: 'bx bx-user-pin',
                    iconClass: 'bx bx-face',
                    // iconClass: 'bx bx-cool',
                    // iconClass: 'bx bx-user',
                    style: 'color:rgba(111,111,111,0.6)',
                    text: 'about',
                    slug: 'about',
                    isCategory: false,
                },
                {
                    iconClass: 'bx bx-folder',
                    // iconClass: 'bx bx-briefcase',
                    text: 'work',
                    slug: 'work',
                    isCategory: false,
                },
                {
                    iconClass: 'bx bx-mail-send',
                    text: 'contact',
                    slug: 'contact',
                    isCategory: false,
                },
            ],
        }),
        methods: {
            toProfile () {
                const elm = document.documentElement
                const bottom = elm.scrollHeight - elm.clientHeight
                window.scrollTo(({
                    top: bottom,
                    behavior: 'smooth'
                }))
            },
            toPage (item) {
                if (item.text === 'about') {
                    this.toProfile()
                    return
                }
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                })
                setTimeout(this.toCategoryPage, 300, item)
            },
            toCategoryPage (item) {
                if (item.isCategory) {
                    this.$router.push({
                        path: '/category',
                        query: {
                            name: item.slug
                        }
                    })
                } else {
                    this.$router.push({
                        path: '/' + item.slug
                    })
                }
            }
        },
    }
</script>
<style lang="scss" scoped>
    #header_bottom {
        font-family: 'Alegreya Sans SC', sans-serif;
        // max-width: 1200px;
        // height: 30px;
        // margin: 0 auto;
    }
</style>
