<template>
	<div>
		<v-container v-if="loading">
			<v-row class="text-center">
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
			</v-row>
		</v-container>
		<v-container v-else>
			<v-row class="text-center">
				<v-col cols="12" class="mt-5 text-right">
					<iframe
						style="width:100%; height:600px"
						frameBorder="0"
						:src="content"
					></iframe>
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
		name: "VisualiseReine",
		props: ["name"],
		components: {},

		data: () => ({
			texte: "",
			search: "",
			loading: true,
			ref: null,
			content: null,
		}),

		created() {
			// Retrouver les donnees
			this.ref = this.$route.params.id;

			// Call analyse
			let oldFolders = JSON.parse(localStorage.getItem(this.ref));
			this.texte = oldFolders.text;
			if (oldFolders.getIframe) {
				this.loading = false;
				// this.content = process.env.VUE_APP_API + "/static/" + oldFolders.getIframe + ".html";
				this.content = oldFolders.getIframe;
			} else {
				this.getContent();
			}
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
				this.generateDownload(
					this.name + ".json",
					JSON.stringify(this.content)
				);
			},
			getContent() {
				let formData = new FormData();
				formData.append("link", this.ref);
				formData.append("texte", this.texte);
				axios
					.post(process.env.VUE_APP_API + "/algo-reine", formData)
					.then((response) => {
						this.loading = false;
						this.content = response.data.data;

						// Sauvegarder le contenu
						let oldFolders = JSON.parse(localStorage.getItem(this.ref));
						oldFolders.getIframe =
							process.env.VUE_APP_API +
							"/static/" +
							response.data.data +
							".html";
						this.content = oldFolders.getIframe;
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
