// Fungsi untuk menangani pemilihan menu
function handleMenuSelection(menuText) {
    var selectedValue = document.getElementById('selectedValue');
    selectedValue.innerText = menuText;

    filterLessons(menuText);
}

// Fungsi untuk menyaring elemen-elemen berdasarkan kelas
function filterLessons(menuText) {
    var selectedClass = menuText;
    var lessonElements = document.getElementsByClassName('lesson-element');

    for (var i = 0; i < lessonElements.length; i++) {
        var lessonElement = lessonElements[i];
        var lessonClass = lessonElement.getAttribute('data-class');


        // Jika kelas elemen sama dengan kelas yang dipilih, tampilkan elemen
        if (lessonClass === selectedClass || selectedClass === 'Semua') {
            lessonElement.style.display = 'flex';
        } else {
            // Jika tidak, sembunyikan elemen
            lessonElement.style.display = 'none';
        }
    }
}

function handleLearningClick(button) {
    // Mendapatkan nilai dari atribut data-learning
    var lessonId = button.getAttribute("data-learning");

    window.location.href = '/Learning/' + "get='" + lessonId +"'";
}