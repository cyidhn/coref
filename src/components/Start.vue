<template>
	<div>
		<v-container>
			<v-row class="text-center">
				<v-col class="mb-4">
					<h1 class="display-2 font-weight-bold mb-3 mt-4">
						Importer un texte et identifier les coréférences
					</h1>
				</v-col>

				<v-col cols="12">
					<v-stepper v-model="e1" class="myStepper">
						<v-stepper-header>
							<v-stepper-step color="warning" :complete="e1 > 1" step="1"
								>Importation du texte</v-stepper-step
							>

							<v-divider></v-divider>

							<v-stepper-step color="warning" :complete="e1 > 2" step="2"
								>Paramètres</v-stepper-step
							>

							<v-divider></v-divider>

							<v-stepper-step color="warning" step="3"
								>Visualiser les résultats</v-stepper-step
							>
						</v-stepper-header>

						<v-stepper-items>
							<v-stepper-content step="1">
								<template>
									<h3 class="mb-3">
										Importer un fichier texte (en format classique ou en format
										Iramuteq)
									</h3>
									<v-file-input
										accept=".txt"
										label="Importer un fichier texte"
										color="black"
										v-model="fileText"
									></v-file-input>
								</template>

								<v-btn
									block
									color="warning"
									@click="toImportText"
									:disabled="!fileText"
								>
									Continuer
								</v-btn>
								<v-btn
									class="mt-2"
									block
									color="black white--text"
									@click="e1++"
								>
									Saisir directement un texte
								</v-btn>
							</v-stepper-content>

							<v-stepper-content step="2">
								<h3 class="mb-3">
									Visualiser les résultats
								</h3>
								<v-textarea
									v-model="texte"
									label="Entrez votre texte ici..."
									color="black"
								></v-textarea>
								<v-btn
									v-if="!loading"
									block
									color="warning"
									class="white--text"
									@click="viewResult"
									>Valider mon texte et visualiser les résultats</v-btn
								>
								<v-btn
									v-if="loading"
									block
									color="black"
									class="white--text"
									disabled
								>
									<v-progress-circular
										indeterminate
										color="black"
									></v-progress-circular
									>Chargement en cours... (cela peut prendre plusieurs
									minutes)</v-btn
								>
							</v-stepper-content>

							<v-stepper-content step="3">
								<v-card
									class="mb-12"
									color="grey lighten-1"
									height="200px"
								></v-card>

								<v-btn color="primary" @click="e1 = 1">
									Continue
								</v-btn>

								<v-btn text>Cancel</v-btn>
							</v-stepper-content>
						</v-stepper-items>
					</v-stepper>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	import axios from "axios";

	// Test
	// const excelToJson = require("convert-excel-to-json");
	// const fs = require("fs");

	export default {
		name: "HelloWorld",

		components: {},

		data: () => ({
			texte: "",
			loading: false,
			fileText: null,
			e1: 1,
		}),

		methods: {
			toImportText() {
				// Test
				const file = this.fileText;
				const reader = new FileReader();
				reader.onload = (e) => {
					this.texte = e.target.result;
					// Traitements
					let textTraitement = this.texte;
					console.log();
					textTraitement = textTraitement.replace(/\s[*]\S+/g, "");
					textTraitement = textTraitement.replace("****", "");
					this.texte = textTraitement;
					// /Traitements
				};
				reader.readAsText(file);
				// /Test

				this.e1 += 1;
			},
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

						// window.open(
						// 	process.env.VUE_APP_API + "/static/" + numberWatch + ".xlsx",
						// 	"_blank"
						// );

						// const result = excelToJson({
						// 	source: fs.readFileSync(
						// 		process.env.VUE_APP_API + "/static/" + numberWatch + ".xlsx"
						// 	), // fs.readFileSync return a Buffer
						// });

						// console.log(result);
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

<style scoped>
	.myStepper {
		border: 3px solid black;
	}
</style>
