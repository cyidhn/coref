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
									<h3 class="mb-8">
										Importer un fichier texte (en format classique ou en format
										Iramuteq)
									</h3>
									<v-text-field
										label="Nom de votre projet"
										v-model="projectName"
										color="black"
										outlined
									></v-text-field>
									<v-file-input
										accept=".txt"
										label="Importer un fichier texte"
										color="black"
										outlined
										v-model="fileText"
									></v-file-input>
								</template>

								<v-btn
									block
									color="warning"
									@click="toImportText"
									:disabled="!fileText || !projectName"
								>
									Continuer
								</v-btn>
								<v-btn
									class="mt-2"
									block
									color="black white--text"
									@click="e1++"
									:disabled="!projectName"
								>
									Saisir directement un texte
								</v-btn>
							</v-stepper-content>

							<v-stepper-content step="2">
								<h3 class="mb-8">
									Confirmer le texte saisi ou entrer un texte
								</h3>
								<v-textarea
									v-model="texte"
									label="Entrez votre texte ici..."
									color="black"
									outlined
								></v-textarea>
								<v-btn
									v-if="!loading"
									block
									color="warning"
									class="white--text"
									@click="viewResult"
									:disabled="!texte"
									>Valider mon texte et visualiser les résultats</v-btn
								>
								<v-btn
									class="mt-2"
									block
									color="black white--text"
									@click="e1--"
								>
									← Retour
								</v-btn>
							</v-stepper-content>

							<v-stepper-content step="3">
								<p class="mt-5 mb-5">
									Chargement en cours, cela peut prendre plusieurs minutes...
								</p>
								<v-progress-linear
									class="mb-5"
									indeterminate
									color="black"
									rounded
									height="6"
								></v-progress-linear>
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
			projectName: "",
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
				this.e1 += 1;
				let formData = new FormData();
				let numberWatch = new Date().getUTCMilliseconds();
				numberWatch = String(numberWatch);
				formData.append("texte", this.texte);
				formData.append("name", this.projectName);
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
