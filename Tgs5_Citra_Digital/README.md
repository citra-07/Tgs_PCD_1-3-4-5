## Filtering, Noise Reduction, dan Sharpening

### A. Deskripsi Proyek

Tahap ini dilakukan untuk mengurangi noise dan memperjelas karakter pada citra nomor ijazah. Metode yang digunakan adalah mean filter, median filter, Gaussian filter, dan sharpening. Hasil setiap metode dibandingkan dengan citra asli untuk mengetahui pengaruhnya terhadap keterbacaan nomor ijazah.

### B. Metode yang Digunakan

**1. Mean Filter**

Mean filter menghaluskan citra dengan menghitung rata-rata nilai piksel di sekitar setiap piksel. Metode ini dapat mengurangi noise, tetapi terkadang membuat karakter nomor ijazah menjadi buram.

**2. Median Filter**

Median filter mengganti nilai piksel dengan nilai median dari piksel di sekitarnya. Metode ini cocok untuk mengurangi salt-and-pepper noise karena dapat menghilangkan titik-titik hitam atau putih tanpa terlalu merusak tepi karakter.

**3. Gaussian Filter**

Gaussian filter menghaluskan citra menggunakan pembobotan Gaussian. Metode ini dapat membantu mengurangi noise, tetapi jika terlalu banyak menghaluskan gambar, bentuk karakter bisa menjadi kurang jelas.

**4. Sharpening**

Sharpening digunakan untuk memperjelas tepi dan detail karakter. Metode ini dapat membantu OCR membaca karakter, tetapi juga dapat memperkuat noise jika citra awal memiliki banyak gangguan.

### C. Struktur Folder

```text
Tugas7_PCD_F1G124005_Citra/
├── CitraIjazah5/
│   └── gambar nomor ijazah yang sudah di-crop
├── hasil/
│   ├── mean_filter/
│   ├── median_filter/
│   ├── gaussian_filter/
│   ├── sharpening/
│   ├── perbandingan_filter/
│   └── ocr/
│       └── rekap_ocr.txt
├── filtering.py
├── ocr.py
└── README.md
```

Folder `CitraIjazah5` berisi citra nomor ijazah yang akan diproses. Nama folder harus sama dengan yang digunakan dalam kode program.

### D. Cara Menjalankan Program

**1. Instal library yang diperlukan**

Buka terminal di folder proyek, lalu jalankan:

```bash
python -m pip install opencv-python numpy matplotlib pytesseract
```

Pastikan aplikasi Tesseract OCR juga sudah terpasang di komputer.

**2. Menjalankan Filtering**

Jalankan perintah berikut:

```bash
python filtering.py
```

Program akan menerapkan mean filter, median filter, Gaussian filter, dan sharpening pada setiap gambar. Hasilnya disimpan di folder `hasil`.

**3. Menjalankan OCR**

Setelah proses filtering selesai, jalankan:

```bash
python ocr.py
```

Program akan membaca citra asli dan hasil dari keempat metode filtering menggunakan Tesseract OCR. Hasil pembacaan, jumlah karakter yang benar, dan akurasi akan ditampilkan di terminal dan disimpan dalam file `hasil/ocr/rekap_ocr.txt`.

###
