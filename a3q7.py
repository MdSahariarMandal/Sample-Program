n = int(input("Enter the number of terms : "))
x=int(input("Enter the angle of cosine : "))
def Series(n,x):
    for i in range (0,n+1):
     i=i+2
     g=float1(1+((x*(-1**i))/Factorial(i)))
    return g 

def Factorial(a):
    if(a==0):
        return 1
    if(a==1):
     return a;
    else:
     return a*Factorial(a-1)   
     
print(Series(n,x))