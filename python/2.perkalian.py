# Nama file: 2.perkalian.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Perkalian : 2 interger --> interger
# { perkalian (x,y) mengalikan dua buah bilangan interger yaitu a dengan b. dengan menjumlahkan a terhadap a sebanyak b-kali secara rekursif.)

# Realisasi
def perkalian (x,y):
    if y==1:
        return x
    else:
        return x + perkalian(x,y-1)

# Aplikasi
print(perkalian(4,3))