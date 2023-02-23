def faktorial(num):

    if (num==0) or (num==1):
       return 1
    elif (num>1):
        return num*faktorial(num-1)

print (faktorial(7))