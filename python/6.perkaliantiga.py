# Nama file: 6.perkaliantiga.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# Pertiga : interger --> interger
# { pertiga(x) menghitung perkalian dengan 3 atau f(x) = 3*x)

# Realisasi
def pertiga(x):
    if x==0:
        return 0
    else:
        return pertiga (x-1) + 3

# Aplikasi
print (pertiga(5))
