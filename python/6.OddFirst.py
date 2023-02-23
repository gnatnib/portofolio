task = list(map(int, input().split(' ')))

odd = []
even = []

for i in task:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)
    else:
        print ("Null")

odd.sort(reverse=True)
even.sort(reverse=True)

total= odd+even

print (total)