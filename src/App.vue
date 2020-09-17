<template>
	<v-app v-if="!loading">
		<v-app-bar app color="white">
			<div class="text-left">
				<a href="/">
					<v-img
						:src="require('./assets/logo.png')"
						class="pos-img"
						contain
						width="150"
					/>
				</a>
			</div>

			<v-spacer></v-spacer>

			<v-btn
				href="https://github.com/demangejeremy/coreference-idhn"
				target="_blank"
				text
			>
				<span class="mr-2">Voir le code source</span>
				<v-icon>mdi-open-in-new</v-icon>
			</v-btn>
		</v-app-bar>

		<v-main>
			<HelloWorld />
		</v-main>
	</v-app>
	<v-app v-else>
		<v-main>
			<Loading />
		</v-main>
	</v-app>
</template>

<script>
	import HelloWorld from "./components/HelloWorld";
	import Loading from "./components/Loading";

	export default {
		name: "App",

		components: {
			HelloWorld,
			Loading,
		},

		data: () => ({
			// loading
			loading: true,
		}),

		created() {
			// Enlever Crisp bandeau
			window.$crisp.push(["do", "chat:hide"]);
			// Mettre le timeout
			setTimeout(this.begin, 3000);
		},

		methods: {
			begin() {
				// Fermer le loading
				this.loading = false;
				// Remettre le bandeau Crisp
				window.$crisp.push(["do", "chat:show"]);
			},
		},
	};
</script>
