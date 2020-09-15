<template>
	<v-app>
		<v-app-bar app color="primary" dark>
			<div class="d-flex align-center">
				<h2>Coréférence</h2>
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
</template>

<script>
	import HelloWorld from "./components/HelloWorld";

	export default {
		name: "App",

		components: {
			HelloWorld,
		},

		data: () => ({
			//
		}),
	};
</script>
