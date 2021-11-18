<template>
    <div class="container">
        <h1>Home</h1>
        <BaseInput
            v-model="email"
            label="Email"
            name="email"
            :required="true"
            inputType="email"
        />
        <BaseButton title="Click Me" size="medium" />
    </div>
</template>

<script>
import BaseInput from '@/components/base/BaseInput.vue'
import BaseButton from '@/components/base/BaseButton.vue'

export default {
    components: { BaseInput, BaseButton },
    data() {
        return {
            email: '',
        }
    },
}
</script>

<style>
</style>