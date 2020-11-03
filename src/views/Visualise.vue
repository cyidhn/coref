<template>
	<div class="visualise-tab">
		<v-container>
			<v-row class="mb-2">
				<v-col cols="6">
					<v-btn color="black white--text" @click="goBack">
						← Retour
					</v-btn>
				</v-col>
				<v-col cols="6" class="text-right">
					<v-btn color="black white--text" @click="goDelete">
						<v-icon aria-hidden="false" class="mr-2">
							mdi-delete
						</v-icon>
						Supprimer
					</v-btn>
				</v-col>
			</v-row>
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
						<v-tab @click="toReine">Visualisation avec Reine</v-tab>
					</v-tabs>
				</v-col>
			</v-row>
		</v-container>
		<div v-if="link === 'dash'">
			<VisualiseDash />
		</div>
		<div v-if="link === 'tab'">
			<VisualiseTab :name="visuDesc.name" />
		</div>
		<div v-if="link === 'text'">
			<VisualiseText :name="visuDesc.name" />
		</div>
		<div v-if="link === 'reine'">
			<VisualiseReine :name="visuDesc.name" />
		</div>
	</div>
</template>

<script>
	import VisualiseDash from "@/components/VisualiseDash.vue";
	import VisualiseTab from "@/components/VisualiseTab.vue";
	import VisualiseText from "@/components/VisualiseText.vue";
	import VisualiseReine from "@/components/VisualiseReine.vue";

	export default {
		name: "Visualise",

		components: {
			VisualiseTab,
			VisualiseDash,
			VisualiseText,
			VisualiseReine,
		},

		data: () => ({
			link: "dash",
			noVisu: null,
			visuDesc: {
				name: "",
			},
		}),

		mounted() {
			let noVisu = this.$route.params.id;
			this.noVisu = noVisu;
			this.visuDesc = JSON.parse(localStorage.getItem(noVisu));
		},

		methods: {
			splitArr(arr, attr, value) {
				var i = arr.length;
				while (i--) {
					let hasBarProperty = Object.prototype.hasOwnProperty.call(
						arr[i],
						attr
					);
					if (
						arr[i] &&
						hasBarProperty &&
						arguments.length > 2 &&
						arr[i][attr] === value
					) {
						arr.splice(i, 1);
					}
				}
				return arr;
			},
			goDelete() {
				if (confirm("Êtes-vous sûr de supprimer ces résulats ?")) {
					let list = JSON.parse(localStorage.getItem("folders"));
					list = this.splitArr(list, "link", this.noVisu);
					localStorage.setItem("folders", JSON.stringify(list));
					localStorage.removeItem(this.noVisu);
					this.$router.push("/");
				}
			},
			goBack() {
				this.$router.push("/");
			},
			toDashboard() {
				this.link = "dash";
			},
			toTab() {
				this.link = "tab";
			},
			toText() {
				this.link = "text";
			},
			toReine() {
				this.link = "reine";
			},
		},
	};
</script>
