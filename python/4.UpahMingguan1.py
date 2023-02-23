# Nama file     : 4.UpahMingguan1.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Menghitung gaji karyawan dalam satu minggu berdasarkan jam kerjanya lembur atau tidak.


jam = int(input())
gaji = (20000)
upahlembur = (40000)


if(jam > 48) :
    print (960000 + ((jam-48)*upahlembur))
else :
    print(jam*gaji)