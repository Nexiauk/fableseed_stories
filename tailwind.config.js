/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {},
    screens: {
      '2xl': '2560px', // your custom 2xl breakpoint
    },
  },
  plugins: [],
}
