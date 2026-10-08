# Program: 02_pola_segitiga.py
# Deskripsi: Menampilkan pola bintang segitiga menggunakan nested loop.

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()