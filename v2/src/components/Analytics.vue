<template>
    <div class="my-10 mx-5 py-5">
        <div v-if="isSearching == '' && !isLoading">
            <Nothing />
        </div>
        <div v-if="isLoading">
            <h2 class="text-center text-xl">Chargement en cours...</h2>
            <p class="text-center text-sm">(peut prendre jusqu'à plusieurs minutes)</p>
        </div>
        <div v-if="menuChange == 'man' && isSearching != '' && !isLoading">
            <p>Hello</p>
        </div>
        <div v-if="menuChange == 'men' && isSearching != '' && !isLoading">
            <div class="container py-10">
                <img class="mx-auto" src="/img/exemple_mentions.png" height="100%" />
            </div>
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