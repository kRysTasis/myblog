export default {
    methods: {
        toDetailPost (post) {
            this.$router.push({
                name: 'DetailPost',
                params: {
                    id: post.id
                }
            })
        }
    }
}
