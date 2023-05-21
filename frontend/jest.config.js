module.exports = {
  transform: {
    "^.+\\.vue$": "@vue/vue3-jest",
    "^.+\\.js$": "babel-jest",
  },
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  "moduleNameMapper": {
    "\\.(css|less)$": "<rootDir>/__mocks__/styleMock.js"
  },
   collectCoverageFrom: [
     'src/components/**/*.{js,vue,ts}',
     'src/views/**/*.{js,vue,ts}',
     '!src/main.ts', // Exclude the main.js file or other entry points
     '!**/node_modules/**',
     '!src/api/EchoFetch/**',
   ],
}
