module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended'
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  rules: {
    'no-unused-vars': 'off', // Desactiva la advertencia de variables no usadas
    'vue/multi-word-component-names': 'off', // Permite nombres de componentes de una sola palabra
  },
};
