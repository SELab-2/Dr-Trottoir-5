module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  globals: {
    'vue-jest': {
      compilerOptions: {
        isCustomElement: tag => tag.startsWith('v-')
      }
    }
  }
}
