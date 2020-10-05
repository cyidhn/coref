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
					></v-data-table>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	import axios from "axios";

	export default {
		name: "VisualiseTab",

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
			],
		}),

		created() {
			// Retrouver les donnees
			this.ref = this.$route.params.id;

			// Call analyse
			let oldFolders = JSON.parse(localStorage.getItem(this.ref));
			if (oldFolders.visuTab) {
				this.loading = false;
				this.content = oldFolders.visuTab;
			} else {
				this.getJson();
			}
		},

		methods: {
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
