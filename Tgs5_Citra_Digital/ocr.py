import cv2
import pytesseract
from pathlib import Path
from textwrap import wrap


# =========================================================
# PENGATURAN TESSERACT
# =========================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# =========================================================
# GROUND TRUTH
# =========================================================

GROUND_TRUTH = "Nomor ijazah: 571012022000056"


# =========================================================
# FOLDER PROJECT
# =========================================================

folder_original = Path("CitraIjazah5")

folder_mean = Path("hasil/mean_filter")
folder_median = Path("hasil/median_filter")
folder_gaussian = Path("hasil/gaussian_filter")
folder_sharpening = Path("hasil/sharpening")

# Folder untuk menyimpan hasil akhir
folder_hasil = Path("hasil/ocr")
folder_hasil.mkdir(
    parents=True,
    exist_ok=True
)


# =========================================================
# FUNGSI MEMBERSIHKAN TEKS
# =========================================================

def bersihkan_teks(teks):

    # Huruf kecil
    teks = teks.lower()

    # Spasi tidak dihitung
    teks = teks.replace(" ", "")

    # Enter tidak dihitung
    teks = teks.replace("\n", "")

    # Carriage return tidak dihitung
    teks = teks.replace("\r", "")

    # Tab tidak dihitung
    teks = teks.replace("\t", "")

    return teks


# =========================================================
# FUNGSI HITUNG KARAKTER BENAR
# =========================================================

def hitung_akurasi(ground_truth, hasil_ocr):

    gt = bersihkan_teks(ground_truth)
    ocr = bersihkan_teks(hasil_ocr)

    karakter_benar = 0

    # Membandingkan karakter berdasarkan posisi
    panjang_min = min(
        len(gt),
        len(ocr)
    )

    for i in range(panjang_min):

        if gt[i] == ocr[i]:
            karakter_benar += 1

    # Akurasi berdasarkan jumlah karakter Ground Truth
    if len(gt) > 0:

        akurasi = (
            karakter_benar / len(gt)
        ) * 100

    else:

        akurasi = 0

    return karakter_benar, akurasi


# =========================================================
# FUNGSI OCR
# =========================================================

def proses_ocr(path_gambar):

    gambar = cv2.imread(
        str(path_gambar)
    )

    if gambar is None:

        return "[Gambar gagal dibaca]"


    # -----------------------------------------------------
    # Grayscale
    # -----------------------------------------------------

    gray = cv2.cvtColor(
        gambar,
        cv2.COLOR_BGR2GRAY
    )


    # -----------------------------------------------------
    # Threshold Otsu
    # -----------------------------------------------------

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )


    # -----------------------------------------------------
    # OCR
    # PSM 7 = satu baris teks
    # -----------------------------------------------------

    konfigurasi = "--psm 7"

    hasil = pytesseract.image_to_string(
        threshold,
        config=konfigurasi
    )


    # -----------------------------------------------------
    # Bersihkan hasil
    # -----------------------------------------------------

    hasil = hasil.strip()

    if hasil == "":

        hasil = "[Tidak terbaca]"


    return hasil


# =========================================================
# FUNGSI MEMBUAT GARIS TABEL
# =========================================================

def garis_tabel():

    return (
        "+"
        + "-" * 16
        + "+"
        + "-" * 34
        + "+"
        + "-" * 16
        + "+"
        + "-" * 11
        + "+"
    )


# =========================================================
# FUNGSI MENAMPILKAN TABEL
# =========================================================

def tampilkan_tabel(metode):

    print()

    print(
        garis_tabel()
    )

    print(
        "| {:<14} | {:<32} | {:>14} | {:>9} |".format(
            "Metode",
            "Hasil OCR",
            "Karakter Benar",
            "Akurasi"
        )
    )

    print(
        garis_tabel()
    )


    for nama_metode, hasil in metode.items():

        karakter_benar, akurasi = (
            hitung_akurasi(
                GROUND_TRUTH,
                hasil
            )
        )


        # Bersihkan enter
        hasil_tampil = hasil.replace(
            "\n",
            " "
        ).replace(
            "\r",
            " "
        ).strip()


        # Pecah teks jika terlalu panjang
        bagian = wrap(
            hasil_tampil,
            width=32
        )


        if not bagian:

            bagian = [""]


        # -------------------------------------------------
        # Baris pertama
        # -------------------------------------------------

        print(
            "| {:<14} | {:<32} | {:>14} | {:>8.2f}% |".format(
                nama_metode,
                bagian[0],
                karakter_benar,
                akurasi
            )
        )


        # -------------------------------------------------
        # Jika hasil OCR lebih panjang
        # -------------------------------------------------

        for teks_lanjutan in bagian[1:]:

            print(
                "| {:<14} | {:<32} | {:>14} | {:>9} |".format(
                    "",
                    teks_lanjutan,
                    "",
                    ""
                )
            )


    print(
        garis_tabel()
    )


# =========================================================
# FUNGSI MENYIMPAN TABEL
# =========================================================

def simpan_tabel(file, metode):

    file.write(
        garis_tabel() + "\n"
    )

    file.write(
        "| {:<14} | {:<32} | {:>14} | {:>9} |\n".format(
            "Metode",
            "Hasil OCR",
            "Karakter Benar",
            "Akurasi"
        )
    )

    file.write(
        garis_tabel() + "\n"
    )


    for nama_metode, hasil in metode.items():

        karakter_benar, akurasi = (
            hitung_akurasi(
                GROUND_TRUTH,
                hasil
            )
        )


        hasil_tampil = hasil.replace(
            "\n",
            " "
        ).replace(
            "\r",
            " "
        ).strip()


        bagian = wrap(
            hasil_tampil,
            width=32
        )


        if not bagian:

            bagian = [""]


        # Baris pertama
        file.write(
            "| {:<14} | {:<32} | {:>14} | {:>8.2f}% |\n".format(
                nama_metode,
                bagian[0],
                karakter_benar,
                akurasi
            )
        )


        # Baris lanjutan
        for teks_lanjutan in bagian[1:]:

            file.write(
                "| {:<14} | {:<32} | {:>14} | {:>9} |\n".format(
                    "",
                    teks_lanjutan,
                    "",
                    ""
                )
            )


    file.write(
        garis_tabel() + "\n"
    )


# =========================================================
# CARI SEMUA GAMBAR ORIGINAL
# =========================================================

daftar_gambar = sorted(
    list(folder_original.glob("*.jpg"))
    + list(folder_original.glob("*.jpeg"))
    + list(folder_original.glob("*.png"))
    + list(folder_original.glob("*.bmp"))
)


# =========================================================
# CEK GAMBAR
# =========================================================

if not daftar_gambar:

    print()
    print("Tidak ada gambar di folder:")
    print(folder_original)
    print()

    exit()


# =========================================================
# INFORMASI AWAL
# =========================================================

print()
print("=" * 79)
print("OCR CITRA NOMOR IJAZAH")
print("=" * 79)

print()
print(
    "Ground Truth:",
    GROUND_TRUTH
)

print()
print(
    "Jumlah gambar:",
    len(daftar_gambar)
)

print()
print(
    "Spasi tidak dihitung."
)


# =========================================================
# FILE HASIL REKAP
# =========================================================

file_rekap = (
    folder_hasil
    / "rekap_ocr.txt"
)


# =========================================================
# BUKA FILE REKAP
# =========================================================

with open(
    file_rekap,
    "w",
    encoding="utf-8"
) as file:


    # =====================================================
    # PROSES SEMUA GAMBAR
    # =====================================================

    for nomor, gambar_original in enumerate(
        daftar_gambar,
        start=1
    ):


        nama = gambar_original.stem


        # =================================================
        # HEADER INFORMASI GAMBAR
        # =================================================

        header = []

        header.append(
            "HASIL OCR CITRA NOMOR IJAZAH"
        )

        header.append(
            "==============================================================================="
        )

        header.append("")

        header.append(
            f"Nama gambar : {nama}"
        )

        header.append(
            f"Ground Truth: {GROUND_TRUTH}"
        )

        header.append(
            "Spasi tidak dihitung."
        )

        header.append("")


        # -------------------------------------------------
        # Tampilkan ke CMD
        # -------------------------------------------------

        print()
        print()

        print(
            "\n".join(header)
        )


        # -------------------------------------------------
        # Simpan ke file
        # -------------------------------------------------

        file.write(
            "\n".join(header)
            + "\n"
        )


        # =================================================
        # ORIGINAL
        # =================================================

        hasil_original = proses_ocr(
            gambar_original
        )


        # =================================================
        # MEAN FILTER
        # =================================================

        path_mean = (
            folder_mean
            / f"{nama}_mean.jpg"
        )

        hasil_mean = proses_ocr(
            path_mean
        )


        # =================================================
        # MEDIAN FILTER
        # =================================================

        path_median = (
            folder_median
            / f"{nama}_median.jpg"
        )

        hasil_median = proses_ocr(
            path_median
        )


        # =================================================
        # GAUSSIAN FILTER
        # =================================================

        path_gaussian = (
            folder_gaussian
            / f"{nama}_gaussian.jpg"
        )

        hasil_gaussian = proses_ocr(
            path_gaussian
        )


        # =================================================
        # SHARPENING
        # =================================================

        path_sharpening = (
            folder_sharpening
            / f"{nama}_sharpening.jpg"
        )

        hasil_sharpening = proses_ocr(
            path_sharpening
        )


        # =================================================
        # KUMPULKAN SEMUA HASIL
        # =================================================

        metode = {

            "Original":
                hasil_original,

            "Mean filter":
                hasil_mean,

            "Median filter":
                hasil_median,

            "Gaussian filter":
                hasil_gaussian,

            "Sharpening":
                hasil_sharpening

        }


        # =================================================
        # TAMPILKAN TABEL
        # =================================================

        tampilkan_tabel(
            metode
        )


        # =================================================
        # SIMPAN TABEL
        # =================================================

        simpan_tabel(
            file,
            metode
        )

        file.write("\n\n")


# =========================================================
# SELESAI
# =========================================================

print()
print()
print("=" * 79)
print("PROSES OCR SELESAI")
print("=" * 79)

print()
print(
    "Hasil tabel tersimpan di:"
)

print(
    "hasil/ocr/rekap_ocr.txt"
)

print()