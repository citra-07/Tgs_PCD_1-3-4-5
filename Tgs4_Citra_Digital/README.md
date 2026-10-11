# Image Enhancement pada Area Nomor Ijazah

## 1. Deskripsi Proyek

Proyek ini bertujuan untuk meningkatkan kualitas citra pada area nomor ijazah agar karakter lebih mudah dibaca dan dikenali oleh sistem OCR. Citra yang digunakan sudah dipotong (crop) pada bagian nomor ijazah sehingga proses pengolahan lebih berfokus pada area yang diperlukan.

Tiga metode enhancement yang digunakan adalah brightness adjustment, contrast stretching, dan histogram equalization. Hasil dari setiap metode dibandingkan dengan citra asli melalui tampilan gambar, histogram, dan statistik intensitas piksel.

## 2. Tujuan

- Meningkatkan kualitas citra pada area nomor ijazah.
- Menerapkan brightness adjustment, contrast stretching, dan histogram equalization.
- Membandingkan citra sebelum dan sesudah enhancement.
- Menampilkan histogram sebelum dan sesudah enhancement.
- Menentukan metode yang paling sesuai untuk membantu proses OCR.
- Menjelaskan pengaruh peningkatan kontras terhadap keterbacaan karakter.

## 3. Teknologi yang Digunakan

- Python 3.10.6
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

## 4. Struktur Folder

```text
Tugas7_PCD_F1G124005_Citra/
├── CitraIjazah/
│   ├── 01_HighQuality_Enhanced.jpg
│   ├── 02_LowContrast.jpg
│   ├── 03_Blurred.jpg
│   ├── 04_HighNoise.jpg
│   ├── 05_LowResolution_Upsampled.jpg
│   ├── 06_Faded_Underexposed.jpg
│   ├── 07_ColorShift_WarmTint.jpg
│   ├── 08_JPEGCompression_Artifacts.jpg
│   └── 09_CombinedDegradation.jpg
├── hasil/
│   ├── brightness/
│   ├── contrast_stretching/
│   ├── histogram_equalization/
│   ├── perbandingan/
│   └── histogram/
├── enhancement.py
├── histogram.py
└── README.md
```

## 5. Metode yang Digunakan

### A. Brightness Adjustment

Brightness adjustment digunakan untuk menaikkan atau menurunkan kecerahan citra. Pada program ini, nilai brightness ditetapkan sebesar 20.

Penyesuaian dilakukan dengan menambahkan nilai kecerahan pada piksel. Metode ini dapat membantu jika nomor ijazah terlihat terlalu gelap. Namun, jika citra sudah terang, penambahan brightness dapat membuat bagian putih semakin terang dan detail karakter menjadi kurang jelas.

### B. Contrast Stretching

Contrast stretching memperluas rentang intensitas piksel dari nilai minimum dan maksimum citra menuju rentang 0 sampai 255.

Metode ini membantu membedakan karakter nomor ijazah dengan latar belakang, terutama pada citra yang memiliki kontras rendah. Namun, hasilnya tetap bergantung pada kondisi citra awal dan keberadaan noise.

### C. Histogram Equalization

Histogram equalization mengatur kembali distribusi intensitas piksel agar rentang keabuan lebih tersebar. Tujuannya adalah meningkatkan kontras dan membantu memperjelas detail yang kurang terlihat.

Metode ini dapat berguna pada citra dengan kontras rendah, tetapi tidak selalu memberikan hasil terbaik. Pada citra yang memiliki noise, histogram equalization juga dapat membuat noise semakin terlihat.

## 6. Cara Menjalankan Program

### A. Persiapan

Pastikan Python sudah terpasang. Buka terminal pada folder proyek, kemudian instal library yang diperlukan:

```bash
python -m pip install opencv-python numpy matplotlib
```

### B. Menjalankan Enhancement

Jalankan perintah:

```bash
python enhancement.py
```

Program akan membaca gambar dari folder `CitraIjazah`, mengubahnya menjadi grayscale, menerapkan ketiga metode enhancement, kemudian menyimpan hasilnya ke folder masing-masing.

Hasil gambar perbandingan sebelum dan sesudah enhancement disimpan pada folder `hasil/perbandingan`.

### C. Membuat Histogram

Setelah proses enhancement selesai, jalankan:

```bash
python histogram.py
```

Program akan menampilkan perbandingan histogram citra asli, brightness adjustment, contrast stretching, dan histogram equalization. Hasil histogram disimpan pada folder `hasil/histogram`.

Pastikan nama file Python dan nama folder sesuai dengan yang digunakan di komputer.
