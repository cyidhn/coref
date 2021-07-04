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
        <a href="#" class="font-bold mx-3">Visualisation manuscrite</a> - 
        <a href="#" class="mx-3">Visualisation colorique</a> - 
        <a href="#" class="mx-3">Liste des mentions</a> - 
        <a href="#" class="mx-3">Les paires</a> - 
        <a href="#" class="mx-3">Les prédictions</a>
    </div>
</div>
</template>

<script>
import AlgorithmsList from "./AlgorithmsList.vue";

export default {
    components: {
      AlgorithmsList,
    },
}
</script>