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
                <div class="text-center text-3xl cursor-default" v-html="fullmanuscrit"></div>
            </div>
        </div>
        <div v-if="menuChange == 'men' && isSearching != '' && !isLoading">
            <div class="container py-10">
                <div class="text-center text-3xl cursor-default" v-html="fulltextmentions"></div>
            </div>
        </div>
        <div v-if="menuChange == 'pred' && isSearching != '' && !isLoading">
            <div class="py-5">
            <div class="flex flex-row-reverse mb-5">
                <a @click="download" class="hover:border-4 border-black border-2 py-2 px-4 cursor-pointer rounded-md bg-gray-100"><DownloadIcon class="w-5 h-5 pt-1 absolute" aria-hidden="true" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Télécharger le fichier source</a>
            </div>
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
import { DownloadIcon } from '@heroicons/vue/solid'

export default {
    components: {
        Nothing,
        DownloadIcon
    },

    data() {
        return { 
            fulltextmentions: '',
            fullmanuscrit: ''
        }
    },

    watch: {
        isResults: function () {
            // Mentions
            let texte = this.$store.state.search;
            let texte2 = this.$store.state.search;
            // let mentions = "";
            let truementions = [];
            this.isResults.data.forEach(ct => {
                console.log(ct);
                truementions.push(ct.M1_CONTENT);
                truementions.push(ct.M2_CONTENT);
            });
            console.log(truementions);


            // Mentions create
            truementions.forEach(word => {
                texte = texte.replace(word, `<span class="underline">${word}</span>`);
            });
            this.fulltextmentions = texte;

            // Manuscrit
            // let manuscit = "";
            let loopI = 0;
            let colors = ["bg-red-300", "bg-yellow-300", "bg-green-300", "bg-blue-300", "bg-pink-300"]
            this.isResults.data.forEach(ct => {
                if (ct.PREDICTION == 1 && loopI < 5) {
                    texte2 = texte2.replace(ct.M1_CONTENT, `<span class="${colors[loopI]}">${ct.M1_CONTENT}</span>`);
                    texte2 = texte2.replace(ct.M2_CONTENT, `<span class="${colors[loopI]}">${ct.M2_CONTENT}</span>`);
                    loopI += 1;
                }
            });

            if (loopI == 0) {
                texte2 += `<br/><br/><p class="text-sm text-center ">(Aucune coréférence n'a été détectée)</p>`
            }
            
            this.fullmanuscrit = texte2;
        },
    },

    methods: {
        generateDownload(filename, text) {
            var element = document.createElement("a");
            element.setAttribute(
                "href",
                "data:json/plain;charset=utf-8," + encodeURIComponent(text)
            );
            element.setAttribute("download", filename);

            element.style.display = "none";
            document.body.appendChild(element);

            element.click();

            document.body.removeChild(element);
		},
        download() {
            this.generateDownload("coref.json", JSON.stringify(this.isResults.data));
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