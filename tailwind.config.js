/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // templates of project level
    "./**/templates/**/*.html", // templates of app level
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

