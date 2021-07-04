<template>
    <div class="p-5">
        <div class="flex grid grid-cols-2">
            <div><h1 class="text-4xl font-bold">Co.Ref</h1></div>
            <div class="justify-self-end">aa</div>
        </div>
        <AlgorithmsList />
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