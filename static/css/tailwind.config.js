/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./base/base_output.css", "../../templates/base.html", "../../templates/dashboard.html"],
  theme: {
    extend: {
      "bg-arrow":"#F99437"
    },
  },
  plugins: [],
};
