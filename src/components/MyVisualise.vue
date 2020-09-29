<template>
	<div v-if="view">
		<v-container>
			<v-row class="mb-5 text-center">
				<h2 class="text-center">Mes visualisations</h2>
			</v-row>
			<v-row class="mb-10">
				<v-expansion-panels>
					<v-expansion-panel v-for="(item, i) in folders" :key="i">
						<v-expansion-panel-header>
							{{ item.name }}
						</v-expansion-panel-header>
						<v-expansion-panel-content>
							<div>
								<hr />
								<TextTruncate class="mt-3">
									{{ item.text }}
								</TextTruncate>
								<v-btn
									class="mt-5"
									block
									color="warning white--text"
									@click="view(item.link)"
								>
									Voir l'analyse de coréférence pour ce texte
								</v-btn>
							</div>
						</v-expansion-panel-content>
					</v-expansion-panel>
				</v-expansion-panels>
			</v-row>
			<hr />
		</v-container>
	</div>
</template>

<script>
	export default {
		name: "MyVisualise",

		components: {},

		data: () => ({
			view: false,
			folders: [],
		}),

		mounted() {
			if (localStorage.getItem("folders")) {
				this.folders = JSON.parse(localStorage.getItem("folders"));
				this.view = true;
			}
		},

		methods: {
			view(link) {
				console.log(link);
				this.$router.push("start");
			},
		},
	};
</script>

<style scoped>
	.elevation-1 {
		width: 100% !important;
	}
</style>
