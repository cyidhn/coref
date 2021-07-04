import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import './style.css'

// Create a new store instance.
const store = createStore({
    state() {
        return {
            count: 0,
            menu: "man"
        }
    },
    mutations: {
        increment(state) {
            state.count++
        },
        changeMenu(state, n) {
            state.menu = n
        }
    },
    getters: {
        menuChoice(state) {
            return state.menu
        }
    }
})

const app = createApp(App)
app.use(store)
app.mount('#app')
