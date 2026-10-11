# Perkalian Matriks Array 3 Dimensi Menggunakan Python

## 1. Deskripsi Program

Program ini dibuat untuk melakukan perkalian matriks pada array 3 dimensi menggunakan bahasa pemrograman Python. Program menggunakan dua array, yaitu array A dan array B, yang masing-masing berisi dua matriks berukuran 2 × 2.

Perkalian dilakukan menggunakan perulangan `for` untuk menghitung hasil perkalian setiap matriks pada array A dengan matriks yang sesuai pada array B. Hasil perkalian kemudian ditampilkan melalui Command Line Interface (CLI) atau terminal.

## 2. Tujuan

- Memahami penggunaan array 3 dimensi dalam Python.
- Memahami proses perkalian matriks.
- Menerapkan perulangan `for` untuk mengolah elemen matriks.
- Menampilkan array A, array B, dan hasil perkalian melalui CLI.

## 3. Teknologi yang Digunakan

- Bahasa pemrograman Python.
- Python CLI (Command Line Interface).
- Command Prompt (CMD) Windows.

## 4. Struktur Folder

```text
Tugas1_PCD_Matrix_3D/
├── perkalian_matriks.py
├── README.md
└── desktop.ini
```

Keterangan:

- `perkalian_matriks.py`: file program untuk menjalankan perkalian matriks array 3 dimensi.
- `README.md`: file dokumentasi program.
- `desktop.ini`: file konfigurasi tampilan folder Windows, bukan bagian dari proses perhitungan matriks.

## 5. Array yang Digunakan

Program menggunakan array A dan array B berikut.

**Array A**

```python
A = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
```

**Array B**

```python
B = [
    [[9, 10], [11, 12]],
    [[13, 14], [15, 16]]
]
```

Masing-masing array berisi dua matriks berukuran 2 × 2.

## 6. Cara Kerja Program

1. Membuat array A dan array B yang masing-masing berisi dua matriks.
2. Membuat list kosong bernama `hasil` untuk menyimpan hasil perkalian.
3. Menggunakan perulangan `for` untuk memilih matriks yang akan dikalikan.
4. Menggunakan perulangan untuk menentukan baris dan kolom hasil.
5. Menghitung perkalian elemen matriks menggunakan rumus perkalian matriks.
6. Menyimpan hasil perhitungan ke dalam array `hasil`.
7. Menampilkan array A, array B, dan hasil perkalian melalui terminal.

## 7. Cara Menjalankan Program

### A. Membuka CMD

Buka Command Prompt (CMD), kemudian masuk ke folder tempat program disimpan. Contohnya:

```cmd
cd C:\Users\HP\Tugas1_PCD_Matrix_3D
```

Sesuaikan alamat folder jika lokasi proyek berbeda.

### B. Memeriksa Python

Jalankan perintah:

```cmd
python --version
```

Jika versi Python muncul, berarti Python dapat dipanggil melalui CMD.

### C. Menjalankan Program

Pastikan file program sudah disimpan dengan nama `perkalian_matriks.py`, kemudian jalankan:

```cmd
python perkalian_matriks.py
```

### D. Melihat Hasil

Program akan menampilkan tiga bagian, yaitu:

- Array A
- Array B
- Hasil Perkalian

Semua hasil ditampilkan langsung pada CMD sehingga program dapat dijalankan tanpa antarmuka grafis tambahan.

##
