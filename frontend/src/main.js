import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import "./assets/tailwind.css";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faCrown, faRobot, faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
library.add(faRobot, faUser, faCrown);
Vue.component("font-awesome-icon", FontAwesomeIcon);

// bootstrap
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.config.productionTip = false;

//fontAwesome
import "./fontAwesomeIcon.js"; // fontAwesomeIcon.js 불러옴

//vue-cookie
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)


new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>",
});
