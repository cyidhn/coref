<template>
	<div>
		<v-container>
			<v-row class="text-center">
				<v-data-table
					item-key="name"
					class="elevation-1 black--text"
					loading
					loading-text="Chargement en cours, merci de patienter..."
				></v-data-table>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	export default {
		name: "VisualiseTab",

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
