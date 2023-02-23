# Python program to display the Fibonacci sequence

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n=22
if n<=1:
    print ("Error")
else:
    for i in range (n):

    print (fibonacci(n))


