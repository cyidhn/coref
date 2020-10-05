<template>
	<div>
		<v-container>
			<v-row>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							{{ nbChars }}
						</v-card-title>

						<v-card-subtitle>Nombre de caractères</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							{{ nbWords }}
						</v-card-title>

						<v-card-subtitle>Nombre de mots</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							{{ nbSentences }}
						</v-card-title>

						<v-card-subtitle>Nombre de phrases</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							3
						</v-card-title>

						<v-card-subtitle>Visualisations disponibles</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-12">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							10s
						</v-card-title>

						<v-card-subtitle>Temps de traitement du corpus</v-card-subtitle>
					</v-card>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	export default {
		name: "VisualiseDash",

		components: {},

		data: () => ({
			texte: "",
			loading: false,
			ref: null,
			content: null,
			nbWords: 0,
			nbChars: 0,
			nbSentences: 0,
		}),

		created() {
			// Retrouver les donnees
			this.ref = this.$route.params.id;
			this.content = JSON.parse(localStorage.getItem(this.ref));
			this.texte = this.content.text;

			// Nombre de mots
			this.nbWords = this.texte.split(" ").length;

			// Nombre de caracteres
			this.nbChars = this.texte.length;

			// Nombre de phrases
			this.nbSentences = this.texte.split(/[.!?]/).length;
			this.nbSentences = this.nbSentences - 1;
		},

		methods: {
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
