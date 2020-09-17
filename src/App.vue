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
				class="d-none d-sm-flex"
			>
				<span class="mr-2">Code source</span>
				<v-icon>mdi-open-in-new</v-icon>
			</v-btn>
		</v-app-bar>

		<v-main>
			<a href="#" @click="openChat">
				<v-alert type="warning">
					Actuellement en version bêta, n'hésitez pas à cliquer ici pour nous
					faire part de vos avis, commentaires ou éventuels bugs.<br />
					De nouvelles fonctionnalités sont prévues dans les jours à venir.
				</v-alert>
			</a>
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
				// Mettre le timeout si message bug non affiché
				let view = localStorage.getItem("bugMessage");
				if (!view) {
					setTimeout(this.bugMessage, 5000);
				}
			},
			bugMessage() {
				window.$crisp.push([
					"do",
					"message:show",
					[
						"text",
						"Bonjour, n'hésitez pas à nous signaler le moindre bug afin de corriger cela au plus vite. Merci :)",
					],
				]);
				localStorage.setItem("bugMessage", true);
			},
			openChat() {
				window.$crisp.push(["do", "chat:open"]);
			},
		},
	};
</script>

<style scoped>
	a {
		text-decoration: none;
	}
</style>
