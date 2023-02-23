# Nama file     : 10.GajiTHR.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Menghitung THR sebuah karyawan berdasarkan golongan karyawan dan lama karyawan tersebut bekerja.

gol = str(input("Masukkan Golongan Karyawan: "))
lamakerja = float(input())

thra= 5/100
thrb = 10/100
thrc = 15/100
thrd = 20/100

if (gol == 'a') or (gol == 'A'):
    if (lamakerja < 1):
        print ((300 + (thra*300)))
    elif (lamakerja < 5) and (lamakerja >= 1):
        print ((320 + (thra*320)))
    elif (lamakerja < 10) and (lamakerja >= 5):
        print ((350 + (thra*350)))
    else:
        print (375 + (thra*375))
elif (gol == 'b') or (gol == 'B'):
    if (lamakerja < 1):
        print ((400 + (thrb*400)))
    elif (lamakerja < 5) and (lamakerja >= 1):
        print ((425 + (thrb*425)))
    elif (lamakerja < 10) and (lamakerja >= 5):
        print ((450 + (thrb*450)))
    else:
        print (480 + (thrb*480))
elif (gol == 'c') or (gol == 'C'):
    if (lamakerja < 1):
        print ((500 + (thrc*500)))
    elif (lamakerja < 5) and (lamakerja >= 1):
        print ((525 + (thrc*525)))
    elif (lamakerja < 10) and (lamakerja >= 5):
        print ((560 + (thrc*560)))
    else:
        print (590 + (thrc*590))
elif (gol == 'd') or (gol == 'D'):
    if (lamakerja < 1):
        print ((600 + (thrd*600)))
    elif (lamakerja < 5) and (lamakerja >= 1):
        print ((630 + (thrd*630)))
    elif (lamakerja < 10) and (lamakerja >= 5):
        print ((660 + (thrd*660)))
    else:
        print (700 + (thrd*700))
else:
    print("Angka tidak valid!")
