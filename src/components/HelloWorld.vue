<template>
	<div>
		<MyVisualise />
		<v-container>
			<v-row class="text-center">
				<v-col class="mb-4">
					<h1 class="display-2 font-weight-bold mb-3 mt-4">
						Résolution de coréférence en français
					</h1>

					<h2 class="subheading font-weight-regular">
						L'interface qui vous permet de détecter et de résoudre les problèmes
						de coréférence.
					</h2>
				</v-col>

				<v-col class="col-md-12">
					<v-img
						:src="require('../assets/solve.svg')"
						class="my-3"
						contain
						height="300"
					/>
				</v-col>

				<v-col class="col-md-12">
					<p class="text-center">
						Une interface simple d'utilisation, totalement Open Source et
						entièrement sécurisée.
					</p>
				</v-col>

				<v-col class="col-md-6">
					<v-btn block color="warning" class="white--text" @click="toStart"
						>Commencer maintenant ></v-btn
					>
				</v-col>

				<v-col class="col-md-6">
					<v-btn block color="black" class="white--text" @click="toAbout"
						>En savoir plus... ></v-btn
					>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
	import MyVisualise from "@/components/MyVisualise.vue";

	export default {
		name: "HelloWorld",

		components: {
			MyVisualise,
		},

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
