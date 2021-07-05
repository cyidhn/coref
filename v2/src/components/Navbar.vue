<template>
<div>
    <div class="p-5">
        <div class="grid grid-flow-col">
            <div><h1 class="text-4xl font-bold"><a href="/">Co.Ref</a></h1></div>
            <div class="flex flex-col items-end justify-center">
                <AlgorithmsList />
            </div>
            <!-- <br/><br/> -->
            <!-- <AlgorithmsList /> -->
        </div>
        <div class="mt-8">
            <input type="text" v-model="search" class="rounded-md p-2 h-12 focus:outline-none border-black border-2 w-full" />
        </div>
    </div>
    <div class="mt-5 px-5 py-5 bg-black text-white text-lg text-center">
        <a @click="callViz('man')" class="cursor-pointer mx-3">Visualisation manuscrite</a> - 
        <!-- <a @click="callViz('col')" class="cursor-pointer mx-3">Visualisation colorée</a> -  -->
        <a @click="callViz('men')" class="cursor-pointer mx-3">Visualisation des mentions</a> - 
        <!-- <a @click="callViz('pai')" class="cursor-pointer mx-3">Les paires</a> -  -->
        <a @click="callViz('pred')" class="cursor-pointer mx-3">Les paires et les prédictions</a>
    </div>
</div>
</template>

<script>
import AlgorithmsList from "./AlgorithmsList.vue";
import _ from 'lodash';

export default {
    components: {
      AlgorithmsList,
    },

    data() {
        return { 
            search: "" 
        }
    },

    watch: {
        search: function () {
            this.$store.commit('changeSearch', this.search);
            if (this.search != "") {
                this.$store.commit('load', true);
                this.throttleMethod();
            } else {
                this.$store.commit('load', false);
            }
        },
    },

    methods: {
        callViz(n) {
            this.$store.commit('changeMenu', n);
            // console.log(this.$store.state.menu);
        },
        throttleMethod: _.debounce(function () {
            if (this.search != "") {
                console.log('Throttle button clicked!');
                this.$store.commit('load', false);
            }
        }, 2000)
    },
}
</script>