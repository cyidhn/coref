<template>
<div>
    <div class="p-5">
        <div class="flex grid grid-cols-2">
            <div><h1 class="text-4xl font-bold"><a href="/">Co.Ref</a></h1></div>
            <div class="justify-self-end">
                <AlgorithmsList />
            </div>
        </div>
        <div class="mt-8">
            <input type="text" class="rounded-md p-2 h-12 focus:outline-none border-black border-2 w-full" />
        </div>
    </div>
    <div class="mt-5 px-5 py-5 bg-black text-white text-lg text-center">
        <a @click="callViz('man')" class="cursor-pointer mx-3">Visualisation manuscrite</a> - 
        <a @click="callViz('col')" class="cursor-pointer mx-3">Visualisation colorée</a> - 
        <a @click="callViz('men')" class="cursor-pointer mx-3">Liste des mentions</a> - 
        <a @click="callViz('pai')" class="cursor-pointer mx-3">Les paires</a> - 
        <a @click="callViz('pred')" class="cursor-pointer mx-3">Les prédictions</a>
    </div>
</div>
</template>

<script>
import AlgorithmsList from "./AlgorithmsList.vue";

export default {
    components: {
      AlgorithmsList,
    },

    methods: {
        callViz(n) {
            this.$store.commit('changeMenu', n);
            // console.log(this.$store.state.menu);
        }
    },
}
</script>