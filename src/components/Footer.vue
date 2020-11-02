<template>
	<!-- 
    /** ATTENTION **/
    Selon la licence, il est strictement interdit de modifier ces mentions 
    et ce Footer pour votre projet.
    -->
	<v-container class="mt-15 board">
		<v-row>
			<v-col class="text-center col-md-12">
				<a
					href="https://www.u-cergy.fr/fr/laboratoires/idhn.html"
					target="_blank"
				>
					<v-img
						:src="require('../assets/LogoCY.png')"
						class="my-3"
						contain
						height="50"
					/>
				</a>
			</v-col>
			<v-col class="text-center col-md-12 pt-5">
				<p class="font-weight-bold">
					© Laboratoire IDHN - 2020
				</p>
				<p>
					Développé par
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
		border-top: 5px solid black;
	}

	a {
		color: black;
	}

	p {
		margin-bottom: 5px;
	}
</style>
