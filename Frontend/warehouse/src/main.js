// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import axios from 'axios'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.use(iView)
Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:3622'
axios.defaults.auth = {
      username: localStorage.token,
      password: 'unused',
}



//axios.defaults.headers.common['Authentication-Token'] = store.state.token;
/*
axios.interceptors.request.use(
  config => {
    if (localStorage.getItem('token')) {
      config.headers.Authorization = localStorage.getItem('token');
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  });
*/

/*
axios.interceptors.request.use((config) => {
     console.log(config)
     return config;
 }, (error) => {
     return Promise.reject(error)
 })
*/
/*
//添加一个请求拦截器
axios.interceptors.request.use(
config => {
// config.headers['Content-Type'] = 'application/x-www-form-urlencoded';
        let token =localStorage.getItem('token')
　　　　　console.log(token)
if (token) {
config.headers.common['token'] =localStorage.getItem('token');
}
return config
},
err => {
return Promise.reject(err);
}
)
*/
/*
axios.interceptors.request.use(
  config => {
    if (localStorage.token) {  // 判断是否存在token，如果存在的话，则每个http header都加上token
      config.headers.Authorization = `token ${localStorage.token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  });
*/

axios.interceptors.response.use((response) => {
    return response;
}, (error) => {
    if (error.response) {
        switch (error.response.status) {
            case 401:
                store.commit('del_token')
                router.push('/login')
        }
    }
    return Promise.reject(error.response.data)
})

router.beforeEach((to, from, next) => {
    if (to.meta.required) {
        if (localStorage.token) {
            store.commit('set_token', localStorage.token)
            axios.defaults.auth = {
                username: store.state.token,
                password: store.state.token,
            }
            iView.LoadingBar.start();
            next()
        } else {
            next({
                path: '/login',
            })
        }
    } else {
        iView.LoadingBar.start();
        next()
    }
})

router.afterEach((to, from, next) => {
    iView.LoadingBar.finish();
})


Vue.prototype.$axios = axios
    /* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
})
