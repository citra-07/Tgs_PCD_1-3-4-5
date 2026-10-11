# Analisis Citra Ijazah Menggunakan Grayscale dan Histogram

## 1. Deskripsi Proyek

Proyek ini dibuat untuk menganalisis sembilan citra ijazah dengan kondisi pencahayaan dan kualitas gambar yang berbeda. Pengolahan dilakukan menggunakan Python, OpenCV, NumPy, dan Matplotlib.

Tujuan proyek ini adalah mengubah citra berwarna menjadi grayscale, menampilkan histogram citra asli dan grayscale, menganalisis distribusi intensitas piksel, serta menentukan metode image enhancement yang sesuai dengan kondisi setiap gambar.

## 2. Tujuan

- Mengubah citra ijazah berwarna menjadi grayscale.
- Membuat histogram RGB dari citra asli.
- Membuat histogram intensitas piksel dari citra grayscale.
- Menganalisis tingkat kecerahan, kontras, dan penyebaran intensitas piksel.
- Mengidentifikasi permasalahan citra, seperti terlalu gelap, terlalu terang, kontras rendah, pencahayaan tidak merata, dan noise.
- Menentukan metode enhancement yang sesuai untuk setiap citra.

## 3. Teknologi yang Digunakan

- Python 3.10.6
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

## 4. Struktur Folder

```text
Tugas7_PCD_F1G124005_Citra/
├── Foto_Ijazah/
│   ├── foto1.jpg.jpg
│   ├── foto2.jpg.jpg
│   ├── foto3.jpg.jpg
│   ├── foto4.jpg.jpg
│   ├── foto5.jpg.jpg
│   ├── foto6.jpg.jpg
│   ├── foto7.jpg.jpg
│   ├── foto8.jpg.jpg
│   └── foto9.jpg.jpg
├── Hasil_Grayscale/
├── Hasil_Histogram/
│   ├── Histogram_Asli/
│   └── Histogram_Grayscale/
├── grayscale.py
├── histogram.py
└── README.md
```

Nama `grayscale.py` dan `histogram.py` merupakan nama yang disarankan untuk file kode. Sesuaikan dengan nama file Python yang digunakan di komputer.

## 5. Cara Menjalankan Program

### A. Persiapan

Pastikan Python sudah terpasang. Buka terminal di folder proyek, lalu instal library yang dibutuhkan:

```bash
python -m pip install opencv-python numpy matplotlib
```

### B. Menjalankan Grayscale

Jalankan perintah:

```bash
python grayscale.py
```

Program membaca sembilan gambar dari folder `Foto_Ijazah`, mengubahnya menjadi grayscale, kemudian menyimpan hasilnya di folder `Hasil_Grayscale`.

### C. Menjalankan Histogram

Jalankan perintah:

```bash
python histogram.py
```

Program menampilkan informasi intensitas piksel dan menyimpan histogram citra asli RGB ke folder `Hasil_Histogram/Histogram_Asli`, serta histogram grayscale ke folder `Hasil_Histogram/Histogram_Grayscale`.

Jika nama file Python berbeda, ganti perintah di atas sesuai nama file yang digunakan.

|   |
| - |
|   |

