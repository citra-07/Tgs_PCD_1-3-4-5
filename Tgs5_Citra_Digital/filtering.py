import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================================
# KONFIGURASI FOLDER
# ==========================================================

folder_input = Path("CitraIjazah5")

folder_mean = Path("hasil/mean_filter")
folder_median = Path("hasil/median_filter")
folder_gaussian = Path("hasil/gaussian_filter")
folder_sharpening = Path("hasil/sharpening")
folder_perbandingan = Path("hasil/perbandingan_filter")


# ==========================================================
# MEMBUAT FOLDER HASIL
# ==========================================================

folder_mean.mkdir(parents=True, exist_ok=True)
folder_median.mkdir(parents=True, exist_ok=True)
folder_gaussian.mkdir(parents=True, exist_ok=True)
folder_sharpening.mkdir(parents=True, exist_ok=True)
folder_perbandingan.mkdir(parents=True, exist_ok=True)


# ==========================================================
# MENCARI GAMBAR
# ==========================================================

daftar_gambar = sorted(
    list(folder_input.glob("*.jpg"))
    + list(folder_input.glob("*.jpeg"))
    + list(folder_input.glob("*.png"))
    + list(folder_input.glob("*.bmp"))
)


if not daftar_gambar:
    print("Tidak ada gambar di folder:", folder_input)
    exit()


# ==========================================================
# INFORMASI PROGRAM
# ==========================================================

print("=" * 70)
print("FILTERING CITRA NOMOR IJAZAH")
print("=" * 70)

print()
print(f"Folder input  : {folder_input}")
print(f"Jumlah gambar : {len(daftar_gambar)}")


# ==========================================================
# PROSES SEMUA GAMBAR
# ==========================================================

for nomor, file_gambar in enumerate(daftar_gambar, start=1):

    print()
    print("-" * 70)
    print(f"[{nomor}/{len(daftar_gambar)}] {file_gambar.name}")
    print("-" * 70)

    # ------------------------------------------------------
    # BACA GAMBAR
    # ------------------------------------------------------

    gambar = cv2.imread(str(file_gambar))

    if gambar is None:
        print("Gambar gagal dibaca.")
        continue

    # Ubah ke grayscale
    gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)


    # ------------------------------------------------------
    # 1. MEAN FILTER
    # ------------------------------------------------------

    mean_filter = cv2.blur(
        gray,
        (5, 5)
    )


    # ------------------------------------------------------
    # 2. MEDIAN FILTER
    # ------------------------------------------------------

    median_filter = cv2.medianBlur(
        gray,
        5
    )


    # ------------------------------------------------------
    # 3. GAUSSIAN FILTER
    # ------------------------------------------------------

    gaussian_filter = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )


    # ------------------------------------------------------
    # 4. SHARPENING
    # ------------------------------------------------------

    kernel_sharpening = np.array([
        [0, -1,  0],
        [-1, 5, -1],
        [0, -1,  0]
    ])

    sharpening = cv2.filter2D(
        gray,
        -1,
        kernel_sharpening
    )


    # ------------------------------------------------------
    # NAMA FILE
    # ------------------------------------------------------

    nama = file_gambar.stem


    # ------------------------------------------------------
    # SIMPAN HASIL
    # ------------------------------------------------------

    cv2.imwrite(
        str(folder_mean / f"{nama}_mean.jpg"),
        mean_filter
    )

    cv2.imwrite(
        str(folder_median / f"{nama}_median.jpg"),
        median_filter
    )

    cv2.imwrite(
        str(folder_gaussian / f"{nama}_gaussian.jpg"),
        gaussian_filter
    )

    cv2.imwrite(
        str(folder_sharpening / f"{nama}_sharpening.jpg"),
        sharpening
    )


    # ======================================================
    # PERBANDINGAN HASIL
    # ======================================================

    plt.figure(figsize=(12, 8))


    # Original
    plt.subplot(2, 3, 1)

    plt.imshow(
        gray,
        cmap="gray"
    )

    plt.title("Original")
    plt.axis("off")


    # Mean
    plt.subplot(2, 3, 2)

    plt.imshow(
        mean_filter,
        cmap="gray"
    )

    plt.title("Mean Filter")
    plt.axis("off")


    # Median
    plt.subplot(2, 3, 3)

    plt.imshow(
        median_filter,
        cmap="gray"
    )

    plt.title("Median Filter")
    plt.axis("off")


    # Gaussian
    plt.subplot(2, 3, 4)

    plt.imshow(
        gaussian_filter,
        cmap="gray"
    )

    plt.title("Gaussian Filter")
    plt.axis("off")


    # Sharpening
    plt.subplot(2, 3, 5)

    plt.imshow(
        sharpening,
        cmap="gray"
    )

    plt.title("Sharpening")
    plt.axis("off")


    # Judul
    plt.suptitle(
        f"Perbandingan Filtering - {nama}",
        fontsize=14
    )

    plt.tight_layout()


    # ------------------------------------------------------
    # SIMPAN PERBANDINGAN
    # ------------------------------------------------------

    path_perbandingan = (
        folder_perbandingan
        / f"{nama}_perbandingan.png"
    )

    plt.savefig(
        str(path_perbandingan),
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


    # ------------------------------------------------------
    # INFORMASI
    # ------------------------------------------------------

    print("Mean filter       : selesai")
    print("Median filter     : selesai")
    print("Gaussian filter   : selesai")
    print("Sharpening        : selesai")

    print(
        f"Hasil perbandingan: {path_perbandingan}"
    )


# ==========================================================
# SELESAI
# ==========================================================

print()
print("=" * 70)
print("PROSES FILTERING SELESAI")
print("=" * 70)

print()
print("Hasil tersimpan di:")
print("- hasil/mean_filter")
print("- hasil/median_filter")
print("- hasil/gaussian_filter")
print("- hasil/sharpening")
print("- hasil/perbandingan_filter")