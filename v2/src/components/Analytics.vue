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
            <div class="container py-10">
                <div class="text-center text-3xl" v-html="fulltextmentions"></div>
            </div>
        </div>
        <div v-if="menuChange == 'men' && isSearching != '' && !isLoading">
            <div class="container py-10">
                <div class="text-center text-3xl" v-html="fulltextmentions"></div>
            </div>
        </div>
        <div v-if="menuChange == 'pred' && isSearching != '' && !isLoading">
            <div class="container py-10">
            <div class="flex flex-col ">
                <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                    <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                        <tr>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            ID
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            M1
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            M2
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Prédiction
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Probabilité
                            </th>
                        </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                        <tr v-for="(ct, i) in isResults.data" :key="i">
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                {{i}}
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                               {{ ct.M1_CONTENT }}
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                {{ ct.M2_CONTENT }}
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                {{ ct.PREDICTION }}
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                               {{ ct.PROBABILITY }}
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
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

    data() {
        return { 
            fulltextmentions: ''
        }
    },

    watch: {
        isResults: function () {
            // Mentions
            let texte = this.$store.state.search;
            texte = texte.split(" ");
            let mentions = "";
            let truementions = [];
            this.isResults.data.forEach(ct => {
                console.log(ct);
                truementions.push(ct.M1_CONTENT.replace(" ", ""));
                truementions.push(ct.M2_CONTENT.replace(" ", ""));
            });
            console.log(truementions);

            // Mentions create
            texte.forEach(word => {
                if (truementions.includes(word)) {
                    mentions += `<span class="underline">${word}</span> `;
                } else {
                    mentions += `${word} `;
                }
            });
            this.fulltextmentions = mentions;

        },
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
        isResults() {
            return this.$store.getters.viewResults;
        },
    }
}
</script>