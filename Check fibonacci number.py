import math

a=int(input("Enter the number : "))

def is_Perfect_Square(y):
    x=int(math.sqrt(y))
    return x*x==y

def Check_Fibonacci(n):
  return is_Perfect_Square(5*n*n+4) or is_Perfect_Square(5*n*n-4)
if a==0 or a==1:
    print("Fibonacci number")
else:
    if Check_Fibonacci(a):
        print("It is a Fibonacci number")
    else:
        print("It is not a Fibonacci number")
