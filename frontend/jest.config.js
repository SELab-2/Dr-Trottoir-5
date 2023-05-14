module.exports = {
  transform: {
    "^.+\\.vue$": "@vue/vue3-jest",
    "^.+\\.js$": "babel-jest",
  },
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  "moduleNameMapper": {
    "\\.(css|less)$": "<rootDir>/__mocks__/styleMock.js"
  },
}
