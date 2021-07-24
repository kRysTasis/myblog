import { Home, DetailCategory, Work, Contact, DetailPost, SearchResult, TagSearchResult } from '@/views/index'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            description: 'ブログトップ'
        },
    },
    {
        path: '/post/:id',
        name: 'DetailPost',
        component: DetailPost,
    },
    {
        path: '/category',
        name: 'DetailCategory',
        component: DetailCategory,
    },
    {
        path: '/tag',
        name: 'TagSearchResult',
        component: TagSearchResult,
    },
    {
        path: '/work',
        name: 'Work',
        component: Work
    },
    {
        path: '/contact',
        name: 'Contact',
        component: Contact
    },
    {
        path: '/search',
        name: 'SearchResult',
        component: SearchResult
    },
]

export default routes
