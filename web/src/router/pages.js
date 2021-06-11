import { Home, Programming, Music, Category, About, Work, Contact } from '@/views/index'

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
        path: '/programming',
        name: 'Programming',
        component: Programming
    },
    {
        path: '/music',
        name: 'Music',
        component: Music
    },
    {
        path: '/category',
        name: 'Category',
        component: Category
    },
    {
        path: '/about',
        name: 'About',
        component: About
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
    }
]

export default routes
