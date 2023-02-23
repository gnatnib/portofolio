# Nama file: 8.aritmatika.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Pembagian : interger --> interger
# { derit(n) menghitung deret bilangan aritmatika 3 + 6 + 9 + 12 + ...)

# Realisasi
def derit(n):
    if n == 0:
        return 0
    else:
        return derit(n-1) + n*3

# Aplikasi
print (derit(3))