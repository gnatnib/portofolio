# Nama file     : 1.bintangmenghitungdetik.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 1 September 2022
# Deskripsi     : Mengkonversi jam, menit, dan detik yang telah diinput dalam satuan detik dihitung mulai dari waktu 00:00:00 
#                 pada tanggal yang bersangkutan.

# Definisi dan spesifikasi:
# waktu_ke_detik = 3 integer>= 0 --> integer
#   {waktu_ke_detik(j,m,s) menghitung jumlah detik dengan j sebagai jam dengan ketentuan jam <24, m sebagai menit<60
#   dan s sebagai sekon <60}

# Realisasi
def waktu_ke_detik(j,m,s):
    return(j*3600 + m*60 + s)

# Aplikasi
print(waktu_ke_detik(2,15,5))