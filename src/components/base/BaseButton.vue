<template>
    <b-button
        :native-type="buttonType"
        :type="designType"
        :class="{ medium: size === 'medium' }"
        >{{ title }}</b-button
    >
</template>

<script>
export default {
    name: 'BaseButton',
    props: {
        title: {
            type: String,
            required: true,
        },
        buttonType: {
            type: String,
            default: 'button',
        },
        designType: {
            type: String,
            default: 'is-primary',
        },
        size: {
            type: String,
            default: '',
        },
    },
}
</script>

<style scoped>
.medium {
    padding: 30px 20px;
}
</style>