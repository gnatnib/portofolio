
def pangkat(a,b):
    if (b==0):
        return 1
    else:
        return a * pangkat(a,b-1)

a =int(input(":"))
b =int(input(":"))

print(pangkat(a,b))