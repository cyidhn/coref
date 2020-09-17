<template>
	<!-- 
    /** ATTENTION **/
    Selon la licence, il est strictement interdit de modifier ces mentions 
    et ce Footer pour votre projet.
    -->
	<v-container class="mt-15 board">
		<v-row>
			<v-col class="text-left col-md-6">
				<v-img
					:src="require('../assets/idhn.jpeg')"
					class="my-3"
					contain
					width="100"
				/>
			</v-col>
			<v-col class="text-right col-md-6 pt-8">
				<p>© Laboratoire IDHN - Développé par @DemangeJeremy</p>
			</v-col>
		</v-row>
	</v-container>
</template>

<style scoped>
	.board {
		border-top: 2px solid black;
	}
</style>
