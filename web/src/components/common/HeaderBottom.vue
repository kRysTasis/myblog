<template>
    <div class="header_bottom">
        <span
            v-for="(btn, i) in btnList"
            :key="i"
        >
            <v-btn
                text
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
        data: () => ({
            btnList: [
                {
                    iconClass: 'bx bx-desktop',
                    style: 'color:rgba(255,37,88,0.8)',
                    // iconClass: 'bx bxl-python',
                    // iconClass: 'bx bxl-django',
                    text: 'programming'
                },
                {
                    // iconClass: 'bx bxs-music',
                    iconClass: 'bx bx-music',
                    style: 'color:rgba(5,255,147,0.8)',
                    text: 'music'
                },
                {
                    // iconClass: 'bx bxs-category-alt',
                    iconClass: 'bx bx-category-alt',
                    // style: 'color:rgba(5,138,255,0.3)',
                    style: 'color:rgba(111,111,111,0.6)',
                    text: 'category'
                },
                {
                    // iconClass: 'bx bx-user-pin',
                    iconClass: 'bx bx-face',
                    // iconClass: 'bx bx-cool',
                    // iconClass: 'bx bx-user',
                    style: 'color:rgba(111,111,111,0.6)',
                    text: 'about'
                },
                {
                    iconClass: 'bx bx-folder',
                    // iconClass: 'bx bx-briefcase',
                    text: 'work'
                },
                {
                    iconClass: 'bx bx-mail-send',
                    text: 'contact'
                },
            ],
        }),
        methods: {

        },
    }
</script>
<style lang="scss" scoped>
    .header_bottom {
        font-family: 'Alegreya Sans SC', sans-serif;
        width: 1200px;
        height: 30px;
        margin: 0 auto;
        text-align: center;
    }
</style>
