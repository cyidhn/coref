<template>
    <div>
        <div class="mt-20">
            <ExclamationIcon class="mx-auto w-32 h-32 text-red-500" aria-hidden="true" />
        </div>
        <div class="mb-20">
            <p class="text-center text-lg text-red-500">Écrivez un premier texte dans le formulaire en haut du menu pour l'analyser...</p>
        </div>
    </div>
</template>

<script>
import { ExclamationIcon } from '@heroicons/vue/outline'

export default {
    components: {
        ExclamationIcon
    }
}
</script>