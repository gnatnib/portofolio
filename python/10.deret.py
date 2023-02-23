from email.generator import DecodedGenerator


# Nama file: 10.deret.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Pembagian : interger --> interger
# { deku(n) menghitung deret bilangan 1 + 4 + 9 + 16 + ...)

# Realisasi
def deku(n):
    if n==0:
        return 0
    else:
        return deku(n-1) + n**2

# Aplikasi
print (deku(3))