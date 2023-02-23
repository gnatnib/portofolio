# Nama file     : 6.KuadranTitik.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Menentukan kuadran titik berdasarkan koordinat x,y yang diinput.


x = int(input("Masukkan x : "))
y = int(input("Masukkan y : "))

if (x>0)and(y>0) :
    print ("Titik (",x,",",y,") Berada di Kuadran 1")
elif (x<0)and(y>0) :
    print ("Titik (",x,",",y,") Berada di Kuadran 2")
elif (x<0)and(y<0) :
    print ("Titik (",x,",",y,") Berada di Kuadran 3")
elif (x>0)and(y<0) :
    print ("Titik (",x,",",y,") Berada di Kuadran 4")
else:
    print("Titik Origin")