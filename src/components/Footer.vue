<template>
	<!-- 
    /** ATTENTION **/
    Selon la licence, il est strictement interdit de modifier ces mentions 
    et ce Footer pour votre projet.
    -->
	<v-container class="mt-15 board">
		<v-row>
			<v-col class="text-left col-md-6">
				<a
					href="https://www.u-cergy.fr/fr/laboratoires/idhn.html"
					target="_blank"
				>
					<v-img
						:src="require('../assets/idhn.jpeg')"
						class="my-3"
						contain
						width="100"
					/>
				</a>
			</v-col>
			<v-col class="text-right col-md-6 pt-5">
				<p>
					© Laboratoire IDHN - 2020
				</p>
				<p>
					Développé avec ❤️ par
					<a href="https://twitter.com/demangejeremy" target="_blank"
						>@DemangeJeremy</a
					>
				</p>
			</v-col>
		</v-row>
	</v-container>
</template>

<style scoped>
	.board {
		border-top: 2px solid black;
	}

	a {
		color: black;
	}

	p {
		margin-bottom: 5px;
	}
</style>
