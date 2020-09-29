<template>
	<div class="visualise-tab">
		<v-container>
			<v-row class="text-center mb-2">
				<v-col cols="12">
					<small class="text-uppercase mb-8">Nom de votre projet</small>
					<h1 class="text-uppercase">{{ visuDesc.name }}</h1>
				</v-col>
			</v-row>
			<v-row class="text-center mt-1 mb-8">
				<v-col cols="12">
					<v-tabs centered color="black">
						<v-tab @click="toDashboard">Dashboard</v-tab>
						<v-tab @click="toTab">Visualisation en Tableau</v-tab>
						<v-tab @click="toText">Visualisation en Texte</v-tab>
					</v-tabs>
				</v-col>
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
			visuDesc: null,
		}),

		mounted() {
			let noVisu = this.$route.params.id;
			this.visuDesc = JSON.parse(localStorage.getItem(noVisu));
		},

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
