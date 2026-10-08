# Program: 04_hitung_pasangan.py
# Deskripsi: Menghitung total iterasi atau pasangan yang memenuhi kondisi tertentu.

n = 4
hitung = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:
            hitung += 1

print(f"Jumlah pasangan dengan (i + j) genap adalah: {hitung}")