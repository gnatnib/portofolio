n = int(input())

budi = list(map(int,input().strip().split()))[:n]
anto = list(map(int,input().strip().split()))[:n]

sorted = []

for i in range (n):
    if budi[i]<anto[i]:
        sorted.append(i)

print (len(sorted))