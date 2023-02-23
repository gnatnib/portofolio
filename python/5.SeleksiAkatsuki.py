kkm = int(input())
nilai = list(map(int, input().split(' ')))
for v in nilai[:]:
    if v < kkm:
        nilai.remove(v)

print (len(nilai))