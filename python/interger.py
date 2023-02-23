def plus(x,y):
    if y == 0 :
        return x
    else:
        return 1 + plus (x,y-1)

x=int(input())
y=int(input())

print (plus(x,y))