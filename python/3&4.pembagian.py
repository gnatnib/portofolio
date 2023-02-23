# Nama file: 3&4.pembagian.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Pembagian : 2 interger --> interger
# { pembagian (x,y) membagi dua bilangan yaitu x dengan y dengan menghitung jumlah berapa kali a dikurangi b hingga a habis secara rekursif.)

# Realisasi
def pembagian (x,y):
    if x<y:
        return 0
    else:
        return 1 + pembagian(x-y,y)

# Aplikasi
print (pembagian(4,2))