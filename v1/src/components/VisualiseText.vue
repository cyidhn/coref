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

				<v-col cols="12" class="text-left">
					<text-highlight :queries="search">
						{{ texte }}
					</text-highlight>
				</v-col>

				<v-col cols="12" class="mt-5 text-right">
					<v-btn depressed @click="download">
						<v-icon light class="mr-2">mdi-upload</v-icon>
						Télécharger le texte
					</v-btn>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	export default {
		name: "VisualiseText",
		props: ["name"],

		components: {},

		data: () => ({
			texte: "",
			search: "",
			ref: null,
			loading: false,
		}),

		created() {
			// Retrouver les donnees
			this.ref = this.$route.params.id;

			// Call analyse
			let oldFolders = JSON.parse(localStorage.getItem(this.ref));
			this.texte = oldFolders.text;
		},

		methods: {
			generateDownload(filename, text) {
				var element = document.createElement("a");
				element.setAttribute(
					"href",
					"data:text/plain;charset=utf-8," + encodeURIComponent(text)
				);
				element.setAttribute("download", filename);

				element.style.display = "none";
				document.body.appendChild(element);

				element.click();

				document.body.removeChild(element);
			},
			download() {
				this.generateDownload(this.name + ".txt", this.texte);
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
