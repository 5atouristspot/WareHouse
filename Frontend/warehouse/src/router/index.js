import Vue from 'vue'
import Router from 'vue-router'
import Index from '../views/index'
import Login from '../views/login'
import plan from '@/pages/plan'
import batch from '@/pages/batch'
import detail from '@/pages/detail'
import search from '@/pages/search'
import supplier from '@/pages/supplier'
import warehouse from '@/pages/warehouse'
import HelloWorld from '@/components/HelloWorld'
import SearchInfo from '@/components/SearchInfo'
import wtbutton from '@/components/Button'

Vue.use(Router)

// 页面刷新时，重新赋值token
if (sessionStorage.getItem('token')) {
store.commit('set_token', sessionStorage.getItem('token'))
}

export default new Router({
    routes: [{
        path: '/',
        name: 'index',
        component: Index,
        meta: {
            required: true,
        }
    }, {
        path: '/login',
        name: 'login',
        component: Login,
    }, {
        path: '/helloworld',
        name: 'HelloWorld',
        component: HelloWorld,
    }, {
        path: '/searchinfo',
        name: 'SearchInfo',
        component: SearchInfo,
    }, {
        path: '/wtbutton',
        name: 'wtbutton',
        component: wtbutton
    }, {
      path: '/plan',
      name: 'plan',
      component: plan
    }, {
      path: '/warehouse/:type',
      name: 'warehouse',
      component: warehouse
    }, {
      path: '/batch/:type',
      name: 'batch',
      component: batch
    }, {
      path: '/detail/:type/:binum/:batchType',
      name: 'detail',
      component: detail
    }, {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/supplier',
      name: 'supplier',
      component: supplier
    }]
})
