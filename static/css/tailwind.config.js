/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./base/base_output.css",
    "../../experimen/base.html",
    "../../experimen/dashboard.html",
    "../../experimen/starting_page.html",
    "../../experimen/login.html",
    "../../templates/login.html",
    "../../experimen/register.html",
    "../../experimen/topics.html",
  ],
  theme: {
    extend: {
      "bg-arrow": "#F99437",
    },
  },
  plugins: [],
};
