a=int(input("Enter the upper limit : "))
def Fibonacci(n):
    print("The fibonacci series is as follows : ")
    x=0
    print(x)
    y=1
    print(y)
    for i in range (n-2):
     z=x+y
     x=y
     y=z
     print(z , " ")
Fibonacci(a)
