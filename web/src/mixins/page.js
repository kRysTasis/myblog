export default {
    methods: {
        toDetailPost (post) {
            this.$router.push({
                name: 'DetailPost',
                params: {
                    id: post.id
                }
            })
        },
        searchTag (tag) {
            this.$router.push({
                path: '/search',
                query: {
                    tag: tag.name
                }
            })
        }
    }
}
