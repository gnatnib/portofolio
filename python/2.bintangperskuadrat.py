# Nama file     : 2.bintangperskuadrat.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 1 September 2022
# Deskripsi     : Menghitung jumlahan kuadrat dari akar akar persamaan kuadrat (x1^2 + x2^2) jika diberikan nilai
#                 a, b, dan c yang merupakan bilangan real.

# Definisi dan Spesifikasi:
# pers_kuadrat : 3 integer> 0 --> real
#   {pers_kuadrat(a,b,c) menghitung nilai akar tambah dari persamaan ax^2+bx+c = 0 menggunakan
#   rumus abc}

# Realisasi
def pers_kuadrat(a,b,c):
    return (-b/a)*(-b/a)-2*(c/a)

# Aplikasi
print("Hasil dari perhitungan berikut yaitu:", pers_kuadrat(1,3,5))