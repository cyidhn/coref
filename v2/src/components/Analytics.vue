<template>
    <div class="my-10 mx-5">
        <div>
            <Nothing />
        </div>
        <div v-if="menuChange == 'pred'">
            <p>Hello</p>
        </div>
    </div>
</template>

<script>
import Nothing from "./Nothing.vue";

export default {
    components: {
        Nothing
    },

    computed: {
      menuChange() {
        return this.$store.getters.menuChoice;
      }
    }
}
</script>