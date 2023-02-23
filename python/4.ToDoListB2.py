n = int(input())
inp = []

if n > 50:
    print ("Tobi tidak bisa bekerja terlalu keras!")
elif n <= 0:
    print ("Tobi tidak ingin bermalas - malasan!")
else:
    for i in range (n): 
        inp.append((input()))
        print (inp)
