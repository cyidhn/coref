import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import TextTruncate from "vue-text-truncate";

Vue.config.productionTip = false;
Vue.component("TextTruncate", TextTruncate);

new Vue({
	vuetify,
	router,
	render: (h) => h(App),
}).$mount("#app");
