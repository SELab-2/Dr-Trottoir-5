module.exports = {
  transform: {
    "^.+\\.vue$": "@vue/vue3-jest",
    "^.+\\.js$": "babel-jest",
  },
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  "moduleNameMapper": {
    "\\.(css|less)$": "<rootDir>/__mocks__/styleMock.js"
  },
  //collectCoverage: true,
  // collectCoverageFrom: [
  //   'src/**/*.{js,vue,ts}',
  //   '!src/main.js', // Exclude the main.js file or other entry points
  //   '!**/node_modules/**',
  // ],
  // coverageReporters: ['html', 'text-summary'],
}
