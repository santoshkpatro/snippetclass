<template>
    <b-field :label="label" :horizontal="inline">
        <b-input
            :type="inputType"
            @input="updateValue"
            :value="value"
            :name="name"
            :required="required"
        >
        </b-input>
    </b-field>
</template>

<script>
export default {
    name: 'BaseInput',
    props: {
        value: {
            type: String,
            default: '',
        },
        label: {
            type: String,
            required: true,
        },
        message: {
            type: String,
            default: '',
        },
        name: {
            type: String,
            required: true,
        },
        inline: {
            type: Boolean,
            default: false,
        },
        required: {
            type: Boolean,
            default: false,
        },
        inputType: {
            type: String,
            default: 'text',
        },
    },
    methods: {
        updateValue(v) {
            this.$emit('input', v)
        },
    },
}
</script>

<style>
</style>