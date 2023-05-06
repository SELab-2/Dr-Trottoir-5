module.exports = {
  globals: {
    'vue-jest': {
      compilerOptions: {
        isCustomElement: tag => tag.startsWith('v-')
      }
    }
  },
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  "moduleNameMapper": {
    "\\.(css|less)$": "<rootDir>/__mocks__/styleMock.js"
  },
}
