# Nama file: 9.geometri.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Pembagian : interger --> interger
# { geo(n) menghitung deret geometri 1 + 3 + 9 + 27 + ...)

# Realisasi
def geo(n):
    if n == 0:
        return 0
    else:
        return geo(n-1) + 3**(n-1)

# Aplikasi
print (geo(3))