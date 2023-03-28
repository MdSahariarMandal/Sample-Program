a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
def Factors(a,b):
      if (b==0):
        exit
      if(a%b==0):
         return b
      else:
       return Factors(b,(a%b))

k=int(Factors(a,b))
def Check(k):
    if(k==1):
        return True
    else:
        return False
print(Check(k))
