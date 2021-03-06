import Vue from 'vue'
import VueRouter from 'vue-router'
import VueSession from 'vue-session'
import VueCookie from 'vue-cookie'

Vue.use(VueRouter)
Vue.use(VueSession)
Vue.use(VueCookie)

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
