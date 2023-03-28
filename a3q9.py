x=int(input("Enter the number : "))
def DigitSum(x):
    b=0
    while(x!=0): 
     a=int(x%10)
     b=int(a+b)
     x=int(x//10)
    return b   
c=int(DigitSum(x)) 
print("The sum of digits is : ",c)