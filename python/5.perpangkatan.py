# Nama file: 5.perpangkatan.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# perpangkatan : 2 interger --> interger
# { perpangkatan (x,y) memangkatkan dua bilangan yaitu x dengan y dengan mengalikan x terhadap x sebanyak y-kali secara rekursif.)

# Realisasi
def perpangkatan(x,y):
    if y == 0:
        return 1
    else:
        return perpangkatan(x,y-1)*x

# Aplikasi
print (perpangkatan(2,6))