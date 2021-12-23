import Vue from 'vue'
import VueRouter from 'vue-router'
import VueSession from 'vue-session'

Vue.use(VueRouter)
Vue.use(VueSession)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: () => import('@/views/Main.vue')
  },
  {
    path: '/auth',
    name: 'Callback',
    component: () => import('@/views/Callback.vue')
  },
  {
    path: '/landing',
    name: 'Landing',
    component: () => import('@/views/Landing.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
