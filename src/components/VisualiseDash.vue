<template>
	<div>
		<v-container>
			<p>Dashboard...</p>
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
