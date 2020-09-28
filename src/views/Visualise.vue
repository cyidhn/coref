<template>
	<div class="visualise-tab">
		<v-container>
			<v-row class="text-center">
				<h1>Visualisation : {{ $route.params.id }}</h1>
			</v-row>
			<v-row class="text-center mt-5 mb-3">
				<v-tabs color="black">
					<v-tab @click="toDashboard">Dashboard</v-tab>
					<v-tab @click="toTab">Visualisation en Tableau</v-tab>
					<v-tab @click="toText">Visualisation en Texte</v-tab>
				</v-tabs>
			</v-row>
		</v-container>
		<div v-if="link === 'dash'">
			<VisualiseDash />
		</div>
		<div v-if="link === 'tab'">
			<VisualiseTab />
		</div>
		<div v-if="link === 'text'">
			<VisualiseText />
		</div>
	</div>
</template>

<script>
	import VisualiseDash from "@/components/VisualiseDash.vue";
	import VisualiseTab from "@/components/VisualiseTab.vue";
	import VisualiseText from "@/components/VisualiseText.vue";

	export default {
		name: "Home",

		components: {
			VisualiseTab,
			VisualiseDash,
			VisualiseText,
		},

		data: () => ({
			link: "dash",
		}),

		methods: {
			toDashboard() {
				this.link = "dash";
			},
			toTab() {
				this.link = "tab";
			},
			toText() {
				this.link = "text";
			},
		},
	};
</script>
