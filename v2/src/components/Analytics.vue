<template>
    <div>
        <div v-if="menuChange == 'pred'">
            <p>Hello</p>
        </div>
    </div>
</template>

<script>
export default {
    computed: {
      menuChange() {
        return this.$store.getters.menuChoice;
      }
    }
}
</script>