<template>
	<div v-if="view">
		<v-container>
			<p>My visualise...</p>
		</v-container>
	</div>
</template>

<script>
	export default {
		name: "MyVisualise",

		components: {},

		data: () => ({
			view: false,
		}),

		mounted() {
			if (localStorage.getItem("folders")) {
				this.view = true;
			}
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
