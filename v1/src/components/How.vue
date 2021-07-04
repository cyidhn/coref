<template>
	<div>
		<v-container>
			<v-row class="text-center">
				<v-col class="mb-4">
					<h1 class="display-2 font-weight-bold mb-3 mt-4">
						Système de résolution de coréférence
					</h1>

					<p class="subheading font-weight-regular">
						Entrez votre texte et téléchargez les résultats en un clic.
					</p>
				</v-col>

				<v-col cols="12">
					<v-textarea
						v-model="texte"
						label="Entrez votre texte ici..."
						color="black"
					></v-textarea>
				</v-col>
				<v-col class="mb-10" cols="12">
					<v-btn
						v-if="!loading"
						block
						color="black"
						class="white--text"
						@click="viewResult"
						>Valider mon texte et télécharger les résultats</v-btn
					>
					<v-btn v-if="loading" block color="black" class="white--text" disabled
						>Chargement en cours... (cela peut prendre plusieurs minutes)</v-btn
					>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	import axios from "axios";

	export default {
		name: "How",

		components: {},

		data: () => ({
			texte: "",
			loading: false,
		}),

		methods: {
			viewResult() {
				let formData = new FormData();
				let numberWatch = new Date().getUTCMilliseconds();
				numberWatch = String(numberWatch);
				formData.append("texte", this.texte);
				formData.append("link", numberWatch);
				console.log(process.env.VUE_APP_API);
				this.loading = true;
				axios
					.post(process.env.VUE_APP_API + "/importer-texte-idhn", formData)
					.then((response) => {
						console.log(response.data);
						this.loading = false;

						window.open(
							process.env.VUE_APP_API + "/static/" + numberWatch + ".xlsx",
							"_blank"
						);
					})
					.catch((e) => {
						this.getError = true;
						console.error("Impossible de charger les données", e);
						alert("Impossible de lancer l'algorithme...");
						this.loading = false;
					});
			},
		},
	};
</script>
