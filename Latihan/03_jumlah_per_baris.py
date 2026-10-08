# Program: 03_jumlah_per_baris.py
# Deskripsi: Menghitung akumulasi jumlah nilai per baris dalam nested loop.

n = 4
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        total_baris += j
    print(f"Baris {i}: jumlah = {total_baris}")