// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// 导入element-ui
import Element from "element-ui"
// 导入样式
import "element-ui/lib/theme-chalk/index.css"
Vue.use(Element)

import axios from "axios";
Vue.prototype.$axios=axios

import "../src/assets/style.css"


Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
