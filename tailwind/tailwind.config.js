/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../**/templates/**/*.html"],
  darkMode: "class",
  theme: {
    extend: {
      appearance: ["responsive"],
      colors: {
        dark: "#1a1b1e",
      },
    },
  },
  daisyui: {
    themes: ["dark"],
  },
  plugins: [require("daisyui"), require("@tailwindcss/forms")],
};
