# Nama file: 7.interger.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Pembagian : interger --> interger
# { bilint (n) menghitung deret bilangan interger: 1 + 2 + 3 + 4 + ...)

# Realisasi
def bilint(n):
    if n == 0:
        return 0
    else:
        return bilint(n-1) + n

print (bilint(3))