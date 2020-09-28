<template>
	<div class="visualise-tab">
		<VisualiseTab />
	</div>
</template>

<script>
	// @ is an alias to /src
	import VisualiseTab from "@/components/VisualiseTab.vue";

	export default {
		name: "Home",
		components: {
			VisualiseTab,
		},
	};
</script>
