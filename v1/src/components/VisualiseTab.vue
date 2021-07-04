<template>
	<div>
		<v-container>
			<v-row class="text-center">
				<v-col cols="12" class="mb-4">
					<v-text-field
						v-model="search"
						append-icon="mdi-magnify"
						label="Rechercher"
						single-line
						hide-details
						outlined
						color="black"
					></v-text-field>
				</v-col>

				<v-col cols="12">
					<v-data-table
						class="elevation-1 black--text"
						:loading="loading"
						:items="content"
						:items-per-page="10"
						:headers="headers"
						loading-text="Chargement en cours, merci de patienter..."
						:search="search"
					>
						<template v-slot:[`item.actions`]="{ item }">
							<v-icon small class="mr-2" @click="seeYou(item)">
								mdi-eye
							</v-icon>
						</template>

						<template v-slot:[`item.Right_ID`]="{ item }">
							<span v-html="item.Right_ID"></span>
						</template>
						<template v-slot:[`item.Left_ID`]="{ item }">
							<span v-html="item.Left_ID"></span>
						</template>
					</v-data-table>
				</v-col>

				<v-col cols="12" class="mt-5 text-right">
					<v-btn depressed @click="download">
						<v-icon light class="mr-2">mdi-upload</v-icon>
						Télécharger le résultat
					</v-btn>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	import axios from "axios";

	export default {
		name: "VisualiseTab",
		props: ["name"],
		components: {},

		data: () => ({
			texte: "",
			search: "",
			loading: true,
			ref: null,
			content: [],
			headers: [
				{
					text: "Partie gauche",
					align: "start",
					sortable: false,
					value: "Left_ID",
				},
				{ text: "Partie droite", value: "Right_ID" },
				{ text: "Prédiction", value: "Prediction" },
				{ text: "Voir", value: "actions", sortable: false },
			],
		}),

		created() {
			// Retrouver les donnees
			this.ref = this.$route.params.id;

			// Call analyse
			let oldFolders = JSON.parse(localStorage.getItem(this.ref));
			this.texte = oldFolders.text;
			if (oldFolders.visuTab) {
				this.loading = false;
				this.content = oldFolders.visuTab;
			} else {
				this.getJson();
			}
		},

		methods: {
			seeYou(item) {
				console.log(item);
				let gauche = item.Left_ID;
				let droite = item.Right_ID;
				let dist = item.DISTANCE_WORD;
				let chars = item.DISTANCE_CHAR;
				let texte = this.texte;
				texte = texte.split(" ");
				let final = "";
				let count = 0;
				for (let i = 0; i < texte.length; i++) {
					let inProg = texte[i];
					let letterCount = inProg.replace(/\s+/g, "").length;
					if (count >= chars) {
						if (final == "") {
							final += gauche;
							let lenn = final.split(" ").length;
							i += lenn - 1;
						} else if (chars >= 0) {
							final += " " + inProg;
							chars -= 1;
						}
					}
					count += letterCount;
				}
				final += " " + droite;
				console.log(dist);
				console.log(final);
			},
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
				this.generateDownload(
					this.name + ".json",
					JSON.stringify(this.content)
				);
			},
			getJson() {
				let formData = new FormData();
				formData.append("link", this.ref);
				axios
					.post(process.env.VUE_APP_API + "/visu-texte-idhn", formData)
					.then((response) => {
						this.loading = false;
						this.content = response.data.data;

						// Sauvegarder le contenu
						let oldFolders = JSON.parse(localStorage.getItem(this.ref));
						oldFolders.visuTab = response.data.data;
						localStorage.setItem(this.ref, JSON.stringify(oldFolders));

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
						alert("Impossible de charger les données.");
						this.loading = false;
					});
			},
			toStart() {
				this.$router.push("start");
			},
			toAbout() {
				this.$router.push("about");
			},
		},
	};
</script>

<style scoped>
	.elevation-1 {
		width: 100% !important;
	}
</style>
