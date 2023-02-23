def s (v,t):
    if (v <= 330) and (v>0):
        return int((v*t)/2)
    else:
        return ('Pengukuran tidak di bumi!')

nilai1 = int(input())
nilai2 = int(input())

print (s(nilai1,nilai2))