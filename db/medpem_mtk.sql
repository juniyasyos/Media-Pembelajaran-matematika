-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 30 Jan 2024 pada 15.58
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medpem_mtk`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `answeroption`
--

CREATE TABLE `answeroption` (
  `option_id` int(11) NOT NULL,
  `question_id` int(11) DEFAULT NULL,
  `teks_opsi` text DEFAULT NULL,
  `jawaban_benar` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `answeroption`
--

INSERT INTO `answeroption` (`option_id`, `question_id`, `teks_opsi`, `jawaban_benar`) VALUES
(1, 1, '0', 0),
(2, 1, '1', 1),
(3, 1, '2', 0),
(4, 1, 'Tidak dapat ditentukan', 0),
(5, 2, 'Algoritma tersebut berjalan dalam waktu konstan.', 0),
(6, 2, 'Algoritma tersebut memiliki kompleksitas waktu kuadratik.', 1),
(7, 2, 'Algoritma tersebut memiliki kompleksitas waktu logaritmik.', 0),
(8, 2, 'Algoritma tersebut tidak efisien.', 0),
(9, 3, '\\(a^{m+n}\\)', 1),
(10, 3, '\\(a^{m-n}\\)', 0),
(11, 3, '\\(a^{mn}\\)', 0),
(12, 3, '\\(a^{m/n}\\)', 0),
(13, 4, 'O(n log n)', 1),
(14, 4, '\\(O(n^2)\\)', 0),
(15, 4, 'Keduanya sama efisien', 0),
(16, 4, 'Tidak dapat ditentukan', 0),
(17, 5, 'x', 0),
(18, 5, '-x', 0),
(19, 5, '\\(x^{-1}\\)', 1),
(20, 5, '\\(-\\frac{1}{x}\\)', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `bab`
--

CREATE TABLE `bab` (
  `id` int(11) NOT NULL,
  `chapter_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `bab`
--

INSERT INTO `bab` (`id`, `chapter_name`) VALUES
(1, 'Bab 1'),
(2, 'Bab 2'),
(3, 'Bab 3'),
(4, 'Bab 4'),
(5, 'Bab 5'),
(6, 'Bab 6'),
(7, 'Bab 7'),
(8, 'Bab 8'),
(9, 'Bab 9'),
(10, 'Bab 10');

-- --------------------------------------------------------

--
-- Struktur dari tabel `class`
--

CREATE TABLE `class` (
  `id` int(11) NOT NULL,
  `class_name` varchar(255) DEFAULT NULL,
  `semester_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `class`
--

INSERT INTO `class` (`id`, `class_name`, `semester_id`) VALUES
(1, 'Kelas 10', 1),
(2, 'Kelas 10', 2),
(3, 'Kelas 11', 1),
(4, 'Kelas 11', 2),
(5, 'Kelas 12', 1),
(6, 'Kelas 12', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `explanation`
--

CREATE TABLE `explanation` (
  `id` int(11) NOT NULL,
  `text` text NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `priority` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `created_by` varchar(255) NOT NULL,
  `topics_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `lesson`
--

CREATE TABLE `lesson` (
  `id` int(11) NOT NULL,
  `class_id` int(11) DEFAULT NULL,
  `quiz_id` int(11) DEFAULT NULL,
  `lesson_name` varchar(255) DEFAULT NULL,
  `src` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `lesson`
--

INSERT INTO `lesson` (`id`, `class_id`, `quiz_id`, `lesson_name`, `src`) VALUES
(204501, 1, 1, 'Eksponen Dan Logaritma', 'eksponen-dan-logaritma.html'),
(204502, 1, NULL, 'Barisan dan Deret', ''),
(204503, 1, NULL, 'Vektor dan Operasinya', ''),
(204504, 1, NULL, 'Trigonometri', ''),
(204505, 2, NULL, 'Sistem Persamaan dan Pertidaksamaan Linear', ''),
(204506, 2, NULL, 'Fungsi Kuadrat', ''),
(204507, 2, NULL, 'Statistika', ''),
(204508, 2, NULL, 'Peluang', ''),
(204509, 3, NULL, 'Komposisi Fungsi dan Fungsi Invers', ''),
(204510, 3, NULL, 'Lingkaran', ''),
(204511, 3, NULL, 'Statistika', ''),
(204512, 4, NULL, 'Bilangan Kompleks', ''),
(204513, 4, NULL, 'Polinomial', ''),
(204514, 4, NULL, 'Matrix', ''),
(204515, 4, NULL, 'Transformasi Geometri', ''),
(204516, 4, NULL, 'Fungsi dan Pemodelannya', ''),
(204517, 5, NULL, 'Tarformasi Fungsi', ''),
(204518, 5, NULL, 'Busur Dan Juring Lingkaran', ''),
(204519, 5, NULL, 'Kombintorik', ''),
(204520, 6, NULL, 'Geometri Analitik', ''),
(204521, 6, NULL, 'Limit', ''),
(204522, 6, NULL, 'Turunan Fungsi', ''),
(204523, 6, NULL, 'Integral', ''),
(204524, 6, NULL, 'Analisis Data dan Peluang', '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `question`
--

CREATE TABLE `question` (
  `question_id` int(11) NOT NULL,
  `quiz_id` int(11) DEFAULT NULL,
  `teks_pertanyaan` text DEFAULT NULL,
  `tipe_pertanyaan` enum('pilihan_ganda','essai') DEFAULT NULL,
  `point` int(6) NOT NULL DEFAULT 100
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `question`
--

INSERT INTO `question` (`question_id`, `quiz_id`, `teks_pertanyaan`, `tipe_pertanyaan`, `point`) VALUES
(1, 1, 'Apa hasil dari \\(2^0\\)?', 'pilihan_ganda', 100),
(2, 1, 'Jika sebuah algoritma memiliki kompleksitas waktu O(n^2), apa artinya hal tersebut?', 'pilihan_ganda', 100),
(3, 1, 'Menurut hukum eksponen, apa hasil dari \\(a^m \\cdot a^n\\)?', 'pilihan_ganda', 100),
(4, 1, 'Dua algoritma memiliki kompleksitas waktu \\(O(n \\log n)\\) dan \\(O(n^2)\\)  masing-masing. Mana yang lebih efisien untuk masalah skala besar?', 'pilihan_ganda', 100),
(5, 1, 'Jika \\(x\\) adalah bilangan bulat positif, apa nilai dari \\(x^{-1}\\)?', 'pilihan_ganda', 100);

-- --------------------------------------------------------

--
-- Struktur dari tabel `quiz`
--

CREATE TABLE `quiz` (
  `quiz_id` int(11) NOT NULL,
  `judul` varchar(255) DEFAULT NULL,
  `deskripsi` text DEFAULT NULL,
  `waktu_mulai` datetime DEFAULT NULL,
  `waktu_selesai` datetime DEFAULT NULL,
  `tipe` enum('latihan','kuis') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `quiz`
--

INSERT INTO `quiz` (`quiz_id`, `judul`, `deskripsi`, `waktu_mulai`, `waktu_selesai`, `tipe`) VALUES
(1, 'Quiz Eksponen dan Algoritma', 'Deskripsi quiz tentang eksponen dan algoritma', '2023-12-26 05:00:00', '2024-01-30 11:00:00', 'kuis');

-- --------------------------------------------------------

--
-- Struktur dari tabel `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `role_name` varchar(255) DEFAULT NULL,
  `token` int(6) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `created_by` int(11) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `role`
--

INSERT INTO `role` (`id`, `role_name`, `token`, `created_at`, `created_by`, `deskripsi`) VALUES
(1, 'guru', 664351, '2024-01-03 01:29:54', 0, 'Seorang guru memiliki akses penuh untuk mengelola dan mengedit materi pembelajaran. Tugas utamanya termasuk mengedit dan menambahkan konten dalam materi, menetapkan tugas dan ujian kepada siswa, serta memberikan umpan balik kepada siswa.'),
(2, 'siswa', 0, '2023-12-26 13:55:14', 0, 'Seorang siswa memiliki akses untuk mengerjakan tugas, ujian, dan membaca modul pembelajaran. Tugas utamanya termasuk mengerjakan tugas dan ujian yang diberikan oleh guru, serta membaca modul pembelajaran dan mengakses materi pelajaran.'),
(3, 'admin', 976481, '2024-01-03 01:29:54', 0, 'Seorang admin memiliki kontrol penuh terhadap platform pembelajaran. Tugas utamanya termasuk mengelola pengguna dan peran, memantau aktivitas pengguna, dan menangani masalah teknis dan keamanan. Admin memiliki hak akses untuk mengelola akun pengguna, mena');

-- --------------------------------------------------------

--
-- Struktur dari tabel `semester`
--

CREATE TABLE `semester` (
  `id` int(11) NOT NULL,
  `semester_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `semester`
--

INSERT INTO `semester` (`id`, `semester_name`) VALUES
(1, 'semester 1'),
(2, 'semester 2');

-- --------------------------------------------------------

--
-- Struktur dari tabel `topics`
--

CREATE TABLE `topics` (
  `id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `topics_name` varchar(255) NOT NULL,
  `bab_id` int(11) DEFAULT NULL,
  `poin` int(11) NOT NULL DEFAULT 10,
  `src_topics` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `topics`
--

INSERT INTO `topics` (`id`, `lesson_id`, `topics_name`, `bab_id`, `poin`, `src_topics`) VALUES
(1, 204501, 'Definisi Eksponen', 1, 10, 'eksponen-dan-algoritma.html'),
(2, 204501, 'Sifat-sifat Eksponen', 1, 10, 'sifat-eksponen.html'),
(3, 204501, 'Fungsi Eksponen', 1, 10, 'fungsi-eksponen.html'),
(4, 204501, 'Eksponen Pertumbuhan', 1, 10, 'eksponen-pertumbuhan.html'),
(5, 204501, 'Eksponen Peluruhan', 1, 10, 'eksponen-peluruhan.html'),
(6, 204501, 'Eksponen Bentuk Akar', 1, 10, 'eksponen-bentuk-akar.html'),
(7, 204501, 'Hubungan Bilangan Pangkat dan Akar', 1, 10, 'hubungan-bilangan-pangkat-dan-akar.html'),
(8, 204501, 'Merasionalkan Bentuk Akar', 1, 10, 'merasionalkan-bentuk-akar.html'),
(9, 204501, 'Definisi Logaritma', 2, 10, 'definisi-logaritma.html'),
(10, 204501, 'Logaritma Sifat-sifat', 2, 10, 'sifat-logaritma.html'),
(11, 204502, 'Barisan Barisan Aritmetika', 1, 10, ''),
(12, 204502, 'Barisan Geometri', 1, 10, ''),
(13, 204502, 'Deret Deret Aritmetika', 2, 10, ''),
(14, 204502, 'Deret Geometri', 2, 10, ''),
(15, 204502, 'Deret Geometri Tak Hingga', 2, 10, ''),
(16, 204503, 'Terminologi, Notasi dan Jenis Vektor', 1, 10, ''),
(17, 204503, 'Panjang dan Arah Vektor', 1, 10, ''),
(18, 204503, 'Vektor Negatif atau Vektor Lawan', 1, 10, ''),
(19, 204503, 'Vektor Ekuivalen (Vektor yang Sama)', 1, 10, ''),
(20, 204503, 'Vektor dan Sistem Koordinat', 2, 10, ''),
(21, 204503, 'Vektor Berdimensi Dua pada Sistem Koordinat', 2, 10, ''),
(22, 204503, 'Komponen-Komponen Vektor', 2, 10, ''),
(23, 204503, 'Vektor-Vektor Ekuivalen pada Sistem Koordinat Kartesius', 2, 10, ''),
(24, 204503, 'Vektor Berdimensi Tiga pada Sistem Koordinat Kartesius', 2, 10, ''),
(25, 204503, 'Vektor Kolom dan Vektor Baris', 2, 10, ''),
(26, 204503, 'Vektor Satuan dari Suatu Vektor', 2, 10, ''),
(27, 204503, 'Vektor Posisi', 2, 10, ''),
(28, 204503, 'Vektor Berkebalikan', 2, 10, ''),
(29, 204503, 'Operasi Vektor Penjumlahan Vektor', 3, 10, ''),
(30, 204503, 'Penjumlahan Dua Vektor dengan Metode Segitiga', 3, 10, ''),
(31, 204503, 'Penjumlahan Dua Vektor dengan Metode Jajar Genjang', 3, 10, ''),
(32, 204503, 'Penjumlahan dengan Metode Poligon', 3, 10, ''),
(33, 204503, 'Penjumlahan Vektor secara Komponen', 3, 10, ''),
(34, 204503, 'Pengurangan Vektor', 3, 10, ''),
(35, 204503, 'Perkalian Skalar dengan Vektor', 3, 10, ''),
(36, 204504, 'Perbandingan Trigonometri', 1, 10, ''),
(37, 204504, 'Penamaan Sisi Segitiga Siku-siku', 1, 10, ''),
(38, 204504, 'Satu Jenis Perbandingan Trigonometri: tan θ', 1, 10, ''),
(39, 204504, 'Kegunaan Perbandingan Trigonometri tan θ', 1, 10, ''),
(40, 204504, 'Pemanfaatan Perbandingan Trigonometri', 2, 10, ''),
(41, 204504, 'Perbandingan Trigonometri di Piramida Tiga Serangkai', 2, 10, ''),
(42, 204504, 'Perbandingan Trigonometri Sudut Istimewa', 2, 10, ''),
(43, 204504, 'Perbandingan Trigonometri', 2, 10, ''),
(44, 204505, 'Sistem Persamaan Linear', 1, 10, ''),
(45, 204505, 'Sistem Pertidaksamaan Linear', 2, 10, ''),
(46, 204506, 'Karakteristik Fungsi Kuadrat', 1, 10, ''),
(47, 204506, 'Mengkonstruksi Fungsi Kuadrat', 2, 10, ''),
(48, 204506, 'Menyelesaikan Masalah dengan Fungsi Kuadrat', 3, 10, ''),
(49, 204507, 'Histogram', 1, 10, ''),
(50, 204507, 'Frekuensi Relatif', 2, 10, ''),
(51, 204507, 'Ukuran Pemusatan Modus dan Median', 3, 10, ''),
(52, 204507, 'Mean (Rerata atau Rata-rata)', 3, 10, ''),
(53, 204507, 'Penggunaan Ukuran Pemusatan Mean/Rata-rata', 3, 10, ''),
(54, 204507, 'Data Kelompok Median dan Kelas Modus', 3, 10, ''),
(55, 204507, 'Ukuran Penempatan (Measure of Location)', 4, 10, ''),
(56, 204507, 'Kuartil Data Tunggal', 4, 10, ''),
(57, 204507, 'Kuartil Data Kelompok', 4, 10, ''),
(58, 204507, 'Persentil Data Kelompok', 4, 10, ''),
(59, 204507, 'Ukuran Penyebaran Jangkauan', 5, 10, ''),
(60, 204507, 'Inter Kuartil', 5, 10, ''),
(61, 204507, 'Varian dan Simpangan Baku Data Tunggal', 6, 10, ''),
(62, 204507, 'Varian dan Simpangan Baku Data Kelompok', 6, 10, ''),
(63, 204508, 'Distribusi Peluang', 1, 10, ''),
(64, 204508, 'Aturan Penjumlahan Dua Kejadian', 2, 10, ''),
(65, 204508, 'Saling Lepas Dua Kejadian A dan B', 2, 10, ''),
(66, 204508, 'Tidak Saling Lepas Dua Kejadian A dan B', 2, 10, ''),
(67, 204509, 'Fungsi dan Bukan Fungsi', 1, 10, ''),
(68, 204509, 'Domain, Kodomain, dan Range', 1, 10, ''),
(69, 204509, 'Penjumlahan dan Pengurangan Fungsi', 2, 10, ''),
(70, 204509, 'Perkalian dan Pembagian Fungsi', 2, 10, ''),
(71, 204509, 'Komposisi Fungsi', 2, 10, ''),
(72, 204509, 'Fungsi Injektif', 3, 10, ''),
(73, 204509, 'Fungsi Surjektif', 3, 10, ''),
(74, 204509, 'Fungsi Bijektif', 3, 10, ''),
(75, 204510, 'Lingkaran dan Busur Lingkaran', 1, 10, ''),
(76, 204510, 'Lingkaran dan Garis Singgung', 2, 10, ''),
(77, 204510, 'Lingkaran dan Garis Busur', 3, 10, ''),
(78, 204511, 'Diagram Pencar atau Diagram Scatter', 1, 10, ''),
(79, 204511, 'Pengertian Regresi Linear', 2, 10, ''),
(80, 204511, 'Metode Kuadrat Terkecil Regresi Linear', 2, 10, ''),
(81, 204511, 'Pengertian Analisis Korelasi', 3, 10, ''),
(82, 204511, 'Korelasi Product Moment Pada Analisis Korelasi', 3, 10, ''),
(83, 204511, 'Koefisien Determinasi Analisis Korelasi', 3, 10, ''),
(84, 204512, 'Bilangan Kompleks', 1, 10, ''),
(85, 204512, 'Operasi Pada Bilangan Kompleks', 2, 10, ''),
(86, 204512, 'Konjugat', 3, 10, ''),
(87, 204512, 'Modulus', 3, 10, ''),
(88, 204512, 'Argumen Bilangan Kompleks dan Sifat-sifatnya', 3, 10, ''),
(89, 204513, 'Polinomial dan Fungsi Polinomial', 1, 10, ''),
(90, 204513, 'Penjumlahan, Pengurangan, dan Perkalian Polinomial', 2, 10, ''),
(91, 204513, 'Pembagian Polinomial', 3, 10, ''),
(92, 204513, 'Faktor dan Pembuat Nol Polinomial', 4, 10, ''),
(93, 204513, 'Identitas Polinomial', 5, 10, ''),
(94, 204514, 'Menemukan Konsep Matriks', 1, 10, ''),
(95, 204514, 'Jenis-Jenis Matriks', 2, 10, ''),
(96, 204514, 'Kesamaan Dua Matriks', 3, 10, ''),
(97, 204514, 'Penjumlahan dan Pengurangan Antarmatriks', 4, 10, ''),
(98, 204514, 'Perkalian Matriks', 5, 10, ''),
(99, 204514, 'Determinan dan Invers Matriks', 6, 10, ''),
(100, 204515, 'Transformasi pada Bidang Kartesius', 1, 10, ''),
(101, 204515, 'Kaitan Matriks dengan Transformasi', 2, 10, ''),
(102, 204515, 'Komposisi Transformasi dengan Menggunakan Matriks', 3, 10, ''),
(103, 204516, 'Fungsi Trigonometri', 1, 10, ''),
(104, 204516, 'Fungsi Logaritma', 2, 10, ''),
(105, 204516, 'Fungsi Aljabar', 3, 10, ''),
(106, 204517, 'Translasi', 1, 10, ''),
(107, 204517, 'Refleksi', 2, 10, ''),
(108, 204517, 'Dilatasi', 3, 10, ''),
(109, 204517, 'Rotasi', 4, 10, ''),
(110, 204517, 'Kombinasi Transformasi Fungsi', 5, 10, ''),
(111, 204518, 'Busur Lingkaran', 1, 10, ''),
(112, 204518, 'Juring Lingkaran', 2, 10, ''),
(113, 204518, 'Hubungan Panjang Busur dan Luas Lingkaran', 3, 10, ''),
(114, 204519, 'Aturan Pengisian Tempat', 1, 10, ''),
(115, 204519, 'Permutasi', 2, 10, ''),
(116, 204519, 'Kombinasi', 3, 10, ''),
(117, 204519, 'Peluang Satu Kejadian', 4, 10, ''),
(118, 204519, 'Peluang Kejadian Majemuk ', 5, 10, ''),
(119, 204519, 'Peluang Kejadina Majemuk Saling Bebas Bersyarat', 6, 10, ''),
(156, 204520, 'Definisi Lingkaran', 1, 10, ''),
(157, 204520, 'Persamaan Lingkaran', 1, 10, ''),
(158, 204520, 'Kedudukan Suatu Titik Terhadap Lingkaran', 1, 10, ''),
(159, 204520, 'Kedudukan Garis Terhadap Lingkaran', 1, 10, ''),
(160, 204520, 'Persamaan Garis Singgung Lingkaran', 1, 10, ''),
(161, 204520, 'Parabola', 2, 10, ''),
(162, 204520, 'Elips', 2, 10, ''),
(163, 204520, 'Hiperbola', 2, 10, ''),
(164, 204521, 'Definisi Limit Fungsi', 1, 10, ''),
(165, 204521, 'Sifat-sifat Limit Fungsi', 2, 10, ''),
(166, 204521, 'Limit Fungsi Aljabar', 3, 10, ''),
(167, 204521, 'Limit Fungsi Trigonometri', 4, 10, ''),
(168, 204521, 'Aplikasi Limit Fungsi', 5, 10, ''),
(169, 204522, 'Konsep Turunan Fungsi', 1, 10, ''),
(170, 204522, 'Penulisan Turunan Fungsi', 1, 10, ''),
(171, 204522, 'Turunan Fungsi Aljabar', 2, 10, ''),
(172, 204522, 'Turunan Fungsi Trigonometri', 2, 10, ''),
(173, 204522, 'Aturan Rantai pada Turunan', 2, 10, ''),
(174, 204522, 'Persamaan Garis Singgung pada Kurva', 3, 10, ''),
(175, 204522, 'Fungsi Naik, Fungsi Turun, dan Diam (Stasioner)', 3, 10, ''),
(176, 204522, 'Titik Ekstrim, Nilai Balik, dan Nilai Balik Maksimum', 3, 10, ''),
(177, 204522, 'Aplikasi Turunan Diberbagai Bidang Ilmu', 4, 10, ''),
(178, 204523, 'Definisi Integral Tak Tentu', 1, 10, ''),
(179, 204523, 'Sifat-sifat integral tek tentu', 1, 10, ''),
(180, 204523, 'Jumlahan Rienmann', 2, 10, ''),
(181, 204523, 'Integral Tentu', 2, 10, ''),
(182, 204523, 'Sifat-sifat Integral Tentu', 2, 10, ''),
(183, 204523, 'Teorema Dasar Kalkulus', 2, 10, ''),
(184, 204523, 'Luas Bidang Datar', 3, 10, ''),
(185, 204523, 'Penerapan Integral dalam Bidang Ekonomi dan Bisnis', 3, 10, ''),
(186, 204523, 'Penerapan Integral dalam Bidang Fisika', 3, 10, ''),
(187, 204524, 'Distribusi Seragam', 1, 10, ''),
(188, 204524, 'Fungsi Distribusi Binomial', 2, 10, ''),
(189, 204524, 'Nilai Harapan Distribusi Binomial', 2, 10, ''),
(190, 204524, 'Fungsi Distribusi Normal', 3, 10, ''),
(191, 204524, 'Nilai Harapan Distribusi Normal', 3, 10, '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `point` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `activation_code` varchar(255) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `point`, `created_at`, `activation_code`, `role_id`) VALUES
(1, 'juniyasyos', 'juniyasyos@gmail.com', '$2b$12$66mMLH6jGRiynOTZnlmi4erAVp3cYF92mp64nCLZLWBheH.OD4ica', 110, '2024-01-06 02:43:31', '0000', 3),
(2, 'dahlan', '222410103049@mail.unej.ac.id', '$2b$12$JuI9yI3MRU5T4tKBxTOfwuELqmXjHAHwqDGSDMMGJD99MMW5bqTdm', 0, '2024-01-02 19:07:25', '0', 1),
(3, 'Ahmad Ilyas', 'AhmadIlyasD7@gmail.com', '$2b$12$rrGwmqxECCrSet3bmvi1A.yvxdVm.3thCvNMxW6Q7h6b4S4dgOIzO', 0, '2024-01-06 20:02:24', '0', 2),
(4, 'juni', 'arek@gmail.com', '$2b$12$PPl7.hT6FHmjPPaNj0Zgre8A.YnT9yTmOq2fVURlZllkJq12mN6iy', 600, '2024-01-11 09:19:42', '0', 2),
(5, 'hanifa', 'hanifa@gmail.com', '$2b$12$k.r4AuQQ54/bOD4K1AxMBuPvPnIqmZ9OxBp.lFGPcagG0Pa1EgYIO', 600, '2024-01-10 15:25:32', '0', 2),
(6, 'kayla', 'ilyas@gmail.com', '$2b$12$S.hXUiVH9IFXg8A6nYEmt.jVPJp2kCC1qkRdlgA5IlmbV8plVzQWm', 10, '2024-01-13 10:49:46', '0', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_quiz_status`
--

CREATE TABLE `user_quiz_status` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `score` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user_quiz_status`
--

INSERT INTO `user_quiz_status` (`id`, `user_id`, `quiz_id`, `score`, `time`, `date`) VALUES
(2, 1, 1, 400, 9854, '2024-01-10'),
(7, 5, 1, 500, 12376, '2024-01-10'),
(8, 4, 1, 500, 16163, '2024-01-11');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_topic_status`
--

CREATE TABLE `user_topic_status` (
  `id` int(11) NOT NULL,
  `topics_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `reading_duration` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user_topic_status`
--

INSERT INTO `user_topic_status` (`id`, `topics_id`, `user_id`, `reading_duration`) VALUES
(1, 64, 1, 3000),
(2, 1, 1, 112),
(3, 2, 1, 7),
(4, 3, 1, 42),
(5, 4, 1, 19),
(6, 5, 1, 40),
(7, 10, 1, 7),
(8, 9, 1, 31),
(9, 8, 1, 7),
(10, 6, 1, 662),
(11, 7, 1, 26),
(12, 1, 4, 37),
(13, 1, 5, 43),
(14, 2, 5, 42),
(15, 3, 5, 33),
(16, 4, 5, 68),
(17, 5, 5, 27),
(18, 6, 5, 22),
(19, 7, 5, 21),
(20, 8, 5, 39),
(21, 9, 5, 15),
(22, 10, 5, 21),
(23, 2, 4, 12),
(24, 3, 4, 36),
(25, 4, 4, 108),
(26, 5, 4, 11),
(27, 6, 4, 17),
(28, 7, 4, 20),
(29, 8, 4, 12),
(30, 9, 4, 11),
(31, 10, 4, 13),
(32, 1, 6, 73);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `answeroption`
--
ALTER TABLE `answeroption`
  ADD PRIMARY KEY (`option_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indeks untuk tabel `bab`
--
ALTER TABLE `bab`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`),
  ADD KEY `semester_id` (`semester_id`);

--
-- Indeks untuk tabel `explanation`
--
ALTER TABLE `explanation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `topics_id` (`topics_id`);

--
-- Indeks untuk tabel `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indeks untuk tabel `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`question_id`),
  ADD KEY `quiz_id` (`quiz_id`);

--
-- Indeks untuk tabel `quiz`
--
ALTER TABLE `quiz`
  ADD PRIMARY KEY (`quiz_id`);

--
-- Indeks untuk tabel `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `created_by` (`created_by`);

--
-- Indeks untuk tabel `semester`
--
ALTER TABLE `semester`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `topics`
--
ALTER TABLE `topics`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lesson_id` (`lesson_id`),
  ADD KEY `fk_topics_bab` (`bab_id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indeks untuk tabel `user_quiz_status`
--
ALTER TABLE `user_quiz_status`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user` (`user_id`),
  ADD KEY `fk_quiz` (`quiz_id`);

--
-- Indeks untuk tabel `user_topic_status`
--
ALTER TABLE `user_topic_status`
  ADD PRIMARY KEY (`id`),
  ADD KEY `topics_id` (`topics_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `answeroption`
--
ALTER TABLE `answeroption`
  MODIFY `option_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT untuk tabel `explanation`
--
ALTER TABLE `explanation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `lesson`
--
ALTER TABLE `lesson`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=204526;

--
-- AUTO_INCREMENT untuk tabel `question`
--
ALTER TABLE `question`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `quiz`
--
ALTER TABLE `quiz`
  MODIFY `quiz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `topics`
--
ALTER TABLE `topics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=192;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `user_quiz_status`
--
ALTER TABLE `user_quiz_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `user_topic_status`
--
ALTER TABLE `user_topic_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `answeroption`
--
ALTER TABLE `answeroption`
  ADD CONSTRAINT `answeroption_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`);

--
-- Ketidakleluasaan untuk tabel `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `class_ibfk_1` FOREIGN KEY (`semester_id`) REFERENCES `semester` (`id`);

--
-- Ketidakleluasaan untuk tabel `explanation`
--
ALTER TABLE `explanation`
  ADD CONSTRAINT `explanation_ibfk_1` FOREIGN KEY (`topics_id`) REFERENCES `topics` (`id`);

--
-- Ketidakleluasaan untuk tabel `lesson`
--
ALTER TABLE `lesson`
  ADD CONSTRAINT `lesson_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`),
  ADD CONSTRAINT `lesson_ibfk_2` FOREIGN KEY (`quiz_id`) REFERENCES `questions` (`id`);

--
-- Ketidakleluasaan untuk tabel `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`);

--
-- Ketidakleluasaan untuk tabel `topics`
--
ALTER TABLE `topics`
  ADD CONSTRAINT `fk_topics_bab` FOREIGN KEY (`bab_id`) REFERENCES `bab` (`id`),
  ADD CONSTRAINT `topics_ibfk_1` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`id`);

--
-- Ketidakleluasaan untuk tabel `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

--
-- Ketidakleluasaan untuk tabel `user_quiz_status`
--
ALTER TABLE `user_quiz_status`
  ADD CONSTRAINT `fk_quiz` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`),
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Ketidakleluasaan untuk tabel `user_topic_status`
--
ALTER TABLE `user_topic_status`
  ADD CONSTRAINT `user_topic_status_ibfk_1` FOREIGN KEY (`topics_id`) REFERENCES `topics` (`id`),
  ADD CONSTRAINT `user_topic_status_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
