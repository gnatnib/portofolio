saham = int(input("Masukkan jumlah saham: "))

hasil = 0


for i in range (saham):
    harga= input().split()
    beli = int(harga[0])
    jual = int(harga[1])
    profit = jual - beli
    profit = profit*100
    hasil += profit

print (hasil)