// Mendapatkan timestamp saat halaman dimuat
const startTime = new Date().getTime();

// Temukan elemen dengan id "question_data"
var questionElement = document.getElementById("question_data");

// Dapatkan nilai dari atribut data-question
var questionDataString = questionElement.getAttribute("data-question");

// Dapatkan nilai id quiz
var quiz_id = questionElement.getAttribute("data-quizId");

// String JSON
const jsonString = `${questionDataString}`;

// Parse string JSON menjadi objek JavaScript
const questionsData = JSON.parse(jsonString);

// Membuat array untuk menyimpan status jawaban
let answeredStatus = new Array(questionsData.length).fill(false);
let selectedChoices = new Array(questionsData.length).fill(null);
let selectedChoicesText = new Array(questionsData.length).fill(null);

document.addEventListener("DOMContentLoaded", function () {
  const exitQuizButton = document.getElementById("exit-quiz");
  const exitQuizModal = document.getElementById("modal-exit-quiz");

  // Tambahkan event listener untuk tombol "Quit Quiz"
  exitQuizButton.addEventListener("click", function () {
    // Tampilkan modal
    exitQuizModal.classList.remove("hidden");
    exitQuizModal.classList.add("block");

    const exitTrueButton = document.getElementById("exit-true");
    const exitFalseButton = document.getElementById("exit-false");
    // Tambahkan event listener untuk tombol "Ya, Saya Yakin" pada modal
    exitTrueButton.addEventListener("click", function () {
      // Sembunyikan modal
      exitQuizModal.classList.remove("block");
      exitQuizModal.classList.add("hidden");

      // Redirect ke halaman dashboard (gantilah URL sesuai kebutuhan Anda)
      window.location.href = "/Dashboard";
    });

    // Tambahkan event listener untuk tombol "Tidak" pada modal
    exitFalseButton.addEventListener("click", function () {
      // Sembunyikan modal
      exitQuizModal.classList.remove("block");
      exitQuizModal.classList.add("hidden");
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const previousButton = document.getElementById("previousButton");
  const nextButton = document.getElementById("nextButton");

  // Tambahkan event listener untuk tombol "Previous"
  previousButton.addEventListener("click", function () {
    navigateQuestion(-1);
  });

  // Tambahkan event listener untuk tombol "Next"
  nextButton.addEventListener("click", function () {
    const currentIndex =
      parseInt(document.getElementById("number").innerText) + 1;
    if (currentIndex == questionsData.length) {
      nextButton.innerText = "Submit";
    }
    navigateQuestion(1);
  });

  // Fungsi untuk mengirim data ke server
  function submitQuizData() {
    // Mendapatkan perbedaan waktu saat tombol "Kumpulkan" ditekan
    const endTime = new Date().getTime();
    const elapsedTime = endTime - startTime;

    // Membuat objek dengan data dan estimasi waktu
    let selectedChoicesObject = {
      selectedChoices: {},
      estimatedTime: elapsedTime,
      selectedChoicesText: {},
    };
    console.log(elapsedTime);

    for (let i = 0; i < selectedChoices.length; i++) {
      selectedChoicesObject.selectedChoices[i + 1] = selectedChoices[i];
      selectedChoicesObject.selectedChoicesText[i + 1] = selectedChoicesText[i];
    }

    // Mengirim data ke server Flask
    fetch("/submit-answers/" + quiz_id, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(selectedChoicesObject),
    })
      .then((response) => response.json())
      .then((data) => {
        const modalSubmitQuiz = document.getElementById("modal-submit-quiz");
        // Sembunyikan modal setelah menangani pengumpulan kuis
        modalSubmitQuiz.classList.remove("block");
        modalSubmitQuiz.classList.add("hidden");

        // Tampilkan modal hasil kuis dengan data dari server
        const modalResult = document.getElementById("popup-modal-result");
        modalResult.classList.remove("hidden");
        modalResult.classList.add("block");

        // Tampilkan data hasil kuis di dalam modal
        const scoreUserElement = document.getElementById("score-user");
        const messageElement = document.getElementById("message");
        const totalAnsweredElement = document.getElementById("total-answered");
        const correctAnswersElement =
          document.getElementById("correct-answers");
        const incorrectAnswersElement =
          document.getElementById("incorrect-answers");

        scoreUserElement.innerText = data.score;
        messageElement.innerText = data.message;
        totalAnsweredElement.innerText = "Soal Terjawab: " + data.totalAnswered;
        correctAnswersElement.innerText =
          "Jawaban Benar: " + data.correctAnswers;
        incorrectAnswersElement.innerText =
          "Jawaban Salah: " + data.incorrectAnswers;

        // Tombol "Dashboard"
        const dashboardButton = document.getElementById(
          "dashoard-modal-result"
        );
        dashboardButton.addEventListener("click", function () {
          // Tambahkan logika untuk pergi ke dashboard
          window.location.href = "/Dashboard";

          // Sembunyikan modal setelah menekan tombol
          modalResult.classList.remove("block");
          modalResult.classList.add("hidden");
        });
      })
      .catch((error) => {
        console.error("Terjadi kesalahan:", error);
      });
  }

  function controller_question(index) {
    const questionData = questionsData[index];

    document.getElementById("number").innerText = questionData.number;
    document.getElementById("soal").innerText = questionData.text;
    // Inisialisasi MathJax pada elemen yang berisi teks matematika
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "soal"]);

    document.getElementById("choice_a_text").innerText =
      questionData.choices[0];
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "choice_a_text"]);
    document.getElementById("choice_b_text").innerText =
      questionData.choices[1];
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "choice_b_text"]);
    document.getElementById("choice_c_text").innerText =
      questionData.choices[2];
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "choice_c_text"]);
    document.getElementById("choice_d_text").innerText =
      questionData.choices[3];
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "choice_d_text"]);

    choices_option = ["a", "b", "c", "d"];
    for (let i = 0; i < choices_option.length; i++) {
      const selectedChoiceElement = document.getElementById(
        `choice_${choices_option[i]}`
      );
      selectedChoiceElement.classList.remove("bg-blue-500");
    }

    if (selectedChoices[index] !== null) {
      const selectedChoiceElement = document.getElementById(
        `choice_${selectedChoices[index]}`
      );
      selectedChoiceElement.classList.add("bg-blue-500");
    }
  }

  // Fungsi untuk menavigasi pertanyaan (kembali atau maju)
  function navigateQuestion(direction) {
    // Mendapatkan nilai index dari elemen dengan ID "number"
    const currentIndex =
      parseInt(document.getElementById("number").innerText) - 1;

    // Hitung index pertanyaan yang akan ditampilkan
    const newIndex = currentIndex + direction;

    // Pastikan index berada dalam rentang pertanyaan yang valid
    if (newIndex >= 0 && newIndex < questionsData.length) {
      controller_question(newIndex);
    }

    if (newIndex >= questionsData.length) {
      // Tampilkan modal
      const modalSubmitQuiz = document.getElementById("modal-submit-quiz");
      modalSubmitQuiz.classList.remove("hidden");
      modalSubmitQuiz.classList.add("block");

      // Tombol "Ya, Saya Yakin"
      const submitButton = document.getElementById("kumpulkan");
      submitButton.addEventListener("click", function () {
        submitQuizData();
      });

      // Tombol "Tidak"
      const cancelButton = document.getElementById("tidak");
      cancelButton.addEventListener("click", function () {
        // Logika untuk tombol "Tidak"
        // Tambahkan logika spesifik Anda di sini
        // Misalnya, Anda mungkin ingin menutup modal tanpa mengumpulkan kuis
        console.log("Pengumpulan kuis dibatalkan.");

        // Sembunyikan modal setelah menangani tombol "Tidak"
        modalSubmitQuiz.classList.remove("block");
        modalSubmitQuiz.classList.add("hidden");
      });
    }
  }

  const questionElements = document.querySelectorAll('[id^="question-"]');

  // Inisialisasi MathJax pada elemen yang berisi teks matematika
  MathJax.Hub.Queue(["Typeset", MathJax.Hub, "soal"]);

  questionElements.forEach(function (element, index) {
    element.addEventListener("click", function () {
      controller_question(index);
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

    // Inisialisasi MathJax pada elemen yang berisi teks matematika
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "soal"]);
  }
});

function selectAnswer(choice) {
  choice = choice.toLowerCase();

  // Mendapatkan nilai index dari elemen dengan ID "number"
  const index = parseInt(document.getElementById("number").innerText) - 1;

  // Set background color for the selected choice
  const selectedChoiceElement = document.getElementById(
    `question-${index + 1}`
  );

  choices_option = ["a", "b", "c", "d"];
  const index_choice = choices_option.indexOf(choice);

  // Simpan pilihan yang dipilih ke dalam array
  selectedChoices[index] = choice;
  selectedChoicesText[index] = questionsData[index].choices[index_choice];

  // Mengubah status jawaban menjadi true jika pertanyaan sudah terjawab
  answeredStatus[index] = true;

  choices_option = ["a", "b", "c", "d"];
  for (let i = 0; i < choices_option.length; i++) {
    const selectedChoiceElement = document.getElementById(
      `choice_${choices_option[i]}`
    );
    selectedChoiceElement.classList.remove("bg-blue-500");
  }

  if (selectedChoices[index] !== null) {
    const selectedChoiceElement = document.getElementById(
      `choice_${selectedChoices[index]}`
    );
    selectedChoiceElement.classList.add("bg-blue-500");
    // console.log(selectedChoiceElement);
  }
  // Menambahkan kelas 'bg-orange-300' jika pertanyaan sudah terjawab
  if (answeredStatus[index]) {
    selectedChoiceElement.classList.remove("bg-slate-400");
    selectedChoiceElement.classList.add("bg-orange-300");
  }
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
    submitQuizData();
  }
}

function padZero(num) {
  return (num < 10 ? "0" : "") + num;
}
