# Array 3 dimensi A
A = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Array 3 dimensi B
B = [
    [[9, 10], [11, 12]],
    [[13, 14], [15, 16]]
]

hasil = []

# Perkalian matriks
for k in range(2):
    matriks = []

    for i in range(2):
        baris = []

        for j in range(2):
            jumlah = 0

            for x in range(2):
                jumlah += A[k][i][x] * B[k][x][j]

            baris.append(jumlah)

        matriks.append(baris)

    hasil.append(matriks)


# Menampilkan Array A
print("=== ARRAY A ===")
for k in range(2):
    print("Matrix ke-", k + 1)
    for baris in A[k]:
        print(baris)

# Menampilkan Array B
print("\n=== ARRAY B ===")
for k in range(2):
    print("Matrix ke-", k + 1)
    for baris in B[k]:
        print(baris)

# Menampilkan hasil
print("\n=== HASIL PERKALIAN ===")
for k in range(2):
    print("Matrix ke-", k + 1)
    for baris in hasil[k]:
        print(baris)