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
        'no-mixed-operators': ['error', { allowSamePrecedence: true }],
        'quotes': [2, "single", { "avoidEscape": true, "allowTemplateLiterals": true }],
        'indent': ['error', 4],
        'semi': ['error', "always"],
        'object-curly-spacing': ['error', 'never'],
        'space-before-blocks': ['error', 'always']
    },
    overrides: [
        {
            'files': ['*.js'],
            'rules': {
                'max-len': ['error', { code: 100 }],
            }
        }
    ],
    parserOptions: {
        parser: 'babel-eslint'
    }
};
