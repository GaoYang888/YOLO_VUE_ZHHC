import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import axios from 'axios'
import Element from 'element-ui'
import echarts from "echarts";

Vue.prototype.$echarts = echarts;
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'

import JsonViewer from 'vue-json-viewer';
Vue.use(JsonViewer);

Vue.use(Element)
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$http = axios

// Import your Login component
import Login from './components/Login.vue'

const router = new VueRouter({
    routes: [
        { path: "/", component: Login }, // Set Login.vue as the default route
        // Define other routes here
    ],
    mode: "history"
})

new Vue({
    el: '#app',
    router,
    render: h => h(App)
})
