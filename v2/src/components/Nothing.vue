<template>
    <div>
        <div class="text-center content-center flex flex-wrap">
            <ExclamationIcon class="text-center w-32 h-32 text-red-500" aria-hidden="true" />
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