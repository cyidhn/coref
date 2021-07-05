<template>
    <div class="my-10 mx-5">
        <div v-if="isSearching == '' && !isLoading">
            <Nothing />
        </div>
        <div v-if="isLoading">
            <h2 class="text-center text-xl">Chargement en cours...</h2>
        </div>
        <div v-if="menuChange == 'pred'">
            <p>Hello</p>
        </div>
    </div>
</template>

<script>
import Nothing from "./Nothing.vue";

export default {
    components: {
        Nothing
    },

    computed: {
        menuChange() {
            return this.$store.getters.menuChoice;
        },
        isSearching() {
            return this.$store.getters.viewSearch;
        },
        isLoading() {
            return this.$store.getters.viewLoad;
        },
    }
}
</script>