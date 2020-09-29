<template>
	<div>
		<v-container>
			<v-row>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							133
						</v-card-title>

						<v-card-subtitle>Nombre de mots</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							133
						</v-card-title>

						<v-card-subtitle>Nombre de mots</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							133
						</v-card-title>

						<v-card-subtitle>Nombre de mots</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-3">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							133
						</v-card-title>

						<v-card-subtitle>Nombre de mots</v-card-subtitle>
					</v-card>
				</v-col>
				<v-col class="col-md-12">
					<v-card color="#385F73" dark>
						<v-card-title class="headline">
							133
						</v-card-title>

						<v-card-subtitle>Nombre de mots</v-card-subtitle>
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
		}),

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
