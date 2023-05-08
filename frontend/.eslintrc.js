module.exports = {
  root: true,

  env: {
    node: true
  },

  extends: [
    'plugin:vue/vue3-essential',
    '@vue/standard',
    '@vue/typescript'
  ],

  parserOptions: {
    parser: '@typescript-eslint/parser',
    babelOptions: {
      parserOpts: {
        plugins: ['typescript']
      }
    }
  },

  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'template-curly-spacing': 'off',
    indent: 'off',
    camelcase: 'off',
    'vue/no-v-text-v-html-on-component': 'off'
  },

  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ]
}
