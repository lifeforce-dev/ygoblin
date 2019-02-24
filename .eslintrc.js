module.exports = {
    root: true,
    env: {
        node: true
    },
    extends: [
        'plugin:vue/essential',
    ],
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'max-len': ['error', { code: 100 }],
        'no-mixed-operators': ['error', { allowSamePrecedence: true }],
        "quotes": [2, "single", { "avoidEscape": true }],
        indent: ['error', 4]
    },
    parserOptions: {
        parser: 'babel-eslint'
    }
};
