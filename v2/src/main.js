import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import './style.css'

// Create a new store instance.
const store = createStore({
    state() {
        return {
            menu: "man",
            loading: false,
            search: "",
            algo: "crs",
            result: {}
        }
    },
    mutations: {
        load(state, n) {
            state.loading = n
        },
        changeResults(state, n) {
            state.result = n
        },
        changeMenu(state, n) {
            state.menu = n
        },
        changeSearch(state, n) {
            state.search = n
        },
        changeAlgo(state, n) {
            state.algo = n
        }
    },
    getters: {
        menuChoice(state) {
            return state.menu
        },
        viewLoad(state) {
            return state.loading
        },
        viewSearch(state) {
            return state.search
        }
    }
})

const app = createApp(App)
app.use(store)
app.mount('#app')
