/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../experimen/base.html",
    "../../experimen/dashboard.html",
    "../../experimen/starting_page.html",
    "../../experimen/login.html",
    "../../templates/login.html",
    "../../experimen/register.html",
    "../../experimen/topics.html",
    "../../experimen/exercise.html",
    "../../experimen/lesson.html",
    "../../experimen/profil.html",
    "../../experimen/404.html",
    "../../experimen/leaderboard.html",
  ],
  theme: {
    extend: {
      "bg-arrow": "#F99437",
    },
  },
  plugins: [require("flowbite-typography")],
};
