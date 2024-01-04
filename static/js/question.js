// Temukan elemen dengan id "question_data"
var questionElement = document.getElementById("question_data");

// Dapatkan nilai dari atribut data-question
var questionDataString = questionElement.getAttribute("data-question");

// String JSON
const jsonString = `${questionDataString}`;

// Parse string JSON menjadi objek JavaScript
const questionsData = JSON.parse(jsonString);

// Membuat array untuk menyimpan status jawaban
let answeredStatus = new Array(questionsData.length).fill(false);
let selectedChoices = new Array(questionsData.length).fill(null);

document.addEventListener("DOMContentLoaded", function () {
  const questionElements = document.querySelectorAll('[id^="question-"]');
  const selectedColor = "bg-blue-300";

  questionElements.forEach(function (element, index) {
    element.addEventListener("click", function () {
      resetBackground();
      // Reset background color for all elements
      questionElements.forEach(function (el) {
        el.classList.remove(selectedColor);
      });

      // Set background color for the clicked element
      element.classList.add(selectedColor);

      // Dapatkan data soal berdasarkan indeks
      const questionData = questionsData[index];

      choices_option = ["a", "b", "c", "d"];
      for (let i = 0; i < choices_option.length; i++) {
        const selectedChoiceElement = document.getElementById(
          `choice_${choices_option[i]}`
        );
        selectedChoiceElement.classList.remove("bg-blue-400");
      }

      if (selectedChoices[index] !== null) {
        const selectedChoiceElement = document.getElementById(
          `choice_${selectedChoices[index]}`
        );
        selectedChoiceElement.classList.add("bg-blue-400");
      }

      // Tampilkan informasi soal
      document.getElementById("number").innerText = questionData.number + ".";
      document.getElementById("soal").innerText = questionData.text;
      document.getElementById("choice_a_text").innerText =
        questionData.choices[0];
      document.getElementById("choice_b_text").innerText =
        questionData.choices[1];
      document.getElementById("choice_c_text").innerText =
        questionData.choices[2];
      document.getElementById("choice_d_text").innerText =
        questionData.choices[3];
    });
  });

  // Jalankan fungsi simulateClick pada elemen pertama secara otomatis
  simulateClick(questionElements[0]);
  // Fungsi untuk mensimulasikan klik pada suatu elemen
  function simulateClick(element) {
    const event = new MouseEvent("click", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    element.dispatchEvent(event);
  }
});

function selectAnswer(choice) {
  choice = choice.toLowerCase();
  resetBackground();
  
  // Mendapatkan nilai index dari elemen dengan ID "number"
  const index = parseInt(document.getElementById("number").innerText) - 1;

  // Set background color for the selected choice
  const selectedChoiceElement = document.getElementById(
    `question-${index + 1}`
  );

  const UserselectedChoiceElement = document.getElementById(`choice_${choice}`);

  // Simpan pilihan yang dipilih ke dalam array
  selectedChoices[index] = choice;

  // Mengubah status jawaban menjadi true jika pertanyaan sudah terjawab
  answeredStatus[index] = true;

  // Menambahkan kelas 'bg-orange-300' jika pertanyaan sudah terjawab
  if (answeredStatus[index]) {
    selectedChoiceElement.classList.remove("bg-blue-50");
    selectedChoiceElement.classList.add("bg-orange-300");
    UserselectedChoiceElement.classList.add("bg-blue-300");
  }
}

function resetBackground() {
  // Remove background color for all choices
  const choices = document.querySelectorAll('[id^="choice_"]');
  choices.forEach((choice) => {
    choice.classList.remove("bg-blue-300");
  });
}

// Set the countdown date and time
const countdownDate = new Date().getTime() + 5 * 60 * 1000; // 5 minutes from now

// Update the countdown every 1 second
const countdownElement = document.getElementById("timer");
const countdownInterval = setInterval(updateCountdown, 1000);

function updateCountdown() {
  const now = new Date().getTime();
  const distance = countdownDate - now;

  // Calculate minutes and seconds
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the countdown
  countdownElement.innerHTML = `<span>${padZero(minutes)}:${padZero(
    seconds
  )}</span>`;

  // If the countdown is over, display a message
  if (distance < 0) {
    clearInterval(countdownInterval);
    countdownElement.innerHTML = "<span>Time's up!</span>";
  }
}

function padZero(num) {
  return (num < 10 ? "0" : "") + num;
}
