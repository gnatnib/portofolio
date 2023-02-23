# Nama file     : 5.WujudAir.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Menentukan wujud air apakah wujud berupa padat, cair , dan gas berdasarkan temperatur yang diinput dalam satuan celcius.


suhu = float(input())
if (suhu<0):
    print ("Padat")
elif (suhu>=0) and (suhu <= 100):
    print ("Cair")
else:
    print ("Uap")
