import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import './style.css'

// Create a new store instance.
const store = createStore({
    state() {
        return {
            count: 0,
            menu: "man",
            loading: false,
            search: ""
        }
    },
    mutations: {
        increment(state) {
            state.count++
        },
        load(state, n) {
            state.loading = n
        },
        changeMenu(state, n) {
            state.menu = n
        },
        changeSearch(state, n) {
            state.search = n
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
