import cv2
import os

# Folder gambar asli
folder_input = "Foto_Ijazah"

# Folder untuk menyimpan hasil grayscale
folder_output = "Hasil_Grayscale"

# Membuat folder output jika belum ada
os.makedirs(folder_output, exist_ok=True)

# Memproses foto 1 sampai foto 9
for i in range(1, 10):

    nama_file = f"foto{i}.jpg.jpg"

    # Lokasi gambar
    path_input = os.path.join(folder_input, nama_file)

    # Membaca gambar
    img = cv2.imread(path_input)

    # Mengecek apakah gambar berhasil dibaca
    if img is None:
        print(f"Gambar tidak ditemukan: {path_input}")
        continue

    # Mengubah BGR/RGB menjadi grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Menyimpan hasil
    path_output = os.path.join(
        folder_output,
        f"foto{i}_grayscale.jpg"
    )

    cv2.imwrite(path_output, gray)

    print(f"Berhasil: {nama_file} -> foto{i}_grayscale.jpg")

print("Semua gambar selesai diproses.")