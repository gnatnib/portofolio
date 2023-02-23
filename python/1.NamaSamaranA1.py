# inp = list(input().split(' '))
# print (inp)
print ("Masukkan nama kamu: ")
nama= str(input())

namanama = nama.split()

first = namanama[0]
last = namanama[1]

x = list(first)
y = list(last)

cek=x[0]
x[0]=y[0]
y[0]=cek

print(("".join(x)),("".join(y)))